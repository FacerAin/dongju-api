import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.texts
text_collection = database.get_collection("texts_collection")
def text_helper(text) -> dict:
    return {
            "id": str(text["_id"]),
            "title": text["title"],
            "author": text["author"],
            "year": text["year"],
            "emotions": text["emotions"],
            "text": text["text"],
    }

#Add a new text into a database 
async def add_text(text_data: dict) -> dict:
    text = await text_collection.insert_one(text_data)
    new_text = await text_collection.find_one({"_id": text.inserted_id})
    return text_helper(new_text)

#Update a Text with a matching ID
async def update_text(id: str, data: dict):
    if len(data) < 1:
        return False
    text = await text_collection.find_one({"_id": ObjectId(id)})
    if text:
        updated_text = await text_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if updated_text:
            return True
        return False
    
#Remove a Text from the database
async def remove_text(id: str):
    text = await text_collection.find_one({"_id": ObjectId(id)})
    if text:
        await text_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False

#Get a Text from the database
async def get_text(id: str) -> dict:
    text = await text_collection.find_one({"_id": ObjectId(id)})
    if text:
        return text_helper(text)
    
#Get ALL texts from the database
async def get_texts():
    texts = []
    async for text in text_collection.find():
        texts.append(text_helper(text))
    return texts