from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

from app.crud.order import order_crud
from app.models.order import Order
from app.schemas.order import (
    OrderCreate, OrderDB, OrderUpdate
)
from app.schemas.orderitem import OrderItemDB
from app.api.validators import check_order_exists, check_quantity
import logging

   
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter()


@router.get(
    '/{order_id}',
    response_model=OrderDB,
    response_model_exclude_none=True,
)
async def get_order_by_id(
    order_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    order = await order_crud.get(order_id, session)
    return order


@router.get(
    '/',
    response_model=list[OrderDB],
    response_model_exclude_none=True,
)
async def get_all_orders(
    session: AsyncSession = Depends(get_async_session)
):
    orders = await order_crud.get_multi(session)
    return orders


@router.get(
        '/details/{order_id}',
        response_model=list[OrderItemDB],
        response_model_exclude_none=True,
)
async def get_order_details(
    order_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    details = await order_crud.get_order_items(session, order_id)
    return details


@router.post(
    '/',
    response_model=OrderDB,
    response_model_exclude_none=True,
)
async def create_new_order(
    order: OrderCreate,
    session: AsyncSession = Depends(get_async_session),
):
    #product_id = order.product_id
    #order = await check_quantity(product_id, session)
    
    new_order = await order_crud.create_order(session, order)
    return new_order


@router.patch(
    '/{order_id}/status',
    response_model=OrderDB,
    response_model_exclude_none=True,
)
async def change_order_status(
    order_id: int,
    obj_in: OrderUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    order = check_order_exists(order_id, session)
    new_status_order = await order_crud.update(order, obj_in.status, session)
    return new_status_order