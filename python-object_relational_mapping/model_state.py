#!/usr/bin/python3
"""
Class state using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


"""
Class state using SQLAlchemy
"""


class State(Base):
    """
    Class state using SQLAlchemy
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
