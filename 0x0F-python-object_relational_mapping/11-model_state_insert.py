#!/usr/bin/python3
"""Adds Louisiana to states
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
    new_data = State(name="Louisiana")
    session.add(new_data)
    session.commit()
    lou = session.query(State)
    my_query = lou.filter(State.name == "Louisiana")
    for state in my_query:
        res = state.id
    print(res)
    session.close()
