from enum import Enum
from typing import Optional, List
from uuid import uuid4, UUID

from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"
    others = "others"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


# class Gender(BaseModel):
#     male: str
#     female: str
#     others: str


class User(BaseModel):
    id: UUID | None = uuid4()
    first_name: str = None
    last_name: str = None
    middle_name: str | None = None
    gender: Gender
    roles: list[Role]


class UserUpdateRequest(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    roles: list[Role] | None = None

    # def role_val_checker(self):
    #     accepted_roles = ['user', 'student', 'admin']
    #     if User.roles in accepted_roles:
    #         return True
    #     else:
    #         return False
