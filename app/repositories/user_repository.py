from app.core.database import database
from datetime import datetime
from bson import ObjectId


class UserRepository:

    collection = database["users"]

    async def create_user(self, username: str, email: str):

        user = {
            "username": username,
            "email": email,
            "created_at": datetime.utcnow()
        }

        result = await self.collection.insert_one(user)

        user["_id"] = result.inserted_id

        return user

    async def get_user_by_id(self, user_id: str):

        user = await self.collection.find_one({"_id": ObjectId(user_id)})

        return user

    async def get_all_users(self):

        users_cursor = self.collection.find()

        users = []

        async for user in users_cursor:
            users.append(user)

        return users