import json
import csv
from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import dict_to_model, model_to_dict
db = PostgresqlDatabase('states', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class State(BaseModel):
    name = CharField()
    total_cases = CharField()
    new_cases = CharField()
    total_deaths = CharField()
    new_deaths = CharField()
    total_recovered = CharField()
    active_cases = CharField()


db.connect()
db.drop_tables([State])
db.create_tables([State])

# f = open('./dataFile.py', 'r')

# # print(f.read())


# with open('./dataFile.py') as lst:
#     print(str(lst[0]))


with open('data.txt') as json_file:
    data = json.load(json_file)
    print(data)

for i in data:
    State(name=i['name'], total_cases=i['total_cases'],
          new_cases=i['new_cases'], total_deaths=i['total_deaths'], new_deaths=i['new_deaths'], total_recovered=i['total_recovered'], active_cases=i['active_cases']).save()


# for row in f[0]:

#     State(name=row[0], total_cases=row[1],
#           new_cases=row[3], total_deaths=row[4], new_deaths=row[5], total_recovered=row[6], active_cases=row[7]).save()
#     print(row)


app = Flask(__name__)

# Create Person
@app.route('/state/', methods=['POST'])
def create_person():
    new_state = dict_to_model(State, request.get_json())
    new_state.save()
    return jsonify({"success": True})

# Get All
@app.route('/state/', methods=['GET'])
@app.route('/state/<id>', methods=['GET'])
def get_state(id=None):
    if id:
        return jsonify(
            model_to_dict(
                State.get(State.id == id)))
    else:
        states = []
        for state in State.select():
            states.append(model_to_dict(state))
        return jsonify(states)


@app.route('/endpoint', methods=['GET', 'PUT', 'POST', 'DELETE'])
def endpoint():
    if request.method == 'GET':
        return 'GET request'

    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        return 'POST request'

    if request.method == 'DELETE':
        return 'DELETE request'


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    goner = State.get(State.id == id)
    State.delete_instance(goner)
    return jsonify(model_to_dict(goner))


app.run(debug=True, port=9000)
