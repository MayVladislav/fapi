from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import dependencies
from . import crud
from .schemas import ProductCreate, Product, ProductUpdate, ProductPartial
from core.models import db_helper

router = APIRouter()


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(product: Product = Depends(dependencies.product_by_id)):
    return product


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(dependencies.product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        session=session, product=product, product_update=product_update
    )


@router.patch("/{product_id}/")
async def update_product(
    product_update: ProductPartial,
    product: Product = Depends(dependencies.product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product_partial(
        session=session, product=product, product_update=product_update
    )


@router.delete("/{product_id}/")
async def delete_product(
    product: Product = Depends(dependencies.product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)
