import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.texts
text_collection = database.get_collection("texts_collection")

def text_helper(text) -> dict:
    return {
            "id": str(text["_id"]),
            "author": text["author"],
            "year": text["year"],
            "emotions": text_collection["emotions"],
            "text": text["text"],
    }

async def add_text()

async def update_text()

async def remove_text()

async def get_text()

async_def get_texts()