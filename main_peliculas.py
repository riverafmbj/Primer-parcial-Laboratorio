from funciones_peliculas import *

"""
Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato: id_peli, titulo, genero, rating por ejemplo: 1,Adventures of Rocky,sin genero,0 2,My Brother the Devil,sin genero,0 3,Criminal,sin genero,0 Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar nuevos archivos de salida de formato similar filtrados por varios criterios: el programa contará con el siguiente menú: 
1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios los elementos del mismo. 
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas. 
3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal calculado de manera aleatoria se mostrará por pantalla el mismo. 
4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4. 1: drama 2: comedia 3: acción 4: terror 
5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero donde solo aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv 
6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por género y dentro de las del mismo género que aparezcan ordenadas por rating descendente. 
7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating 
8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON. 
9) Salir. 
"""

while True:
  match menu():
    case "1":
      lista_peliculas = cargar_archivo_csv("movies.csv")
      
    case "2":
      mostrar_peliculas(cargar_archivo_csv("movies.csv"))

    case "3":
      lista_peliculas = cargar_archivo_csv("movies.csv")
      lista_ratings = mapear_titulos_rating(lista_peliculas)
      for pelicula in lista_peliculas:
        titulo = pelicula["titulo"]
        rating = pelicula["rating"]
        print(f"Película: {titulo} - Rating: {rating}")

    case "4":
      lista_peliculas = cargar_archivo_csv("movies.csv")
      lista_generos = mapear_generos(lista_peliculas)
      for pelicula in lista_peliculas:
        titulo = pelicula["titulo"]
        genero = pelicula["genero"]
        print(f"Película: {titulo} - Género: {genero}")

    case "5":
      pass

    case "6":
      lista_peliculas = cargar_archivo_csv("movies.csv")
      lista_generos = mapear_generos(lista_peliculas)
      lista_ratings = mapear_titulos_rating(lista_peliculas)
      ordenar_clave_criterio(lista_peliculas, "genero", "rating")
      mostrar_peliculas(lista_peliculas)

    case "7":
      lista_peliculas = cargar_archivo_csv("movies.csv")
      lista_ratings = mapear_titulos_rating(lista_peliculas)
      lista_generos = mapear_generos(lista_peliculas)

      rating_max = 0
      flag_rating = False
      lista_mejores_ratings = []

      for pelicula in lista_peliculas:
        rating = pelicula["rating"]
        if flag_rating == False or rating > rating_max:
          rating_max = rating
          flag_rating = True

      if flag_rating == True:
        for pelicula in lista_peliculas:
          rating = pelicula["rating"]
          titulo = pelicula["titulo"]
          if rating == rating_max:
            lista_mejores_ratings.append(pelicula)
      
      mostrar_peliculas(lista_mejores_ratings)

    case "8":
      pass

    case "9":
      break
 
        