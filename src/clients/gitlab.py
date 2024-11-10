from ..client_protocol import VCSClientProtocol
from ..models import VCSConnectionObject


class GitlabClient(VCSClientProtocol):
    """
    GitLabClient: Client for fetching data from GitLab
        connection_object (VCSConnectionObject): The object containing connection information for GitLab.
        base_api_endpoint (str): The base URL for the GitLab API.
        headers (dict): Headers including the Authorization Bearer token for authentication.
    """

    def __init__(self, vcs_connection_object: VCSConnectionObject):
        self.connection_object = vcs_connection_object
        self.base_api_endpoint = vcs_connection_object.url
        self.headers = {"Authorization": f"Bearer {vcs_connection_object.token}"}
