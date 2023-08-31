from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/web',
    tags=['menu','landing']
)

templates=Jinja2Templates(directory='app\\templates')

@router.get('/menu')
async def get_main_page(request: Request):
    context={
        'request': request,

    }
    return templates.TemplateResponse(
        'menu.html',
        context=context
    )
@router.get('/about-us')
async def get_main_page(request: Request):
    context={
        'request': request,

    }
    return templates.TemplateResponse(
        'about_us.html',
        context=context
    )