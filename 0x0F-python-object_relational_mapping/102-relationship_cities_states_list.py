#!/usr/bin/python3
"""Lists States and Cities from DB"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    ngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=ngine)
    sess = Sess()
    new_state = State(name='California')
    to_get = session.query(City).order_by(City.id).all()
    for i in to_get:
        print('{}: {} -> {}'.format(i.id, i.name, i.state.name))
    sess.close()