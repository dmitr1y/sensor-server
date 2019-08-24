from flask import Flask
from flask_restful import Api

from controllers.SensorController import SensorController

app = Flask(__name__)
api = Api(app)

api.add_resource(SensorController, '/sensor/<id>')

if __name__ == "__main__":
    app.run(port='8080')
