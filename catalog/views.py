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
        columns = ['reg_id','customer_id','customer_name','customer_gender','customer_phone','customer_username','customer_password','customer_type','customer_status']
        docsql = text('SELECT * FROM demodb.user_signup')
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


        # /////////LOGIN

        @api_view(['GET','POST'])
        @permission_classes([AllowAny, ])
        def authenticate_user(request):
            try:
                session = dbsession.Session()

                username = request.GET.get('customer_username')
                password =request.GET.get('customer_password')
                print(username)
                print(password)

                columns = ['reg_id','customer_id','customer_name','customer_gender','customer_phone','customer_username','customer_password','customer_type','customer_status']
                docsql = text("SELECT * FROM demodb.user_signup where customer_username='+username+' AND customer_password='+password+'")
                reviewList = session.execute(docsql).fetchall()
                review_list = [dict(row) for row in reviewList]
                review_list = json.dumps(review_list, cls=AlchemyEncoder)
                review_list = pd.read_json(review_list)
                if columns:
                    review_list.columns = columns
                    review_list = review_list.to_json(orient='records')
                    session.close()
                    return Response({'response': 'Success', 'reviews_list': json.loads(review_list)},'customer_username':customer_username)
                except SQLAlchemyError as e:
                    session.rollback()
                    session.close()
                    return Response({'response': 'Error occured'})


    #     user = session.query(Login).filter(or_(Login.customer_username == customer_username, Login.customer_password==customer_password)).one()
    #     # user_id = user.id
    #     if user.check_password(customer_password):
    #         user.Status = 'active'
    #         session.commit()
    #         columns =['reg_id','customer_id','customer_name','customer_gender','customer_phone','customer_username','customer_password','customer_type','customer_status']
    #         user_list = session.query(Login.customer_username,Login.customer_password).filter(or_(Login.customer_username,Login.customer_password)).all()
    #         print(user_list)
    #         user_list = json.dumps(user_list, cls=AlchemyEncoder)
    #         user_list = pd.read_json(user_list)
    #         print(user_list.columns)
    #         if columns:
    #             user_list.columns = columns
    #             user_list = user_list.to_json(orient='records')
    #             return Response({'response': 'success','data':json.loads(user_list)})

    #     else:
    #         return Response({'response': 'Error','message':'Please provide a valid credentails'})

    #     return Response({'response': 'success'})
    # except SQLAlchemyError as e:
    #     print(e)
    #     session.rollback()
    #     session.close()
    #     return Response({'response': 'Error occured'})



 # //////////Signup
@api_view(['GET','POST'])
@permission_classes([AllowAny, ])
def saveRegister(request):
    try:
        session = dbsession.Session()

        idd = request.data['customer_id']
        name=request.data['Name']
        gender= request.data['gender']
        phone = request.data['phone']
        username =request.data['username']
        password = request.data['password']
        types = request.data['type']
        status = request.data['status']
        
        
        email_check = session.query(Login).filter(Login.customer_username==username).all()
        if(len(email_check) > 0):
            return Response({'status': 'email Id exists','message':'email Id already exists'})
        phno_check = session.query(Login).filter(Login.customer_phone==phone).all()
        if(len(phno_check) > 0):
            return Response({'status': 'phone num exists','message':'phone num already exists'})

        user_signup = Login()

        user_signup.customer_id = idd
        user_signup.customer_name= name
        user_signup.customer_gender= gender
        user_signup.customer_phone = phone
        user_signup.customer_username = username
        user_signup.customer_password = password
        user_signup.customer_type = types
        user_signup.customer_status = status
        
        session.add(user_signup)
        session.commit()
        session.close()
        return Response({'response': 'Data saved success fully'})
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
        session.close()
        return Response({'response': 'Error occured'})

        # //////////Adv

        @api_view(['GET','POST'])
        @permission_classes([AllowAny, ])
        def get_adv(request):
            try:
                session = dbsession.Session()
                columns = ['adv_id','adv_name','adv_imageurl','adv_status']
                docsql = text('SELECT * FROM demodb.first_advertisement')
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


                    # /////////categoryview
                     # //////////Adv

        @api_view(['GET','POST'])
        @permission_classes([AllowAny, ])
        def get_category(request):
            try:
                session = dbsession.Session()
                columns = ['cat_id','cat_name','cat_imageurl','cat_status']
                docsql = text('SELECT * FROM demodb.product_categoery;')
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


                    # /////////////////home


        @api_view(['GET','POST'])
        @permission_classes([AllowAny, ])
        def get_home(request):
            try:
                session = dbsession.Session()
                columns = ['home_id','home_heading','home_tablename','home_subcategoryname','home_categoryname','home_suburl','home_offer','home_background','home_cardnumber']
                docsql = text('SELECT * FROM demodb.User_home')
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



`home_heading`,
`home_tablename`,
`home_categoryname`,
`home_subcategoryname`,
`home_suburl`,
`home_offer`,
`home_background`,
`home_cardnumber`)
