from pydantic import BaseModel
from typing import Optional
from typing import List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    role: str
    client: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    id: int
    user_first_name: str
    user_last_name: str
    user_e_mail_id: Optional[str] = None
    user_phone_number: Optional[str] = None
    user_login_id: str
    client_id: int

    class Config:
        orm_mode = True

class UserTokenSchema(BaseModel):
    id: int
    user_id: int
    token: str
    created_on: datetime
    active_flag: int 
