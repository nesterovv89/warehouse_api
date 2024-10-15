from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.product import product_crud
from app.models.product import Product
from app.models.order import Order
from app.schemas.orderitem import OrderItem

async def check_order_exists(
        order_id: int,
        session: AsyncSession,
) -> Order:
    order = await order.get(order_id, session)
    if order is None:
        raise HTTPException(
            status_code=422,
            detail='Этого заказа не существует'
        )
    return order


async def check_name_duplicate(
        product_name: str,
        session: AsyncSession,
) -> None:
    product_id = await product_crud.get_product_id_by_name(product_name, session)
    if product_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Товар с таким именем уже есть'
        )
    
async def check_product_exists(
        product_id: int,
        session: AsyncSession,
) -> Product:
    product = await product_crud.get(product_id, session)
    if product is None:
        raise HTTPException(
            status_code=422,
            detail='Этого продукта не существует'
        )
    return product


async def check_quantity(product_id: int, quantity: int, session: AsyncSession):
    product = await product_crud.get(product_id, session)

    if product.quantity < quantity:
        raise HTTPException(
            status_code=400,
            detail=f'Продукта {product.name} недостаточно',
        )

    product.quantity -= quantity
    session.commit()
    session.refresh(product)
    return product