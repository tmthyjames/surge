import random
import operator

names = ['Mike', 'Tim', 'Horshel', 'Sandael', 'Dybee', 
         'Batman', 'Superman', 'Spiderman', 'Allyson',
         'Shawn', 'Kyle', 'Kelly', 'Keisha', 'Rhonda',
         'Bob', 'Mark', 'Emily', 'Bo', 'Emmit', 'Irving',
         'Dieon', 'Lebron', 'Steph', 'Kevin', 'Durant',
         'Demarcus', 'Karl', 'Anthony', 'Dennis', 'Blake', 'Penny']

things = ['markers', 'pencils', 'toys', 'flowers', 'bottles', 
          'books', 'dimes', 'quarters', 'nickles', 'cars']

operators = {
    'addition': operator.add,
    'subtraction': operator.sub
}

class WordProblem(object):

    @staticmethod
    def missing_term_problem(operation):
        person1 = random.choice(names)
        person2 = random.choice([name for name in names if name != person1])
        operation = operators.get(operation)
        term1 = random.randint(10, 70)
        term2 = random.randint(0, 9)
        thing = random.choice(things)
        problem = person1 + " has " + str(term1) + " " + thing + ". " + person1 + " has " + str(term2) + " more " + thing + " than " + person2 + ". "
        problem += "How many total " + thing + " are there?"
        answer = term1 + (term1 + term2)
        return {
            'text': problem,
            'problem': problem,
            'answer': answer,
            'terms': [term1, term2]
        }

    @staticmethod
    def simple_word(op):
        person1 = random.choice(names)
        person2 = random.choice([name for name in names if name != person1])
        operation = operators.get(op)
        term1 = random.randint(0, 49)
        term2 = random.randint(50, 99)
        thing = random.choice(things)
        operations = {
            'addition': "How many " + thing + " do they have in total?",
            'subtraction': "How many more " + thing + " does " + person2 + " have?"
        }
        problem = person1 + " has " + str(term1) + " " + thing + " and " + person2 + " has " + str(term2) + " " + thing + ". "
        problem += operations.get(op)
        answer = operation(term2, term1)
        return {
            'text': problem,
            'problem': problem,
            'answer': answer,
            'terms': [term1, term2]
        }
