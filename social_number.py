import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        endpoint = 'SocialNumber'

        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key": "2d794c6f46094ceb96bd719c1c26c984"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

        return response.status_code
