from fastapi import HTTPException, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from starlette import status
from . import crud
from core.models import db_helper, Product


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
