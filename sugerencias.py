print("=====================================\n")
print("      SUGERENCIAS DE PELÌCULAS       \n")
print("=====================================\n")
usuario=input("Buen dìa, cùal es tu nombre? ")
print("¿Què querès ver hoy, "+usuario+"?")
nombre_pelicula="Ràpidos y furiosos"
genero_pelicula="Accion"
anio_pelicula=2001
rating_pelicula=6.8
nombre_pelicula2="Troya"
genero_pelicula2="Accion"
anio_pelicula2=2004
rating_pelicula2=7.3
nombre_pelicula3="Terminator 2"
genero_pelicula3="Accion"
anio_pelicula3=1991
rating_pelicula3=8.6
nombre_pelicula4="¿Y dónde está el piloto?"
genero_pelicula4="Comedia"
anio_pelicula4=1980
rating_pelicula4=7.7
nombre_pelicula5="¿Què pasò ayer?"
genero_pelicula5="Comedia"
anio_pelicula5=2009
rating_pelicula5=7.7
nombre_pelicula6="¿Y dònde estàn las rubias?"
genero_pelicula6="Comedia"
anio_pelicula6=2004
rating_pelicula6=5.8
nombre_pelicula7= "Coco"
genero_pelicula7="Animacion"
anio_pelicula7=2017
rating_pelicula7=8.4
nombre_pelicula8="Shrek"
genero_pelicula8="Animacion"
anio_pelicula8=2001
rating_pelicula8=7.9
print("-------- GÈNEROS --------")
print("Acción")
print("Comedia")
print("Animación")
genero_favorito=input("¿Qué género te gusta? ")
rating_favorito=float(input("¿Cual es el rating minimo? "))
print ("Buscando Péliculas del Género "+genero_favorito)
encontrar=False
if (genero_pelicula==genero_favorito) and (rating_favorito<rating_pelicula):
	print(nombre_pelicula)
	encontrar=True	
if (genero_pelicula2==genero_favorito) and (rating_favorito<rating_pelicula2):
	print(nombre_pelicula2)
	encontrar=True
if (genero_pelicula3==genero_favorito) and (rating_favorito<rating_pelicula3):
	print(nombre_pelicula3)
	encontrar=True
if (genero_pelicula4==genero_favorito) and (rating_favorito<rating_pelicula4):
	print(nombre_pelicula4)
	encontrar=True
if (genero_pelicula5==genero_favorito) and (rating_favorito<rating_pelicula5):
	print(nombre_pelicula5)				
	encontrar=True
if (genero_pelicula6==genero_favorito) and (rating_favorito<rating_pelicula6):
	print(nombre_pelicula6)
	encontrar=True
if (genero_pelicula7==genero_favorito) and (rating_favorito<rating_pelicula7):
	print(nombre_pelicula7)
	encontrar=True
if (genero_pelicula8==genero_favorito) and (rating_favorito<rating_pelicula8):
	print(nombre_pelicula8)			
	encontrar=True
if (encontrar==False):
	print("No hay peliculas disponibles")