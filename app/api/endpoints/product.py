from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

from app.crud.product import product_crud
from app.models.product import Product
from app.schemas.product import (
    ProductCreate, ProductDB, ProductUpdate
)
from app.api.validators import check_name_duplicate, check_product_exists

router = APIRouter()


@router.get(
        '/{product_id}',
        response_model=ProductDB,
        response_model_exclude_none=True,
)
async def get_product_by_id(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    product = await product_crud.get(product_id, session)
    return product
    

@router.post(
    '/',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def create_new_product(
    product: ProductCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(product.name, session)
    new_product = await product_crud.create(product, session)
    return new_product


@router.get(
    '/',
    response_model=list[ProductDB],
    response_model_exclude_none=True,
)
async def get_all_products(
    session: AsyncSession = Depends(get_async_session),
):
    all_products = await product_crud.get_multi(session)
    return all_products


@router.put(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def update_product(
    product_id: int,
    obj_in: ProductUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    product = await check_product_exists(product_id, session)
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    product = await product_crud.update(
        product, obj_in, session
    )
    return product

@router.delete(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def remove_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    product = await check_product_exists(product_id, session)
    product = await product_crud.remove(product, session)
    return product
