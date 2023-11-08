from fastapi import APIRouter, status, HTTPException, Request, Response, Depends

from . import dependencies
import requests

from .auth_lib import AuthHandler, AuthLibrary
from .schemas import AuthDetails, AuthRegistred, AuthLogin
import dao

import telebot
router = APIRouter(
    prefix="/auth",
    tags=['auth']

)



@router.post('/register', response_model=AuthRegistred, status_code=status.HTTP_201_CREATED)
async def register(request: Request, response: Response, auth_details: AuthDetails):
    is_login_already_used = await dao.get_user_by_login(auth_details.login)
    if is_login_already_used:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'User with email{auth_details.login} is alerady exist'
        )
    hashed_password = await AuthHandler.get_password_hash(auth_details.password)


    user_data = await dao.create_user(
        name=auth_details.name,
        login=auth_details.login,
        password=hashed_password,
        notes=auth_details.notes,
    )
    token = await AuthHandler.encode_token(user_data[0])
    response.set_cookie(key='my_name', value='Vasyl', max_age=10, httponly=True)
    response.set_cookie(key='token', value=token, httponly=True)
    return AuthRegistred(success=True, id=user_data[0], login=user_data[1])
'''
@router.post('/change_password', response_model=AuthRegistred, status_code=status.HTTP_201_CREATED)
async def change_password(response: Response, auth_details: AuthDetails, auth_handler: AuthHandler):
    is_login_already_used = await dao.get_user_by_login(auth_details.login)
    if is_login_already_used:
        await auth_handler.verify_password(plain_password=auth_details.password, )


    user_data = await dao.create_user(
        name=auth_details.name,
        login=auth_details.login,
        password=hashed_password,
        notes=auth_details.notes,
    )
    token = await AuthHandler.encode_token(user_data[0])
    response.set_cookie(key='my_name', value='Vasyl', max_age=10, httponly=True)
    response.set_cookie(key='token', value=token, httponly=True)
    return AuthRegistred(success=True, id=user_data[0], login=user_data[1])

'''

@router.post('/login')
async def login_api(response: Response, user_data: AuthLogin):
    user = await AuthLibrary.authenticate_user(user_data.login, user_data.password)
    token = await AuthHandler.encode_token(user.id)
    response.set_cookie(key='token', value=token, httponly=True)
    return {'user': user.login, "logged_in": True}


@router.post('/logout')
async def logout_api(response: Response, user=Depends(dependencies.get_current_user_required)):
    response.delete_cookie('token')
    return {'user': user.login, "logged_out": True}