#!/usr/bin/python3
"""
Class state using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# Connecting to MySQL server at 23.92.23.113 using mysql-python DBAPI 
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "hbtn_0c_0"), pool_pre_ping=True)


class State(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, autoincrement="auto", primary_key=True, unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)

Base.metadata.create_all(engine)
                