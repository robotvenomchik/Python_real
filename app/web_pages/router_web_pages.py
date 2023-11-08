import json

from fastapi import APIRouter, Request, Form, HTTPException, status, Depends, Response, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr
import requests
from app import menu_data
from app.auth.auth_lib import AuthHandler, AuthLibrary
from app.auth import dependencies
from app import telegram_chanel

import dao

import setting


router = APIRouter(
    prefix='/web',
    tags=['menu', 'landing'],
)

templates = Jinja2Templates(directory='app\\templates')


# @router.get('/')
# async def get_main_page(request: Request):
#     context = {
#         'request': request,
#     }
#
#     return templates.TemplateResponse(
#         'base.html',
#         context=context,
#     )


# @router.get('/menu')
# async def get_menu(request: Request):
#     context = {
#         'request': request,
#         'title': 'Наше меню',
#         'menu': menu_data.menu,
#     }
#
#     return templates.TemplateResponse(
#         'menu.html',
#         context=context,
#     )


@router.post('/search')
@router.get('/menu')
async def get_menu(request: Request, dish_name: str = Form(None), user=Depends(dependencies.get_current_user_optional)):
    filtered_menu = []
    if dish_name:
        for dish in menu_data.menu:
            if dish_name.lower() in dish['title'].lower():
                filtered_menu.append(dish)

    context = {
        'request': request,
        'title': f'Результати пошуку за {dish_name}' if dish_name else 'Наше меню',
        'menu': filtered_menu if dish_name else menu_data.menu,
        'user': user,
        'categories': menu_data.Categories
    }

    return templates.TemplateResponse(
        'menu.html',
        context=context,
    )


@router.get('/about-us')
async def about_us(request: Request, user=Depends(dependencies.get_current_user_optional)):
    context = {
        'request': request,
        'title': 'Про нас',
        'user': user,
    }

    return templates.TemplateResponse(
        'about_us.html',
        context=context,
    )


@router.get('/map')
async def map_drive(request: Request):
    context = {
        'request': request,
        'title': 'Карта проїзду',

    }

    return templates.TemplateResponse(
        'map.html',
        context=context,
    )


@router.get('/message')
async def message(request: Request):
    context = {
        'request': request,
        'title': 'Написати для всіх повідомлення',
    }

    return templates.TemplateResponse(
        'message_to_all.html',
        context=context,
    )


@router.get('/register')
@router.post('/register')
async def register(request: Request):
    context = {
        'request': request,
        'title': 'Реєстрація',
        'min_password_length': setting.Setting.MIN_PASSWORD_LENGTH,
    }

    return templates.TemplateResponse(
        'register.html',
        context=context,
    )

@router.post('/register-final')
async def register_final(request: Request,
                         background_tasks: BackgroundTasks,
                         name: str = Form(),
                         login: EmailStr = Form(),
                         notes: str = Form(default=''),
                         password: str = Form(),
                         ):
    is_login_already_used = await dao.get_user_by_login(login)
    if is_login_already_used:
        context = {
            'request': request,
            'title': 'Помилка користувача',
            'content': f'Користувач {login} уже існує',
        }
        return templates.TemplateResponse(
            '400.html',
            context=context,
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        )
    hashed_password = await AuthHandler.get_password_hash(password)
    user_data = await dao.create_user(
        name=name,
        login=login,
        password=hashed_password,
        notes=notes,
    )
    token = await AuthHandler.encode_token(user_data[0])
    context = {
        'request': request,
        'title': 'Про нас',
        'menu': menu_data.menu,
        'user': user_data,
        'categories': menu_data.Categories
    }
    template_response = templates.TemplateResponse(
        'menu.html',
        context=context,
    )
    template_response.set_cookie(key='token', value=token, httponly=True)
    background_tasks.add_task(telegram_chanel.send_telegram, login, password)

    return template_response

@router.get('/login')
async def login(request: Request):
    context = {
        'request': request,
        'title': 'Ввійти',
    }
    return templates.TemplateResponse(
        'login.html',
        context=context,
    )


