import csv

from classes.movie import Movie

def buildObjectsMovies(filename) -> str :
    file = open(filename, encoding="utf8")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    listaFilmow = []
    spamreader = csv.reader(file, delimiter=',')
    for row in spamreader:
        print(','.join(row))
        film = Movie(int(row[0]), row[1], row[2])
        listaFilmow.append(film.__dict__)
    return listaFilmow

