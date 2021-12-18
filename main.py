from services.fileopener import buildObjectsMovies
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        return buildObjectsMovies("movies.csv")

class HelloWorld1(Resource):

    def get(self):
        return buildObjectsMovies("movies.csv")

class HelloWorld2(Resource):

    def get(self):
        return buildObjectsMovies("ratings.csv")

class HelloWorld3(Resource):

    def get(self):
        return buildObjectsMovies("tags.csv")

class HelloWorld4(Resource):

    def get(self):
        return buildObjectsMovies("links.csv")

api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorld1, '/movies')
api.add_resource(HelloWorld2, '/ratings')
api.add_resource(HelloWorld3, '/tags')
api.add_resource(HelloWorld4, '/links')




if __name__ == '__main__':
    app.run(debug=True)



