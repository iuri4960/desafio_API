from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from workout_api.configs.dadabase import get_session

DatabaseDependecy = Annotated[AsyncSession, Depends(get_session)]