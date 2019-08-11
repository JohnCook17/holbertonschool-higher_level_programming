#!/usr/bin/python3
"""Replaces state id #2 with New Mexico
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
    state_query = session.query(State)
    my_query = state_query.filter(State.id == "2").first()
    my_query.name = "New Mexico"
    session.commit()
    session.close()
