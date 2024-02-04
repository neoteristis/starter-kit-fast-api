from fastapi import FastAPI
from starlette.responses import Response

from .constants.constants import API_VERSION
from .routes import hello

app = FastAPI()
app.include_router(hello.router, prefix=f"/api/{API_VERSION}/hello", tags=["hello"])


# CORS
@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"

    if request.method == "OPTIONS":
        return Response(status_code=200, headers=response.headers)

    return response
