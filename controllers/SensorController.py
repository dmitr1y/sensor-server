from flask_jsonpify import jsonify
from flask_restful import Resource

from sensors.dht.DhtSensor import DhtSensor
from sensors.dht.DhtType import DhtType


class SensorController(Resource):
    def get(self, id):
        sensor = DhtSensor(pin=4, type=DhtType.DHT11.value)

        return jsonify(sensor.get_temp())
