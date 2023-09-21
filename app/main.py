from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sentry_sdk
from app.auth import router_auth

from app.web_pages import router_web_pages
from app.sockets import router_websocket


sentry_sdk.init(
    dsn="https://84e5070d48a8fc439d35e4ade9b5184a@o4505760997834752.ingest.sentry.io/4505761038467072",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI(
    title='First our app',
    description='we are champions',
    version='0.0.1',
    debug=True
)
app.mount('/app/static', StaticFiles(directory='app/static'), name='static')
app.include_router(router_web_pages.router)
app.include_router(router_websocket.router)
app.include_router(router_auth.router)

@app.get('/')
async def main_page():
    return {'data': 'something'}


'''
@app.get('/{user_name}')
@app.get('/{user_name}/{user_nik}')
async def user_page(user_name: str, user_nick: str = '', limit: int = 10, skip: int = 0) -> dict:
    data = [i for i in range(1000)]

    return {'user_name': user_name, 'user_nik': user_nick, 'data': data}
'''