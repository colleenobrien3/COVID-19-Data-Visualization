from peewee import *

db = PostgresqlDatabase('states', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

print(State.select())

with
user_plays as (
    select
    user_id, count(1) as num_plays
    from
    gameplays
    group by
    1
)
