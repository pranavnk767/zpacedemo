from django.db import models

# coding: utf-8
from sqlalchemy import CheckConstraint, Column, DateTime, Float, ForeignKey, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT, TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer)
    name = Column(String(50))


