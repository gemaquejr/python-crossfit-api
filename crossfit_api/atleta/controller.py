from fastapi import APIRouter, Body, status
from crossfit_api.atleta.schemas import AtletaIn

from crossfit_api.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post("/", summary="Criar a novo atleta", status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    pass
