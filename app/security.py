from fastapi import HTTPException, Depends, Header
from fastapi.security import HTTPBearer
import jwt
from datetime import datetime, timedelta
import jwt
from sqlalchemy.orm import Session
from app.models import UserTokens
from app.config.config import settings
from fastapi import Header
from typing import List
from app.dependencies import get_db
from pdbwhereami import whereami


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def validate_token(token: str, db: Session):
    payload = None

    whereami(f'token :{token}')
    token_entry = db.query(UserTokens).filter(UserTokens.token == token).first()
    if not token_entry:
        raise HTTPException(status_code=403, detail="Login session expired or invalid session. Please log in again.")
    whereami()

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        whereami()

    except jwt.ExpiredSignatureError:
        db.query(UserTokens).filter(UserTokens.token == token).delete()
        db.commit()
        whereami()
        raise HTTPException(status_code=403, detail="Login session expired. Please log in again.")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid login session. Please log in again.")

    whereami()
    return payload

security_scheme = HTTPBearer()

def role_required(allowed_roles: List[str]):
    def wrapper(
        credentials: str = Depends(security_scheme),  # HTTPBearer automatically parses the token
        db: Session = Depends(get_db),
    ):
        if not credentials or not credentials.credentials:
            raise HTTPException(status_code=403, detail="Authorization header missing or invalid")
        
        whereami()
        token = credentials.credentials
        payload = validate_token(token, db)
        user_roles = payload.get("roles", [])
        whereami()
        
        if "ADMIN" in user_roles:  # Admin has access to everything
            return payload
        whereami()
        
        if not any(role in user_roles for role in allowed_roles):
            raise HTTPException(status_code=403, detail="Access forbidden: Insufficient privileges")
        whereami()
        
        return payload
    return wrapper

