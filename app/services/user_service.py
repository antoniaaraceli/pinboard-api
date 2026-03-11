from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, username: str, email: str):

        return await self.repo.create_user(username, email)

    async def get_user(self, user_id: str):

        return await self.repo.get_user_by_id(user_id)

    async def list_users(self):

        return await self.repo.get_all_users()