from django.shortcuts import render
import jwt,json
import os
from dateutil.relativedelta import relativedelta
from datetime import datetime 
from datetime import datetime , date
from sqlalchemy import inspect, asc, desc, text, func, extract, and_
from sqlalchemy.orm import load_only
from sqlalchemy.exc import SQLAlchemyError
from rest_framework.response import Response
from rest_framework.views import APIView
from mysite import dbsession
from decimal import Decimal
from mysite.SqlAlcchemyencoder import AlchemyEncoder
import string,random
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes, renderer_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate, get_user, login
import pandas as pd
from catalog.models import User

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny, ])
def get_reviews(request):
    try:
        session = dbsession.Session()
        columns = ['id','name']
        docsql = text('SELECT * from  user')
        reviewList = session.execute(docsql).fetchall()
        review_list = [dict(row) for row in reviewList]
        review_list = json.dumps(review_list, cls=AlchemyEncoder)
        review_list = pd.read_json(review_list)
        if columns:
            review_list.columns = columns
        review_list = review_list.to_json(orient='records')
        session.close()
        return Response({'response': 'Success', 'reviews_list': json.loads(review_list)})
    except SQLAlchemyError as e:
        session.rollback()
        session.close()
        return Response({'response': 'Error occured'})





