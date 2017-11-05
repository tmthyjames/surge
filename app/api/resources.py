from flask import jsonify, request
from flask_restful import Resource
from math_.math_problems import MathProblem, CheckMathProblem
from math_.word_problems import WordProblem
from problems.models import Problem, db
import time

class Generate(Resource):

    def get(self, grade=None, operation=None):
        operators = {
            'addition': " + ",
            'subtraction': " - "
        }
        problem = getattr(MathProblem, operation)(grade)
        return jsonify({
            'grade': grade,
            'operation': operation,
            'problem': problem,
            'text': str(problem['terms'][0]) + operators[operation] + str(problem['terms'][1]) + " = "
        })

class GenerateWordProblem(Resource):

    def get(self, grade=None, type_=None, operation=None):
        problem = getattr(WordProblem, type_)(operation)
        return jsonify({
            'grade': grade,
            'operation': operation,
            'problem': {
                'problem': problem.get('problem'),
                'answer': problem.get('answer'),
                'terms': problem.get('terms')
            },
            'text': problem.get('problem')
        })

class Check(Resource):

    def get(self, grade=None, operation=None, term1=None, term2=None, submitted_answer=None):
        check_work = getattr(CheckMathProblem, operation)(term1, term2, submitted_answer)
        answer = check_work.get('answer')
        correct = check_work.get('correct')
        problem = Problem(
            term1=term1, term2=term2, 
            answer=answer, submitted_answer=submitted_answer,
            grade=grade, operation=operation, 
            dateof=int(time.time())
        )
        db.session.add(problem)
        db.session.commit()
        return jsonify({
            'answer': int(answer),
            'correct': correct,
            'submitted_answer': int(submitted_answer)
        })

class CheckWordProblem(Resource):

    def get(self, grade=None, operation=None, 
            submitted_answer=None, type_=None, answer=None):
        text = request.args.get('problem')
        problem = Problem(
            answer=answer, submitted_answer=submitted_answer,
            grade=grade, operation=operation,
            dateof=int(time.time()), type=type_,
            textrep=text
        )
        db.session.add(problem)
        db.session.commit()
        return jsonify({
            'answer': int(answer),
            'correct': str(answer).strip() == str(submitted_answer).strip(),
            'submitted_answer': submitted_answer
        })


class Results(Resource):

    def get(self):
        columns = Problem.__table__.columns.keys()
        problems = Problem.query.all()
        results = [{c: getattr(p, c) for c in columns} for p in problems]
        return jsonify(results)
