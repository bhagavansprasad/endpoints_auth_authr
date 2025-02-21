from sqlalchemy import Column, Integer, String, TIMESTAMP, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_first_name = Column(String(125), nullable=False)
    user_last_name = Column(String(125), nullable=False)
    user_e_mail_id = Column(String(125), nullable=True)
    user_phone_number = Column(String(125), nullable=True)
    user_login_id = Column(String(125), nullable=False, unique=True)
    user_password = Column(String(250), nullable=False)
    client_id = Column(Integer, ForeignKey("client_master.id", ondelete="CASCADE"), nullable=False)
    created_on = Column(TIMESTAMP, default=datetime.now)
    created_by = Column(String(125), nullable=True)
    modified_on = Column(TIMESTAMP, nullable=True, onupdate=datetime.now)
    modified_by = Column(String(125), nullable=True)
    active_flag = Column(SmallInteger, nullable=False, default=1)

    # Relationship with UserRole
    user_roles = relationship("UserRole", back_populates="user")

    # Relationship with user tokens
    tokens = relationship("UserTokens", back_populates="user", cascade="all, delete-orphan")

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(125), nullable=False)
    role_description = Column(String(250), nullable=False)
    created_on = Column(TIMESTAMP, default=datetime.now)
    created_by = Column(String(125), nullable=True)
    modified_on = Column(TIMESTAMP, nullable=True, onupdate=datetime.now)
    modified_by = Column(String(125), nullable=True)
    active_flag = Column(SmallInteger, nullable=False, default=1)

    # Relationship with UserRole
    user_roles = relationship("UserRole", back_populates="role")


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    created_on = Column(TIMESTAMP, default=datetime.now)
    created_by = Column(String(125), nullable=True)
    modified_on = Column(TIMESTAMP, nullable=True, onupdate=datetime.now)
    modified_by = Column(String(125), nullable=True)
    active_flag = Column(SmallInteger, nullable=False, default=1)

    # Relationships
    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")

class UserTokens(Base):
    __tablename__ = "user_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, nullable=False)
    created_on = Column(TIMESTAMP, default=func.now(), onupdate=func.now(), nullable=False)
    created_by = Column(String, nullable=True)
    modified_on = Column(TIMESTAMP, default=func.now(), onupdate=func.now(), nullable=False)
    modified_by = Column(String, nullable=True)
    active_flag = Column(SmallInteger, nullable=False, default=1)  # Add active_flag with a default value

    # Relationship with User
    user = relationship("User", back_populates="tokens")
