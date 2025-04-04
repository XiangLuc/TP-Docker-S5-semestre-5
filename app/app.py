from flask import Flask
from flask_cors import CORS
from controller.message_controller import message_bp
import logging


app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(message_bp, url_prefix='/hello')


logging.basicConfig(filename='/logs/app.log', level=logging.DEBUG)


@app.route('/')
def hello_world():
    return 'Hello Worlds !'


if __name__ == "__main__":
    app.run(debug=True)