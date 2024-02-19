#!/usr/bin/python3
"""Write a python file that contains the class definition of a State"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
import sys


class City(Base):
    """__table__name : the table name.
    id: primary key
    name: a string with nullable false
    state_id: foreign key"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
