

class VCSClientNotSupportedException(Exception):
    """ VCSClientNotSupportedException is throw if not in VCSNames """
    def __init__(self, client_type_str=None):
        formatted_message = f"Error {client_type_str}: is not currently supported"
        super().__init__(formatted_message)
