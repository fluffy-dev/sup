from fastapi import APIRouter
from src.api.v1.auth.controller import router as auth


router = APIRouter(prefix="/v1", tags=["v1"])
router.include_router(auth)
