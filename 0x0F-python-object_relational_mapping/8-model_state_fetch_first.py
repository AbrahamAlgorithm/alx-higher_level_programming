#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).first()

    if (query is None):
        print('Nothing')
    else:
        print("{}: {}".format(query.id, query.name))
