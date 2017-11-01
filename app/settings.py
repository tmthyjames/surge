import os 

class Config(object):

    db_username = os.environ['SURGE_DB_USERNAME']
    db_conn_string = 'postgresql://'+db_username+':'+os.environ['SURGE_DB_PASSWORD']+'@localhost:5432/surge'
