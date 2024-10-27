"""Server."""

import typing as tp

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .views import routes as api_routes

# @asynccontextmanager
# async def lifespan(app: FastAPI) -> tp.AsyncGenerator[None, tp.Any]:
#     """Define lifespan for the server.
#     Args:
#         app (FastAPI): server
#     """
#     # sess = await get_connection()
#     sess = await db.get_db_session()
#     app.state.DB = sess
#     yield
#     await sess.close()
# app = FastAPI(lifespan=lifespan)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

routes = APIRouter()


@routes.get('/health')
async def root(req: Request) -> dict[str, tp.Any]:
    """Helper route to see available routes."""
    return {'health': 'ok'}


app.include_router(api_routes)
app.include_router(routes)
