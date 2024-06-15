import uuid
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_clients():
    clients = {
        "client1": str(uuid.uuid4()),
        "client2": str(uuid.uuid4()),
        "client3": str(uuid.uuid4())
    }
    return clients

def get_user():
    users = {
        "user1": str(uuid.uuid4()),
        "user2": str(uuid.uuid4()),
        "user3": str(uuid.uuid4())
    }
    return users

def insert_user(body):
    name = body.get('Name')
    user_id = body.get('id')
    logger.info(f'Creando usuario: {name}, id: {user_id}')
    return {'name': name, 'id': user_id}

def insert_client(body):
    name = body.get('Name')
    client_id = body.get('id')
    logger.info(f'Creando cliente: {name}, id: {client_id}')
    return {'name': name, 'id': client_id}