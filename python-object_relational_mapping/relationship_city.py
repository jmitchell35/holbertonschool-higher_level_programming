#!/usr/bin/python3
"""
Contains the class definition of a City with relationship to State
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base

    Attributes:
        id (int): Primary key for the city
        name (str): Name of the city
        state_id (int): Foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
