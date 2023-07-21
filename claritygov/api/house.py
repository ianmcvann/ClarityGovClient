from claritygov.api.state import State
import requests
import utils
class House:
    def __init__(self, state: State) -> None:
        self.state = state
        self.state_abbrev = utils.us_state_to_abbrev(state)
        self.api_client = state.api_client
    def get_house_members(self):
        resp = self.api_client.get(f'/{self.state_abbrev}/house/members')
        return resp
