""" Provides the NotFoundError class """
class NotFoundError(Exception):
    """
        NotFoundError is raised if the URL the api is accessing does not exist.
        This should probably never happen.
    """
    pass
