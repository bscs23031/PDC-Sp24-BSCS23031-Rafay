from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Simulated shared document
DOCUMENT = {
    "id": 1,
    "content": "Initial text",
    "version": 1
}

class UpdateRequest(BaseModel):
    content: str
    version: int

@router.get("/document")
def get_document():
    return DOCUMENT

@router.put("/document")
def update_document(data: UpdateRequest):

    global DOCUMENT

    if data.version != DOCUMENT["version"]:
        raise HTTPException(
            status_code=409,
            detail="Version conflict detected"
        )

    DOCUMENT["content"] = data.content
    DOCUMENT["version"] += 1

    return {
        "message": "Document updated successfully",
        "document": DOCUMENT
    }