#!/usr/bin/python3
"""
Module contain a class city
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Class city using SQLAlchemy
    """
    __tablename__ = 'cities'
    id = Column("id", Integer,
                autoincrement="auto",
                primary_key=True,
                unique=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column(
        "state_id",
        Integer,
        ForeignKey(State.id), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
