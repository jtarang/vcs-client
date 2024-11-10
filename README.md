# VCS Client

This project demonstrates how to interact with different Version Control Systems (VCS), such as GitHub and GitLab, using a unified `VCSClient` interface. The client abstracts the connection to each VCS and provides methods for fetching repositories and other data.

## Example Code

Below is a sample usage of the `VCSClient` to connect to both GitHub and GitLab and retrieve repository lists.

```python
from src.client import VCSClient
from src.enums import VCSNames
from src.models import VCSConnectionObject

if __name__ == "__main__":
    VCS_CLIENT = VCSClient()
    
    GITHUB_CONNECTION_OBJECT = VCSConnectionObject(
        url='https://api.github.com',
        token='your_github_token'
    )
    GITLAB_CONNECTION_OBJECT = VCSConnectionObject(
        url='https://gitlab.com/api/v4',
        token='your_gitlab_token'
    )
    
    GITHUB_CLIENT = VCS_CLIENT.get_client(client_type=VCSNames.GITHUB, vcs_connection_object=GITHUB_CONNECTION_OBJECT)
    GITLAB_CLIENT = VCS_CLIENT.get_client(client_type=VCSNames.GITLAB, vcs_connection_object=GITLAB_CONNECTION_OBJECT)
    
    GITHUB_REPOS = GITHUB_CLIENT.get_repos()
    GITLAB_REPOS = GITLAB_CLIENT.get_repos()
    
    print(f"GitHub Repositories: {GITHUB_REPOS}\nGitLab Repositories: {GITLAB_REPOS}")
