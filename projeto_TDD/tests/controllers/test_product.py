from typing import List

import pytest
from tests.factories import product_data
from fastapi import status

async def  test_conroller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json= product_data())
    content= response.json()
    del content['created_at']
    del content['update_at']
    del content['id']

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {'name':'iphone 14 pro max', 'quantity':10, 'price':8.500, 'status':True}

async def  test_conroller_get_should_return_success(client, products_url, product_insert):
    response = await client.get(f'{products_url}{product_insert.id}')
    content= response.json()
    del content['created_at']
    del content['update_at']


    assert response.status_code== status.HTTP_200_OK
    assert content == {'id': str(product_insert.id),'name':'iphone 14 pro max', 'quantity':10, 'price':8.500, 'status':True}

async def  test_conroller_get_should_return_not_found(client, products_url):
    response = await client.get(f'{products_url}{id}')

    assert response.status_code ==status.HTTP_404_NOT_FOUND
    assert response.json() == 'product not found with filter: {id}'

@pytest.mark.usefixtures(' products_inserted')
async def  test_conroller_query_should_return_success(client, products_url):
    response = await client.query(products_url)

    assert response.status_code== status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json())>1

async def  test_conroller_patch_should_return_success(client, products_url, product_insert):
    response = await client.patch(f'{products_url}{product_insert.id}',json={'price':'7.500'})
    content= response.json()
    del content['created_at']
    del content['update_at']

    assert response.status_code== status.HTTP_200_OK
    assert content == {'id': str(product_insert.id),'name':'iphone 14 pro max', 'quantity':10, 'price':8.500, 'status':True}

async def  test_conroller_delete_should_return_no_content(client, products_url, product_insert):
    response = await client.delete(f'{products_url}{product_insert.id}')

    assert response.status_code== status.HTTP_204_NO_CONTENT

async def  test_conroller_delete_should_return_not_found(client, products_url):
    response = await client.delete(f'{products_url}{id}')

    assert response.status_code ==status.HTTP_404_NOT_FOUND
    assert response.json() == 'product not found with filter: {id}'