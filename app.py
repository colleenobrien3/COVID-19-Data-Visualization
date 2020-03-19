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
    cases_reported = IntegerField()


db.connect()
db.drop_tables([State])
db.create_tables([State])
State(name='Delaware', cases_reported=28).save()
State(name='Maryland', cases_reported=29).save()
State(name='DC', cases_reported=34).save()
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
