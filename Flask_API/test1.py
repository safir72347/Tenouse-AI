from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Data = []

class People(Resource):
    def __init__(self):
        pass
    
    def get(self, name):
        for x in Data:
            if x['Data'] == name:
                return x
        return {'Data':None}

    def post(self):
        data = request.get_json()
        return jsonify(data)

    def delete(self, name):
        for ind, x in enumerate(Data):
            if x['Data'] == name:
                Tem = Data.pop(ind)
                return {'Note':"Deleted"}

api.add_resource(People, '/Name')

if __name__=='__main__':
    app.run(debug=True, port=8000)