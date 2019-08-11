#!/usr/bin/python3

import MySQLdb
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    my_query = session.query(State,
                             City).filter(City.state_id == State.id).all()
    for state, city in my_query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
