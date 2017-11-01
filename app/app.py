from flask import Flask
from flask_restful import Api

from api.resources import Generate, Check, Results
from views.views import api_bp
from problems.models import db
from settings import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.db_conn_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)

api.add_resource(Generate, '/api/generate/<grade>/<operation>/')
api.add_resource(Check, '/api/check/<grade>/<operation>/<term1>/<term2>/<submitted_answer>/')
api.add_resource(Results, '/api/results/')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
