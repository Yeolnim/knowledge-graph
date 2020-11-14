from SPARQLWrapper import SPARQLWrapper, JSON
class MySPARQLWrapper:

    def query(self, query_string=None):
        sparql = SPARQLWrapper("http://localhost:3030/movie/sparql")
        sparql.setQuery(query_string)
        sparql.setReturnFormat(JSON)
        results = None
        try:
            results = sparql.query().convert()
        except:
            return False
        return results

    def update(self, update_string=None):
        sparql_update = SPARQLWrapper(endpoint="http://localhost:3030/movie/update")
        sparql_update.setQuery(update_string)
        sparql_update.method = "POST"
        sparql_update.setReturnFormat(JSON)
        results = None
        try:
            results = sparql_update.query()
        except:
            return False
        return True