from motor.motor_asyncio import AsyncIOMotorClient

class MongoDBHandler:
    def __init__(self):
        mongo_url = "YOUR_MONGODB_URL_HERE"
        self.client = AsyncIOMotorClient(mongo_url)
        self.db = self.client["csv_database"]
        self.collection = self.db["csv_files"]

    async def insert_file(self, file_id: str, file_name: str, data: list):
        await self.collection.insert_one({"file_id": file_id, "file_name": file_name, "data": data})

    async def get_files(self):
        return await self.collection.find({}, {"_id": 0, "file_id": 1, "file_name": 1}).to_list(length=100)

    async def get_file_data(self, file_id: str):
        return await self.collection.find_one({"file_id": file_id}, {"_id": 0, "data": 1})

    async def delete_file(self, file_id: str):
        await self.collection.delete_one({"file_id": file_id})
