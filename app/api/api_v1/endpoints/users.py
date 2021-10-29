from fastapi import APIRouter

router = APIRouter()

# /users  already included in endpoints

@router.get("/")
async def get_users():
    return {"message": "Get Users!"}