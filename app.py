from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from fastai.basic_train import load_learner
from fastai.vision import *
from flask_cors import CORS,cross_origin
import os
import sys

import torch
from torch import nn
from torchvision import datasets, transforms, models
import torchvision.models as models
import torch.nn.functional as F
import torchvision.transforms.functional as F
from torch import optim
import json

from PIL import *
import requests
from io import BytesIO

import numpy as np

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

            path = os.getcwd()
            path = path + "/Classification/house_structure/"
            learn = load_learner(path=path, file='house_structure_classify_model.pkl')
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


api.add_resource(AI, '/')
api.add_resource(classify_house_structure, '/predict_structure')
api.add_resource(classify_house_type, '/predict_type')


if __name__=='__main__':
    app.run(debug=True, port=8000)