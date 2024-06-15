from utils import get_clients, get_user, insert_client, insert_user

def manage_get_request(path):
    if path == "/clients":
        return get_clients()
    elif path == "/users":
        return get_user()
    else:
        return None

def manage_post_request(path, body):
    if path == "/clients":
        return insert_client(body)
    elif path == "/users":
        return insert_user(body)
    else:
        return None