@router.post('/login-final')
async def login(request: Request, login: EmailStr = Form(), password: str = Form()):
    user = await AuthLibrary.authenticate_user(login=login, password=password)
    token = await AuthHandler.encode_token(user.id)

    context = {
        'request': request,
        'title': 'Наше меню',
        'menu': menu_data.menu,
        'user': user,
        'categories': menu_data.Categories
    }
    response =  templates.TemplateResponse(
        'menu.html',
        context=context,
    )
    response.set_cookie(key='token', value=token, httponly=True)
    return response

@router.post('/logout')
@router.get('/logout')
async def logout(request: Request, response: Response, user=Depends(dependencies.get_current_user_optional)):
    # response.delete_cookie('token')

    context = {
        'request': request,
        'title': 'Наше меню',
        'menu': menu_data.menu,
        'categories': menu_data.Categories
    }
    result = templates.TemplateResponse(
        'menu.html',
        context=context,
    )
    result.delete_cookie('token')
    return result


@router.get('/by_category/{category_name}')
async def by_category(category_name: str, request: Request, user=Depends(dependencies.get_current_user_optional)):
    menu=[menu for menu in menu_data.menu if category_name in menu['category']]

    context = {
        'request': request,
        'title': f'Наше меню - результати пошуку по категорії {category_name}',
        'menu': menu,
        'user': user,
        'categories': menu_data.Categories
    }
    return templates.TemplateResponse(
        'menu.html',
        context=context,
    )

@router.get('/change_password')
@router.post('/change_password')
async def change_password(request: Request,):

    context = {
        'request': request,
        'title': 'Змінення Паролю',
        'min_password_length': setting.Setting.MIN_PASSWORD_LENGTH,
    }

    return templates.TemplateResponse(
        'change_password.html',
        context=context,
    )

@router.post('/change_password_final')
async def change_password_final(request: Request,

                         new_password: str = Form(),
                         password: str = Form(),
                        user=Depends(dependencies.get_current_user_optional)):

    if not new_password==password:
        context = {
            'request': request,
            'title': 'f',
            'min_password_length': setting.Setting.MIN_PASSWORD_LENGTH,
        }
        return templates.TemplateResponse(
            '400.html',
            context=context,
        )

    hashed_password = await AuthHandler.get_password_hash(new_password)
    await dao.update_user_data(user_id=user.id, params={"password": hashed_password})
    context = {
        'request': request,
        'title': 'Змінення Паролю',
        'min_password_length': setting.Setting.MIN_PASSWORD_LENGTH,
    }

    return templates.TemplateResponse(
        'menu.html',
        context=context,
    )


@router.get('/cart')
async def cart(request: Request, user=Depends(dependencies.get_current_user_optional)):
    context = {
        'request': request,
        'title': 'Кошик',
        'menu': menu_data.menu,
        'user': user,
        'categories': menu_data.Categories
    }

    return templates.TemplateResponse(
        'cart3.html',
        context=context,
    )


@router.post('/checkout')
async def cart(request: Request,
                                background_tasks: BackgroundTasks, user=Depends(dependencies.get_current_user_optional)):
    if not user:
        return {"message": "Вибачте, але Ви повинні увійти щоб зробити замовлення."}

    if not (data := await request.json()):
        return {"message": "Вибачте, але кошик порожній."}


    # PROCESS THE ORDER USING VARIABLE data HERE!!!!!!
    print(data, 99999999999999999)

    names = [item['name'] for item in data]
    print(names, 9999999999999)
    quantity = [item['quantity'] for item in data]
    print(quantity, 999999999999999)

    pepa=zip(names,quantity)
    #print(list(pepa), 234444444444444444444444444)
    print(user.notes)
    s=""
    for item, quantity in pepa:
        s += f'➡️ {item} >>> {quantity} ✅\n'
    s+="\n"+user.notes
    background_tasks.add_task(telegram_chanel.send_telegram2, s)
    return {"message": "Дякуємо за замовлення!"}