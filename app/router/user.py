from fastapi import FastAPI, status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import session
from .. import models, schema, utils
from ..database import get_db


router=APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/" , status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_user(user:schema.UserCreate, db: session=Depends(get_db)):
    # -- hashed password --
    hashed_password=utils.hash(user.password)
    user.password=hashed_password

    new_user= models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schema.UserOut)
def get_user(id:int, db:session=Depends(get_db)):
    get_use= db.query(models.User).filter(models.User.id==id).first()

    if not get_use:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id={id} does not exist")
        
    return get_use
