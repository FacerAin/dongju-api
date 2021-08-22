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
    ErrorResponseModel,
    ResponseModel,
    TextSchema,
    UpdateTextModel,
)

router = APIRouter()

@router.post("/", response_description="Text data added into the database")
async def add_text_data(text: TextSchema = Body(...)):
    text = jsonable_encoder(text)
    new_text = await add_text(text)
    return ResponseModel(new_text, "Text added successfully.")


@router.get("/", response_description="All Texts data retrieved")
async def get_texts_data():
    texts = await get_texts()
    if texts:
        return ResponseModel(texts, "Texts data retrieved successfully")
    return ResponseModel(texts, "Empty list returned")


@router.get("/{id}", response_description="Text data retrieved")
async def get_text_data(id):
    text = await get_text(id)
    if text:
        return ResponseModel(text, "Text data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Text doesn't exist.")


@router.put("/{id}")
async def update_text_data(id: str, req: UpdateTextModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_text = await update_text(id, req)
    if updated_text:
        return ResponseModel(
            "Text with ID: {} name update is successful".format(id),
            "Text name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the text data.",
    )

@router.delete("/{id}", response_description="Text data deleted from the database")
async def delete_text_data(id: str):
    removed_text = await remove_text(id)
    if removed_text:
        return ResponseModel(
            "Text with ID: {} removed".format(id), "Text deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Text with id {0} doesn't exist".format(id)
    )