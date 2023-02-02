"""OAuth2 Graph Connector class."""
from string import Template
from typing import Dict
from typing import List

import requests

from .base import Base


class GraphConnector(Base):
    """Main connector object for all connections to graph API."""

    __TOKEN_URL__ = Template("https://login.windows.net/$tenant/oauth2/token")
    __API_VERSION__ = "v1.0"
    __APP_URL__ = "https://api.securitycenter.windows.com"

    def __init__(self, client_id: str, client_secret: str, tenant_id: str) -> None:
        """Initialize our graph connection.

        Args:
            client_id (str): The client ID for your app registration in Azure.
            client_secret (str): The client secret for your app registration in Azure.
            tenant_id (str): The tenant ID for your app registration in Azure.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id

        self.token: str = None

        self.session = requests.Session()
        self.session.verify = True

    def get_token(self) -> None:
        """Makes API call to retrieve token from Graph and saves it to a instance variable called token."""
        body = {
            "resource": self.__APP_URL__,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }
        url = self.__TOKEN_URL__.substitute(tenant=self.tenant_id)
        response = self.session.request("POST", url, data=body).json()
        self.token = response["access_token"]

    def invoke(self, method: str, url: str, data: dict = None) -> Dict or List:
        """Invokes an API call using the provided inputs.

        Args:
            method (str): A HTTP request method. Examples are GET, POST, PUT, DELETE, HEAD
            url (str): The URL to send the request to.
            data (dict): The data object (usually JSON) sent to the API. Defaults to None.

        Returns:
            Dict or List: Returns the response object.
        """
        self.get_token()
        self.session.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.token,
        }
        self.session.verify = True
        response = self.session.request(method, url, data=data)
        return response
