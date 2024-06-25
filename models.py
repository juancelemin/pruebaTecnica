from typing import Union, Dict, Any, List, Optional
from sqlalchemy import Column, Integer, String, Boolean, TypeDecorator, Text

import json

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base





Base = declarative_base()



class Parameter(Base):
    __tablename__ = 'parameters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500))
    type = Column(String(500), nullable=True)
    value = Column(String(500), nullable=True) 