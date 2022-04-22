from flask import Flask,render_template,Response,jsonify
import cv2
import time
import datetime
import cvzone
import json
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

app=Flask(__name__)
cap=cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]

color = (255, 0, 255)

ratioList = []

with open('overall.json') as f:
    data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/emotion')
def emotion():
    data1 = data
    person = data1['person']
    BlinkData = data1['blink_data']
    current_time = data1['current_time']
    return render_template("new.html",person = person,blinkdata= BlinkData,current_time = current_time)

if __name__ == "__main__":
    app.run(debug=True)