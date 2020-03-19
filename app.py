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
    date = CharField()
    name = CharField()
    new_cases = CharField()
    new_deaths = CharField()
    total_cases = CharField()
    total_deaths = CharField()


db.connect()
db.drop_tables([State])
db.create_tables([State])


data = 'full_data.csv'

with open('full_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        obj = (row[0].split(','))
        new_cases = ''
        new_deaths = ''
        total_cases = ''
        total_deaths = ''
        if len(obj) > 2:
            new_cases = obj[2]
        if len(obj) > 3:
            new_deaths = obj[3]
        if len(obj) > 4:
            total_cases = obj[4]
        if len(obj) > 5:
            total_deaths = obj[5]
        State(date=obj[0], name=obj[1], new_cases=new_cases,
              new_deaths=new_deaths, total_cases=total_cases, total_deaths=total_deaths).save()

# State(name='Delaware', cases_reported=28).save()
# State(name='Maryland', cases_reported=29).save()
# State(name='DC', cases_reported=34).save()
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
