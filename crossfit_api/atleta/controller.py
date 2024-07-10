from fastapi import APIRouter, status

router = APIRouter()


@router.post("/", summary="Criar a novo atleta", status_code=status.HTTP_201_CREATED)
async def post(db_session:):
    pass
