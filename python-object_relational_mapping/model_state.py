#!/usr/bin/python3
"""
Defines the State class and creates the database schema.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """
    State class that maps to the "states" table in the database.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://username:password@localhost:3306/db_name',
        pool_pre_ping=True
    )

    # Create the table
    Base.metadata.create_all(engine)
