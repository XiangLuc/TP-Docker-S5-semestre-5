from flask import Blueprint, jsonify
# from message_db import message_val
from service.message_service import get_messages

message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/', methods=['GET'])
def messages():
    messages = get_messages()
    return jsonify(messages), 200