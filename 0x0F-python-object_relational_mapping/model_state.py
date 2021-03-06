#!/usr/bin/python3

"""file that contains the class definition of a State and an instance
   Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State (Base):
    """creating table states of class State inherit of Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
