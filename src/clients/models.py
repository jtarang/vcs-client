from dataclasses import dataclass
from src.enums import VCSNames


@dataclass
class VCSConnectionObject:
    """ VCSConnectionObject: Contains all connetion info """
    type: VCSNames
    url: str
    token: str


