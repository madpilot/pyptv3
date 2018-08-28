""" Provides the Patterns Class """
import pyptv3

class Patterns: # pylint: disable=too-many-function-args,too-few-public-methods
    """
        View the stopping pattern for a specific trip/service run

        Args:
            run_id (int) Identifier of a trip/service run; values returned by pyptvv3.Run.all()
    """
    def __init__(self, client, run_id, route_type):
        self._client = client
        self._run_id = run_id
        self._route_type = route_type

    def all(self, **kwargs):
        """
            The stopping pattern of the specified trip/service run and route type.
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        path = "/pattern/run/" + str(self._run_id) + "/route_type/" + str(self._route_type)
        response = self._client.get(path)
        return pyptv3.PatternsResponse(response, query_list)
