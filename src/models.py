from dataclasses import dataclass

@dataclass
class VCSConnectionObject:
    """ VCSConnectionObject: Contains all connetion info """
    url: str
    token: str


