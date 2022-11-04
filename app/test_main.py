# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:46:18 2022

@author: Krzysztof.Joachimiak
"""

from .main import app
from fastapi.testclient import TestClient

# @pytest.fixture
# def client():
#     with TestClient(app) as c:
#         yield c

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    # 'message' instead of message
    assert response.json() == {'message': 'Hello World'}