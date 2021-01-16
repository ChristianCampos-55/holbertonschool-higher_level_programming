#!/usr/bin/python3
"""Class state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''State Class'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
