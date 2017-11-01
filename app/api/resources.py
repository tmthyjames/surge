from flask import jsonify
from flask_restful import Resource
from math_.math_problems import MathProblem, CheckMathProblem

class Surge(Resource):

    def get(self, grade=None, operation=None):
        return jsonify({
            'grade': grade,
            'operation': operation,
            'problem': getattr(MathProblem, operation)(grade)
        })

class Check(Resource):

    def get(self, operation=None, term1=None, term2=None, submitted_answer=None):
        check_work = getattr(CheckMathProblem, operation)(term1, term2, submitted_answer)
        answer = check_work.get('answer')
        correct = check_work.get('correct')
        return jsonify({
            'answer': int(answer),
            'correct': correct,
            'submitted_answer': int(submitted_answer)
        })

