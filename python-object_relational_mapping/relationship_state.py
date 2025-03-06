#!/usr/bin/python3
"""
Contains the class definition of a State with relationship to City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base

    Attributes:
        id (int): Primary key for the state
        name (str): Name of the state
        cities (relationship): Relationship with City class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan")
