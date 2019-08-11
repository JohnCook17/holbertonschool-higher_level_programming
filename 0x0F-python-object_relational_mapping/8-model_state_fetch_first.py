#!/usr/bin/python3
"""Print the first state
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
    data = session.query(State.id, State.name).first()
    res = []
    for row in data:
        res.append(str(row))
    res = ": ".join(res)
    print (res)
