#!/usr/bin/python3
"""
Model has a class state
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from model_state import Base, State

Base = declarative_base()


class State(Base):
    """
    print the state of object from the database depending on the name
    """
    __tablename__ = 'states'
    id = Column("id", Integer,
                autoincrement="auto",
                primary_key=True,
                unique=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    state_name = sys.argv[4]
    session = Session(engine)
    state = session.query(State).where(State.name == state_name).order_by(State.id).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
