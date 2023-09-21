from pydantic import BaseModel, Field, EmailStr


class AuthDetails(BaseModel):
    name: str = Field(min_length=3, max_length=50, examples=['Barack Obama'])
    login: EmailStr = Field(examples=["login@ukr.net"])
    password: str=Field(min_length=8, max_length=50, examples=['1321412512'])
    notes: str= Field(default='', max_length=200)

class AuthRegistred(BaseModel):
    success: bool = Field(examples=[True])
    id:int = Field(examples=[565])
    login: EmailStr=Field(examples=['logon@ffa.com'])

class AuthLogin(BaseModel):
    login: EmailStr = Field(examples=["login@ukr.net"])
    password: str=Field(min_length=8, max_length=50, examples=['13214rw4wa12512'])
