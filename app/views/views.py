from flask import Flask, Blueprint, render_template

api_bp = Blueprint('api', __name__, template_folder='templates')

@api_bp.route('/')
def index():
    return render_template('index.html')

