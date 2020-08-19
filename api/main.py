from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/api/test')
def get_test():
    return 'TEST PAGE: API RUNNING'

@app.route('/')
def home():
    return 'Meantweets Flask homepage'

class MeanTweetsApi(Resource):
    def get(self, handle):
        return {'handle': handle,
        'output': handle[::-1]}


api.add_resource(MeanTweetsApi, "/meantweet/<string:handle>")
#format: "/meantweet/<string:handle>/<int:num>/"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
