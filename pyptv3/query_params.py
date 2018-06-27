class QueryParams:
    def _append_query_list(query_list, key, values):
        if isinstance(values, list):
                for value in values:
                    QueryParams._append_query_list(query_list, key, value)
        elif isinstance(values, bool):
            if values == True:
                QueryParams._append_query_list(query_list, key, "true")
            else:
                QueryParams._append_query_list(query_list, key, "false")
        else:
            query_list.append((key, values))

    def process_kwargs(**kwargs):
        query_list = []
        for key in kwargs.keys():
            values = kwargs[key]
            QueryParams._append_query_list(query_list, key, values)

        return query_list
