from flask import request, jsonify, url_for
import random
import re
from datetime import datetime

from app.models import Point

from app import db

from app.data_route import bp


@bp.route('/getData', methods=['POST']) # for AJAX
def sendData():

    content = request.get_json()
    print(content)

    if content["imit"] == 1:
        content["vSeti"] = random.randint(219, 223)
        content["vAkk"] = random.randint(4, 5)
        content["temp"] = random.randint(10,30)
    else:
        state = Point.query.filter_by(id=content["id"]).first()
        content["vSeti"] = state.volt1
        content["vAkk"] = state.volt2
        content["temp"] = state.temp
        state.load1 = content["load1"]
        state.load2 = content["load2"]
        state.load3 = content["load3"]
        content["digitaiInA"] = state.digInA
        content["digitaiInB"] = state.digInB
        content["digitaiInC"] = state.digInC
        content["digitaiInD"] = state.digInD
        content["date"] = state.date
        content["modulName"] = state.modulName
        db.session.add(state)
        db.session.commit()

    return jsonify(content)




@bp.route('/putData', methods=['GET', 'POST'])
def putData():
    content = request.get_json(silent=True)
    print("*******************************************")
    print("Incoming Request")
    print("datetime now {}".format(datetime.utcnow()))
    print("headers {}".format(request.headers))
    print("MIME type {}".format(request.accept_mimetypes))
    print("Date is {}".format(request.date))
    print("Request method: {}".format(request.method))
    print("Content-Type: {}".format(request.content_type))
    print("Data as JSON: {}".format(content))
    print("Raw data: {}".format(request.data))
    print("********************************************")

    if request.content_type is None:
        return (jsonify({"content_type": "None"}), "200")

    if content is None:
        return (jsonify({"Content": "invalid"}), "200")

    # method GET not used
    #
    if request.method == "GET":
        param = request.args
        print("Query parameters: {}".format(param))
        print(param["pointname"])
        match = re.search("LoRa", param["pointname"]) # name match LoRa or not
        if match:
            point = Point.query.filter_by(pointname=content["pointname"]).first()
            
        reply = {"Method": "GET"}
        return (jsonify(reply), "200")
    #
    #
    
    if request.method == "POST":
        match = re.search("LoRa", content["pointname"]) # name match LoRa or not
        print(Point.query.all())

        for item in Point.query.all():
            print("Item in db: {}".format(item))
  
        if match:
            print("from modul {} data is: {}".format(
                content["pointname"], content))

            point = Point.query.filter_by(pointname=content["pointname"]).first()
            
            if point is None: # create new instance
                print("Point is None")
                point = Point(
                    content["pointname"],content["V1"],content["V2"],content["T"],
                    content["load1"],content["load2"],content["load3"],
                    content["A"],content["B"],content["C"],content["D"]
                    )
                db.session.add(point)
                db.session.commit()
                return ("your first query, ok", "200")

            if point.volt1 != str(content['V1']):
                point.volt1 = str(content['V1'])
                print("volt1 is changed")
            if point.volt2 != str(content['V2']):
                point.volt2 = str(content['V2'])
                print("volt2 is changed")
            if point.temp != str(content['T']):
                point.temp = str(content['T'])
                print("temp is changed")
            if point.digInA != str(content['A']):
                point.digInA = str(content['A'])
                print("digitalInA is changed")
            if point.digInB != str(content['B']):
                point.digInB = str(content['B'])
                print("digitalInB is changed")
            if point.digInC != str(content['C']):
                point.digInC = str(content['C'])
                print("digitalInC is changed")
            if point.digInD != str(content['D']):
                point.digInD = str(content['D'])
                print("digitalInD is changed")
            point.date = str(datetime.now().isoformat(timespec = 'seconds'))
            point.modulName = str(request.user_agent)
            db.session.add(point)
            db.session.commit()
            reply = {"load1": point.load1,"load2": point.load2,"load3": point.load3}
            return (jsonify(reply), "200")
        return (jsonify({"Name": "invalid"}), "200")
