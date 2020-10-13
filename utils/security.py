from passlib.context import CryptContext
from models.jwt_user import JWTUser
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUITES, JWT_ALGORITH, JWT_SECRET_KEY
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
import jwt
import time

pwd_context = CryptContext(schemes=["bcrypt"])
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")

# password = "pass1"
jwt_user1 = {
    "username":"user1",
    "password":"$2b$12$K.4E0jZiSCRo08iZHRdVRO4Dzi69NPRsEd.KT0e5bzm/FIaTrbz6C",
    "disabled": False,
    "role":"admin"
}
fake_jwt_user1 = JWTUser(**jwt_user1)

def get_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return False

# Authenticate username and password to give JWT token
def authenticate_user(user: JWTUser):
    if fake_jwt_user1.username == user.username:
        if verify_password(user.password, fake_jwt_user1.password):
            user.role = "admin"
            return user
        
    return None

# Create access JWT token
def create_jwt_token(user: JWTUser):
    expiration = datetime.utcnow() + timedelta(JWT_EXPIRATION_TIME_MINUITES)
    jwt_payload = {
        "sub": user.username,
        "role": user.role,
        "exp": expiration,
    }
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITH)

    return jwt_token
    
# Check whether JWT token is correct
def check_jwt_token(token: str=Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITH)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        
        if time.time() < expiration:
            if fake_jwt_user1.username == username:
                print("ok")
                return final_check(role)

    except Exception as e:
        raise False

    raise False

# Last checking and returning the final result
def final_check(role: str):
    print(role)
    if role == "admin":
        return True
    else:
        return False
#print(get_hashed_password("pass1"))