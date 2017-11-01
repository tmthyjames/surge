from flask import Flask, Blueprint, render_template

api_bp = Blueprint('api', __name__, template_folder='templates')

@api_bp.route('/')
def index():
    return render_template('layout.html')

@api_bp.route('/<grade>/<operation>')
def addition(grade=None, operation=None):
    return render_template(
        'grade/{grade}/{operation}.html'.format(
            grade=grade, operation=operation
        ), operation=operation, grade=grade)

@api_bp.route('/<grade>/<operation>')
def subtraction(grade=None, operation=None):
    return render_template(
        'grade/{grade}/{operation}.html'.format(
            grade=grade, operation=operation
        ), operation=operation, grade=grade)

@api_bp.route('/results/')
def results():
    return render_template('results.html')
