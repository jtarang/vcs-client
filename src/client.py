from src.client_protocol import VCSClientProtocol
from src.enums import VCSNames
from src.clients.github import GithubClient
from src.clients.gitlab import GitlabClient
from src.exceptions import VCSClientNotSupportedException
from src.models import VCSConnectionObject


class VCSClient:
    """
        VCSClient: Returns a instance of *Client.
                   Check VCSNames for supported clients

    """

    def __init__(self):
        self.supported_clients = {
            VCSNames.GITHUB.__str__(): GithubClient,
            VCSNames.GITLAB.__str__(): GitlabClient
        }

    def _create_client(self, client_type_str: str, vcs_connection_object: VCSConnectionObject) -> VCSClientProtocol:
        """ _create_client: private method that creates the client type specified """
        if client_type_str in self.supported_clients.keys():
            return self.supported_clients[client_type_str](vcs_connection_object=vcs_connection_object)
        raise VCSClientNotSupportedException(client_type_str=client_type_str)

    def get_client(self, client_type: str, vcs_connection_object: VCSConnectionObject) -> VCSClientProtocol:
        """ get_client: returns a instance of VCSClientProtocol """
        return self._create_client(client_type, vcs_connection_object=vcs_connection_object)
