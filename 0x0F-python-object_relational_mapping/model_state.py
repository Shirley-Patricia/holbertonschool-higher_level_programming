"""file that contains the class definition of a State and an instance
   Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base = declarative_base()


class State (Base):
    """creating table states of class State inherit of Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


Session = sessionmaker(bind=engine)
session = Session()
