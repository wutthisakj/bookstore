from passlib.context import CryptContext
from models.jwt_user import JWTUser
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUITES, JWT_ALGORITH, JWT_SECRET_KEY
import jwt

pwd_context = CryptContext(schemes=["bcrypt"])

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
def authenticate_user(username:str, password:str):
    if fake_jwt_user1.username == username:
        if verify_password(password, fake_jwt_user1.password):
            return True
        
    return False

# Create access JWT token
def create_jwt_token(username: str):
    expiration = datetime.utcnow() + timedelta(minuites=JWT_EXPIRATION_TIME_MINUITES)
    jwt_payload = {"su"

    }
    {
        
    }
# Check whether JWT token is correct

# Last checking and returning the final result

#print(get_hashed_password("pass1"))