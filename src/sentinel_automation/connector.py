"""OAuth2 Graph Connector class."""
import json

import requests

from .base import Base

# Add your credentials here
##########################################################
__CLIENT_ID__ = ''
__CLIENT_SECRET__ = ''
__TENANT_ID__ = ''
##########################################################

class GraphConnector(Base):
    """Main connector object for all connections to graph API."""

    __TOKEN_URL__ = 'https://login.windows.net/{tenant}/oauth2/token'
    __API_VERSION__ = 'v1.0'
    __APP_URL__ = 'https://api.securitycenter.windows.com'

    def __init__(self, client_id, client_secret, tenant_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        
        self.token: str =  None

        self.session = requests.Session()
        self.session.verify = True

    def get_token(self):
        body = {
            'resource' : self.__APP_URL__,
            'client_id' : self.client_id,
            'client_secret' : self.client_secret,
            'grant_type' : 'client_credentials'
        }
        url = self.__TOKEN_URL__.format(tenant=self.tenant_id)
        response = self.session.request('POST', url, data=body).json()
        self.token = response['access_token']

    def invoke(self, method, url, data=None):
        self.get_token()
        self.session.headers = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : "Bearer " + self.token
        }
        self.session.verify = True
        response = self.session.request(method, url, data=data)
        return response
