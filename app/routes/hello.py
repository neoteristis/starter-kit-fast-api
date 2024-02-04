from fastapi import APIRouter

from app.models.message import Message

router = APIRouter()


@router.get("/", response_model=Message, summary="Root API endpoint", description="Returns a greeting message.")
async def root():
    """
    This endpoint returns a simple greeting message.
    """
    return {"message": "Hello World"}


@router.get("/{name}", response_model=Message, summary="Personalized greeting",
            description="Returns a personalized greeting message.")
async def say_hello(name: str):
    """
    This endpoint returns a personalized greeting message.

    - **name**: The name to be included in the greeting message.
    """
    return {"message": f"Hello {name}"}
