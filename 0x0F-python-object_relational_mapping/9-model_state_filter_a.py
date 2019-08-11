#!/usr/bin/python3
"""Finds states with the letter a
"""
import MySQLdb
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    my_query = states.filter(State.name.like("%" + "a" + "%"))
    for state in my_query:
        print("{}: {}".format(state.id, state.name))
