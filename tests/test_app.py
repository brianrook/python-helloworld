import unittest
from unittest import mock

# Setting the default AWS region environment variable required by the Python SDK boto3
with mock.patch.dict('os.environ', {'AWS_REGION': 'us-east-1'}):
    from app import handler




def test_handler():
    response = handler()
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
