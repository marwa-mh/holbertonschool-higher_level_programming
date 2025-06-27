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
    CREATE a new state
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

    session = Session(engine)
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
