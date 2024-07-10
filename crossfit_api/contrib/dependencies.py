from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from crossfit_api.configs.database import get_db

DatabaseDependency = Annotated[AsyncSession, Depends(get_db)]
