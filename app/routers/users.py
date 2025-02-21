from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.models import User
from app.schemas import UserSchema
from app.security import validate_token, role_required
import logging

router = APIRouter()
security_scheme = HTTPBearer()

@router.get("/users", response_model=List[UserSchema])
def list_users(
    db: Session = Depends(get_db),
    payload: dict = Depends(role_required(["ADMIN", "TEACHER"]))
):
    users = db.query(User).filter(User.active_flag == 1).all()
    if not users:
        raise HTTPException(status_code=404, detail="No active users found")
    return users

@router.get("/first_user", response_model=List[UserSchema])
def first_user(
    db: Session = Depends(get_db),
    payload: dict = Depends(role_required(["ADMIN", "STUDENT"]))
):
    users = db.query(User).filter(User.active_flag == 1).first()
    if not users:
        raise HTTPException(status_code=404, detail="No active users found")
    return [users]

@router.get("/last_user", response_model=List[UserSchema])
def last_user(
    db: Session = Depends(get_db),
    payload: dict = Depends(role_required(["ADMIN", "STUDENT"]))
):
    users = db.query(User).filter(User.active_flag == 1).order_by(User.id.desc()).first()
    if not users:
        raise HTTPException(status_code=404, detail="No active users found")
    return [users]

@router.get("/first_last", response_model=List[UserSchema])
def first_last(
    db: Session = Depends(get_db),
    payload: dict = Depends(role_required(["ADMIN", "TEACHER"]))
):
    first_user = db.query(User).filter(User.active_flag == 1).first()
    last_user = db.query(User).filter(User.active_flag == 1).order_by(User.id.desc()).first()
        
    users = db.query(User).filter(User.active_flag == 1).all()
    if not users:
        raise HTTPException(status_code=404, detail="No active users found")

    return [first_user, last_user]
