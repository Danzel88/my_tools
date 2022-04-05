from fastapi import APIRouter


from . import marking_sp


router = APIRouter()
router.include_router(marking_sp.router)


