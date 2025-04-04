from utiles.postgres_driver import conn
from model.message_model import Message

def get_messages():
    
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM hello")  
        messages = cur.fetchall()

    response = []
    for msg in messages:
        message_instance = Message(id=msg[0], message=msg[1])
        response.append(message_instance.to_dict())

    return response