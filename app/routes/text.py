from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.db.database import (
    add_text,
    remove_text,
    get_text,
    get_texts,
    update_text,
)
from app.models.text import (
    TextSchema,
    UpdateTextModel,
)

router = APIRouter()

@router.post("/", response_description="Text data added into the database")
async def add_text_data(text: TextSchema = Body(...)):
    text = jsonable_encoder(text)
    new_text = await add_text(text)
    return new_text


@router.get("/", response_description="All Texts data retrieved")
async def get_texts_data():
    texts = await get_texts()
    if texts:
        return texts
    return texts


@router.get("/{id}", response_description="Text data retrieved")
async def get_text_data(id):
    text = await get_text(id)
    if text:
        return text
    return "An error occurred, Text doesn't exist."


@router.put("/{id}")
async def update_text_data(id: str, req: UpdateTextModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_text = await update_text(id, req)
    if updated_text:
        return update_text
    return "An error occurred, There was an error updating the text data."

@router.delete("/{id}", response_description="Text data deleted from the database")
async def delete_text_data(id: str):
    removed_text = await remove_text(id)
    if removed_text:
        return "Text with ID: {} removed".format(id)
    return "An error occurred, Text with id {0} doesn't exist".format(id)