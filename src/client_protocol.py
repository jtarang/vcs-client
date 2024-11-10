from typing import Protocol

class VCSClientProtocol(Protocol):
    """
    VCSClientProtocol is the blueprint for all other clients to use

    All clients should include these methods below

    Note: There should not be return values for protocol methods, I have included them for demo purposes
    """

    def get_repos(self):
        """ Get Repos  """
        return 'Not implemented, message from protocol'

    def get_commits(self):
        """ Get Commits """
        return 'Not implemented, message from protocol'

    def get_users(self):
        """ Get Users """
        return 'Not implemented, message from protocol'