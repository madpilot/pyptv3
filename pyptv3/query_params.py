""" Provides the QueryParams Class """
def _append_query_list(query_list, key, values):
    if isinstance(values, list):
        for value in values:
            _append_query_list(query_list, key, value)

    elif isinstance(values, bool):
        if values is True:
            _append_query_list(query_list, key, "true")
        else:
            _append_query_list(query_list, key, "false")
    else:
        query_list.append((key, values))

class QueryParams: # pylint: disable=too-few-public-methods
    """
    Utilities for dealing with Query Parameters
    """

    def process_kwargs(**kwargs): # pylint: disable=no-method-argument
        """
        Converts the supplied **kwargs into a QueryParams list
        """
        query_list = []
        for key in kwargs:
            values = kwargs[key]
            _append_query_list(query_list, key, values)

        return query_list
