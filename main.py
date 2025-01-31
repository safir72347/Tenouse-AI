from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from fastai.basic_train import load_learner
from fastai.vision import *
from flask_cors import CORS,cross_origin
import os
import sys

# import torch
# from torch import nn
# from torchvision import datasets, transforms, models
# import torchvision.models as models
# import torch.nn.functional as F
# import torchvision.transforms.functional as F
# from torch import optim
import json

from PIL import *
from PIL import Image
import requests
from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import math

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# For Cosine Similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import joblib

import pickle

import cv2

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

class AI(Resource):
    def __init__(self):
        pass
    def get(self):
        return {"message":"Welcome to TenRox-AI"}

class classify_house_structure(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            img_url = data['image']

            # Opening image from url
            response = requests.get(img_url)
            img_file = open_image(BytesIO(response.content))
            # img_file = Image.open(BytesIO(response.content))

            print("Image file : ", img_file)

            path = os.getcwd()
            path = path + "/Classification/house_structure/"
            learn = load_learner(path=path, file='house_structure_classify_model.pkl')
            # learn = pickle.load(open(path+'house_structure_classify_model.pkl', 'rb'))
            classes = learn.data.classes

            # Predicting the image
            prediction = learn.predict(img_file)
            probs_list = prediction[2].numpy()
            print(classes[prediction[1].item()])

            # Returning the response
            return jsonify({
                'category': classes[prediction[1].item()],
                'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
            })
        except Exception as e:
            print(e)
            return jsonify({
                'error':"Some Error occurred"
            })

class classify_house_type(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            img_url = data['image']

            # Opening image from url
            response = requests.get(img_url)
            img_file = open_image(BytesIO(response.content))
            
            path = os.getcwd()
            path = path + "/Classification/house_type/"
            learn = load_learner(path=path, file='furnished_unfurnished_classify_model.pkl')
            # learn = joblib.load(path+'furnished_unfurnished_classify_model.pkl')
            classes = learn.data.classes

            # Predicting the image
            prediction = learn.predict(img_file)
            probs_list = prediction[2].numpy()
            print(classes[prediction[1].item()])

            # Returning the response
            return jsonify({
                'category': classes[prediction[1].item()],
                'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
            })
            
        except Exception as e:
            print(e)
            return jsonify({
                'error':"Some Error occurred"
            })

class classify_tenouse_premium(Resource):
    def __init__(self):
        pass
    
    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            main_data_list = data['main_data']

            # Loading the Classification Model
            path = os.getcwd()
            path = path + "/DataAnalysis/"
            clf = joblib.load(path+'PremiumModel.pkl')

            # Predicting the result
            # [3, 1, 4] => 0, [1, 1, 4] => 1
            y_pred = clf.predict([main_data_list])

            print(y_pred)
            # Returning the response
            return jsonify({
                'predictedValue': str(list(y_pred)[0])
            })
        except Exception as e:
            print(e)
            return jsonify({
                'error':"Some Error occurred"
            })

class regress_tenouse_profit(Resource):
    def __init__(self):
        pass
    
    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            main_data_list = data['main_data']

            # Loading the Classification Model
            path = os.getcwd()
            path = path + "/DataAnalysis/"
            reg = joblib.load(path+'TenouseProfitModel.pkl')

            # Since StandardScalar uses the attributes from previously fit_transformed data, we need to fir_transform once more to get the output
            dataset = pd.read_csv(path+'TenouseProfit_file.csv')
            city = {'Pune':1, 'Mumbai':2, 'Bangalore':3, 'Hyderabad':4}
            dataset['City'] = dataset['City'].map(city)

            X = dataset.iloc[:, 0:-1].values
            y = dataset.iloc[:, -1].values
            y = y.reshape(len(y),1)

            sc_X = StandardScaler()
            sc_y = StandardScaler()
            X = sc_X.fit_transform(X)
            y = sc_y.fit_transform(y)

            # Predicting the result
            y_pred = sc_y.inverse_transform(reg.predict(sc_X.transform([main_data_list])))

            print(y_pred)
            # Returning the response
            return jsonify({
                'predictedValue': str(list(y_pred)[0])
            })
        except Exception as e:
            print(e)
            return jsonify({
                'error':"Some Error occurred"
            })

class regress_house_price(Resource):
    def __init__(self):
        pass
    
    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            main_data_list = data['main_data']

            # Loading the Classification Model
            path = os.getcwd()
            path = path + "/DataAnalysis/"
            reg = joblib.load(path+'HousePriceModel.pkl')

            # Since StandardScalar uses the attributes from previously fit_transformed data, we need to fir_transform once more to get the output
            dataset = pd.read_csv(path+'HousePrice_file.csv')
            city = {'Pune':1, 'Mumbai':2, 'Bangalore':3, 'Hyderabad':4}
            house_struct = {'Bungalow':1, 'Building':2, 'Row_House':3}
            house_type = {'Furnished':1, 'Unfurnished':2}
            dataset['City'] = dataset['City'].map(city)
            dataset['House Structure'] = dataset['House Structure'].map(house_struct)
            dataset['House Type'] = dataset['House Type'].map(house_type)

            X = dataset.iloc[:, 0:-1].values
            y = dataset.iloc[:, -1].values
            y = y.reshape(len(y),1)

            sc_X = StandardScaler()
            sc_y = StandardScaler()
            X = sc_X.fit_transform(X)
            y = sc_y.fit_transform(y)

            # Predicting the result
            y_pred = sc_y.inverse_transform(reg.predict(sc_X.transform([main_data_list])))

            print(y_pred)
            # Returning the response
            return jsonify({
                'predictedValue': str(list(y_pred)[0])
            })
        except Exception as e:
            print(e)
            return jsonify({
                'error':"Some Error occurred"
            })


class sentiment_analysis(Resource):
    def __init__(self):
        pass
    
    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            main_data_list = data['main_data']

            # Loading the Classification Model
            path = os.getcwd()
            path = path + "/Classification/sentiment_analysis"
            pred = joblib.load(path+'sentiment_analysis_model.pkl')

            # Predicting the result
            y_pred = pred.predict(data['main_data'])

            print(y_pred)
            # Returning the response
            return jsonify({
                'predictedValue': str(list(y_pred)[0])
            })
        except Exception as e:
            print(e)
            return jsonify({
                'error':"Some Error occurred"
            })

class Advertisement(Resource):
    def __init__(self):
        pass
    
    def get(self):
        try:
            path = os.getcwd()
            path = path + "/DataAnalysis/Ads_CTR_Optimisation.csv"
            dataset = pd.read_csv(path)
            N = 10000
            d = 10
            ads_selected = []
            numbers_of_rewards_1 = [0] * d
            numbers_of_rewards_0 = [0] * d
            total_reward = 0
            for n in range(0, N):
                ad = 0
                max_random = 0
                for i in range(0, d):
                    random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
                    if random_beta > max_random:
                        max_random = random_beta
                        ad = i
                ads_selected.append(ad)
                reward = dataset.values[n, ad]
                if reward == 1:
                    numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
                else:
                    numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
                total_reward = total_reward + reward
            
            # Count Ads Selected Count
            counts = {}

            for i in range(0, d):
                current = ads_selected.count(i)
                counts[i] = current

            print(counts)
            print(ad)
            print(total_reward)
            print(dataset.values.tolist())

            return jsonify({
                'ad_counts': counts,
                'ad_selected': str(ad),
                'total_reward': str(total_reward),
                'dataset': dataset.values.tolist()
            })

        except Exception as e:
            print(e)
            return jsonify({
                'error': "Some Error occurred"
            })

class cosineSimilarity(Resource):
    def __init__(self):
        pass
    
    def post(self):
        try:
            # Getting data from json
            data = request.get_json()
            X = data['X'].lower()
            Y = data['Y'].lower()

            print("Text 1 : ", X)
            print("Text 2 : ", Y)

            # tokenization
            X_list = word_tokenize(X)
            Y_list = word_tokenize(Y)

            # sw contains the list of stopwords
            sw = stopwords.words('english')
            l1 =[];l2 =[]

            # remove stop words from the string
            X_set = {w for w in X_list if not w in sw}
            Y_set = {w for w in Y_list if not w in sw}

            # form a set containing keywords of both strings
            rvector = X_set.union(Y_set)
            for w in rvector:
                if w in X_set: l1.append(1) # create a vector
                else: l1.append(0)
                if w in Y_set: l2.append(1)
                else: l2.append(0)
            c = 0

            # cosine formula
            for i in range(len(rvector)):
                    c+= l1[i]*l2[i]
            cosine = c / float((sum(l1)*sum(l2))**0.5)
            print("similarity: ", cosine)

            return jsonify({
                'cosine': str(cosine)
            })

        except Exception as e:
            print(e)
            return jsonify({
                'error': "Some Error occurred"
            })


api.add_resource(AI, '/')
api.add_resource(classify_house_structure, '/predict_structure')
api.add_resource(classify_house_type, '/predict_type')
api.add_resource(classify_tenouse_premium, '/predict_premium')
api.add_resource(regress_tenouse_profit, '/predict_profit')
api.add_resource(regress_house_price, '/predict_house_price')
api.add_resource(Advertisement, '/predict_advertisement')
api.add_resource(cosineSimilarity, '/predict_cosine_similarity')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    # app.run(debug=True, port=8000)