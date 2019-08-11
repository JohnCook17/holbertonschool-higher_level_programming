#!/usr/bin/python3
"""Finds states with the letter a and deletes
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
    my_query = session.query(State).filter(State.name.like("%" + "a" + "%"))
    my_query.delete('fetch')
    session.commit()
    session.close()
