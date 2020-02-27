from flask import request, jsonify, url_for
import random
import re
from datetime import datetime

from app.models import Point

from app import db

from app.data_route import bp


@bp.route('/getData', methods=['POST']) # for AJAX
def sendData():

    """
    sendData
    sendData - recieve incoming JSON with module parameters,
    modified it by data from data base and return back
    If key 'imit' = 1, then data will take not in from data base,
    data will be random.
    """

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
    """
    putData.

    putData catch GET or POST requests and put paramaterers from it to db.
    The name of point must match pattern 'LoRa', otherwise it will be ignored.
    If name have not in database(db), will be create new point.
    """
    content = request.get_json(silent=True)
    # print("*******************************************")
    # print("Incoming Request")
    # print("datetime now {}".format(datetime.utcnow()))
    # print("headers {}".format(request.headers))
    # print("MIME type {}".format(request.accept_mimetypes))
    # print("Date is {}".format(request.date))
    # print("Request method: {}".format(request.method))
    # print("Content-Type: {}".format(request.content_type))
    # print("Data as JSON: {}".format(content))
    # print("Raw data: {}".format(request.data))
    # print("********************************************")

    if request.content_type is None:
        return (jsonify({"content_type": "None"}), "200")

    if content is None:
        return (jsonify({"Content": "invalid"}), "200")

    # method GET not used
    if request.method == "GET":

        param = request.args

        match = re.search("LoRa", param["pointname"]) # name match LoRa or not

        if match:
            point = Point.query.filter_by(pointname=content["pointname"]).first()
            
        reply = {"Method": "GET"}
        return (jsonify(reply), "200")

    
    if request.method == "POST":

        match = re.search("LoRa", content["pointname"]) # name match LoRa or not

        # for item in Point.query.all():
        #     print("Item in db: {}".format(item))
  
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
            
            compareData(content,point,ignorKeys=('id','pointname','date','modulName','data','load1','load2','load3'))

            point.date = str(datetime.now().isoformat(timespec = 'seconds'))
            point.modulName = str(request.user_agent)

            db.session.add(point)
            db.session.commit()

            reply = {"load1": point.load1,"load2": point.load2,"load3": point.load3}
            return (jsonify(reply), "200")

        return (jsonify({"Name": "invalid"}), "200")

def compareData(inc_data: 'dict',db_point: 'Point',ignorKeys: 'tuple' =()) -> None:

    """
    compareData.

    Compare 'inc_data' and 'db_point' by key, without keys in 'ignorKeys'.
    'inc_data' - incoming dict
    'db_point' - instatnce of Point
    'ignorKeys' - tuple of keywords for ignor
    'stateIsChange' - check is state change
    """

    [db_point.setAttr(key,inc_data.get(key)) for key in inc_data if (stateIsChange(db_point.get(key),str(inc_data.get(key))) and inc_data.get(key) not in ignorKeys)]


def stateIsChange(stateOld,stateNew):

    """
    stateIsChange

    stateIsChange - check is state change or not

    """

    if stateOld == None or stateNew == None:
        return False
    if stateOld != stateNew:
        stateOld = stateNew
        print('value is changed {}'.format(stateOld))
        return True
    return False 