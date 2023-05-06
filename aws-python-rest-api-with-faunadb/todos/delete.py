from todos import client, TODOS

from faunadb.objects import Ref
from faunadb import query

def delete(event, context):
    # delete the todo from the database
    client.query(query.delete(Ref(TODOS, event['pathParameters']['id'])))

    return {"statusCode": 200}
