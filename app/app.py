from flask import Flask
from flask_restful import Api

from api.resources import Generate, Check

from views.views import api_bp

app = Flask(__name__)
api = Api(app)

api.add_resource(Generate, '/api/generate/<grade>/<operation>/')
api.add_resource(Check, '/api/check/<operation>/<term1>/<term2>/<submitted_answer>/')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
