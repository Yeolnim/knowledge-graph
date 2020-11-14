from MySPARQLWrapper import MySPARQLWrapper
ms = MySPARQLWrapper()
query_string = """
PREFIX movie: <http://kg.course/movie/>

SELECT  ?directorID  ?director_name
WHERE {
  ?directorID  movie:director_name ?director_name 
}
"""
results = ms.query(query_string)
for result in results["results"]["bindings"]:
    print(result)
