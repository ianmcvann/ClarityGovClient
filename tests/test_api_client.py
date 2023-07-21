from claritygov.api_client import ClarityAPIClient
import pytest

def test_get():
    client = ClarityAPIClient()
    response = client.get('/md/house/members')
    assert response.status_code == 200