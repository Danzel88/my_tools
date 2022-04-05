from fastapi import APIRouter, File, UploadFile, Depends
from ..services.marking_sp import Marking


router = APIRouter(prefix='/marking_sp')


@router.post('/')
async def create_sku_table(file: UploadFile = File(...),
                           service: Marking = Depends()):
    return await service.create_table(file)
