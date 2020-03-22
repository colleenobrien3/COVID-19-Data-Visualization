from peewee import *

db = PostgresqlDatabase('states', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

print(State.select())
