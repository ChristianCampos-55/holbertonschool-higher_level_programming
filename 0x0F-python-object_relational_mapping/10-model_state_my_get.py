#!/usr/bin/python3
"""Lists States from a database"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    ngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=ngine)
    sess = Sess()
    state = sess.query(State).filter(State.name == argv[4]).first()
    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')
    sess.close()
