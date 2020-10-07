from django.db import models

# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy import CheckConstraint, Column, DateTime, Float, ForeignKey, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT, TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from django.contrib.auth.hashers import make_password, check_password


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(INT, primary_key=true)
    name = Column(String(50))



    class Login(Base):
    __tablename__ = 'user_signup'

    reg_id = Column(INTEGER(11), primary_key=True)
   	customer_id = Column(String(225), comment='customer_id')
   	customer_name= Column(String(225), comment='customer_name ')
    customer_gender= Column(String(225), comment='customer_gender')
    customer_phone = Column(INTEGER(10), comment='customer_phone')
    customer_username = Column(String(45), comment='customer_username')
    customer_password = Column(String(45), comment='customer_password')
    customer_type = Column(String(45), comment='customer_type')
    customer_status = Column(String(45), comment='customer_status')

    def check_password(self, raw_password):
        return check_password(raw_password, self.customer_password)

        


