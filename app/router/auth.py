from fastapi import APIRouter,status,Response,Depends,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from .. import database,models,utils ,oauth2,schema

router=APIRouter(tags=["Authentication"])

@router.post('/login', response_model=schema.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends() , db:session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
    
    access_token=oauth2.create_access_token({"user_id":user.id})
    return {"access_token":access_token, "token_type":"bearer"}