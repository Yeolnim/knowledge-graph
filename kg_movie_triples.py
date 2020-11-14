#!/usr/bin/env python
#encoding=utf-8

import  random
import  sys 


film_name = "<http://kg.course/movie/film_%05d>  <http://kg.course/movie/film_name>  \"film_name_%05d\" ."

film_company = "<http://kg.course/movie/film_%05d>  <http://kg.course/movie/film_company>  <http://kg.course/movie/company_%04d> ."
company_name  = " <http://kg.course/movie/company_%04d>  <http://kg.course/movie/company_name>  \"company_name_%04d\" ."

film_director = "<http://kg.course/movie/film_%05d>  <http://kg.course/movie/film_director>  <http://kg.course/movie/director_%03d> ."
director_name = "<http://kg.course/movie/director_%03d>  <http://kg.course/movie/director_name>  \"director_name_%03d\" ."

tag_name = "<http://kg.course/movie/film_%05d>  <http://kg.course/movie/film_tag>  \"tag_name_%02d\" ."

total_sum = 1000
triples_sum  = 0
triples = []

if (len(sys.argv) >= 2):
    try:
        total_sum = int(sys.argv[1])
    except:
        total_sum = 1000


for i  in range(1,total_sum):
    film_str = film_name % (i,i)

    s = random.randint(1,10)

    company_str = film_company % (i,i/s + 1 )
    company_name_str = company_name % (i/10 + 1,i/10 + 1)

    t = random.randint(1,100)
    film_director_str = film_director % (i ,i % t )

    director_name_str = director_name % (i % t , i % t)


    k = random.randint(1,10)
    tag_name_str = tag_name % ( i , i % k + 1 )


    triples.append(film_str)
    triples_sum += 1
    if(total_sum <= triples_sum):
        break

    triples.append(company_str)
    triples_sum += 1
    if (total_sum <= triples_sum):
        break

    triples.append(company_name_str)
    triples_sum += 1
    if (total_sum <= triples_sum):
        break

    triples.append(film_director_str)
    triples_sum += 1
    if (total_sum <= triples_sum):
        break

    """
    triples.append(director_name_str)
    triples_sum += 1
    if (total_sum <= triples_sum):
        break
    """

    triples.append(tag_name_str)
    triples_sum += 1
    if (total_sum <= triples_sum):
        break

filename = ("movie_%d_triples.nt") % (total_sum)
with open(filename,"w+") as fd:
    fd.write("\n".join(triples))
