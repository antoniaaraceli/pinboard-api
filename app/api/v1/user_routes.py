from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService

router = APIRouter()

service = UserService()


@router.post("/users")
async def create_user(user: UserCreate):

    created_user = await service.create_user(
        username=user.username,
        email=user.email
    )

    created_user["id"] = str(created_user["_id"])

    return created_user


@router.get("/users/{user_id}")
async def get_user(user_id: str):

    user = await service.get_user(user_id)

    user["id"] = str(user["_id"])

    return user


@router.get("/users")
async def list_users():

    users = await service.list_users()

    for user in users:
        user["id"] = str(user["_id"])

    return users