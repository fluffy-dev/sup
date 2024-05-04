from fastapi import APIRouter, HTTPException, Request, Response

from src.apps.user.dto import UserBaseDTO
from src.apps.user.depenends.service import IUserService
from src.apps.auth.exceptions.token import InvalidSignatureError

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/confirm/{token}")
async def confirmation(token: str, service: IUserService, request: Request):
    """
    controller for registration user
    """
    try:
        confirmed = await service.confirmation_user(token)
        return Response(status_code=200)
    except InvalidSignatureError as e:
        raise HTTPException(detail=e)
