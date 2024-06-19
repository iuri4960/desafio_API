from typing import List
from unittest import result
from uuid import UUID

import pytest
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import Product_usecase


async def test_usecases_should_return_success(product_in):
    result = await Product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "iphone 14 pro max"

async def test_usecases_get_should_return_success(product_insert):
    result = await Product_usecase.get(id=product_insert.id)

    assert isinstance(result, ProductOut)
    assert result.name == "iphone 14 pro max"

async def test_usecases_get_shoud_not_found():
     with pytest.raises(NotFoundException)as err:
        await Product_usecase.get(id=UUID())

     assert err.value.args[0] == 'product not found with filter: UUID()'

@pytest.mark.usefixtures('product_insert')
async def test_usecases_query_should_return_success():
    result = await Product_usecase.query()

    assert isinstance(result, List)
    assert len(result)>1

async def test_usecases_update_should_return_success(product_up, product_insert):
    product_up.price= '7.500'
    result = await Product_usecase.update(id=product_insert.id, body= product_up)

    assert isinstance(result, ProductUpdateOut)

async def test_usecases_delete_should_return_success(product_insert):
     result = await Product_usecase.delete(id=product_insert.id)

     assert result is True

async def test_usecases_delete_shoud_not_found():
     with pytest.raises(NotFoundException) as err:
        await Product_usecase.delete(id=UUID())

     assert err.value.args[0] == 'product not found with filter: UUID()'

