from MySPARQLWrapper import MySPARQLWrapper

ms = MySPARQLWrapper()
update_string = """
PREFIX movie: <http://kg.course/movie/>

DELETE 
{  
  movie:director_02   movie:director_name ?x .
}
WHERE 
{ 
   movie:director_02  movie:director_name ?x .
}

"""
ms.update(update_string)
