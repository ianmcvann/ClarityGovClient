from claritygov.api.state import State
from claritygov.api_client import ClarityAPIClient
from claritygov.api.house import House

def test_get_house_members():
    api_client = ClarityAPIClient()
    state = State(api_client, 'Maryland')
    house = House(state)
    members = house.get_house_members()
    assert members.status_code == 200
