from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.menu_data import menu

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


@router.get('/menu')
async def get_menu(request: Request):
    context = {
        'request': request,
        'title': 'Наше меню',
    }

    return templates.TemplateResponse(
        'menu.html',
        context=context,
    )

@router.get('/about-us')
async def get_menu(request: Request):
    context = {
        'request': request,
        'title': 'Про нас',
        'menu': menu,
    }

    return templates.TemplateResponse(
        'about_us.html',
        context=context,
    )