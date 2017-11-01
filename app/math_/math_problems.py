from random import randint

class MathProblem(object):

    @staticmethod
    def addition(grade):
        low_range = 10 if str(grade) == '2' else 50
        high_range = 99 if str(grade) == '2' else 500
        term1 = randint(low_range, high_range)
        term2 = randint(low_range, high_range)
        return {
            'terms': [term1, term2],
            'answer': term1 + term2
        }

    @staticmethod
    def subtraction(grade):
        low_range = 10 if str(grade) == '2' else 50
        high_range = 99 if str(grade) == '2' else 500
        term1 = randint(low_range, high_range)
        term2 = randint(low_range, high_range)
        term1 = max([term1, term2])
        term2 = min([term1, term2])
        return {
            'terms': [term1, term2],
            'answer': term1 - term2
        }

class CheckMathProblem(object):

    @staticmethod
    def addition(term1, term2, submitted_answer):
        answer = (int(term1) + int(term2))
        return {
            'correct': answer == int(submitted_answer),
            'answer': answer
        }

    @staticmethod
    def subtraction(term1, term2, submitted_answer):
        answer = (int(term1) - int(term2))
        return {
            'correct': answer == int(submitted_answer),
            'answer': answer
        }
