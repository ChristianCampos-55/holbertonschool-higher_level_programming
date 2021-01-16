#!/usr/bin/python3
"""Defines State Class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
        """Init of State Class"""
        __tablename__ = 'states'
        id = Column(Integer, ullable=False, primary_key=True, autoincrement=True)
        name = Column(String(128), nullable=False)
