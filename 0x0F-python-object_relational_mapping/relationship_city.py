#!/usr/bin/python3
"""Lists states"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State

class City(Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
