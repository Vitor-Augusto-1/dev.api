from flask_restful import Resource
lista_habilidades = ['Python', 'Java', 'PHP', 'HTML']
class habilidades(Resource):
    def get(self):
        return lista_habilidades
