from flask import Flask
from flask_restful import Api, Resource
from secrets import *

app = Flask(__name__)
api = Api(app)


class MeanTweetsApi(Resource):
    def get(self, handle):
        return {'handle': handle[::-1]}

api.add_resource(MeanTweetsApi, "/meantweet/<string:handle>")
#format: "/meantweet/<string:handle>/<int:num>/"

if __name__ == "__main__":
    app.run(debug=True, host=Evan_Mac_ip)
