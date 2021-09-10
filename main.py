from datetime import datetime
from flask import Flask, json, request, jsonify
import db
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route('/collecting',methods=['POST','GET'])
def collect():
    rows = db.selectAllisRead(conn=db.connector())
    allData = []
    for row in rows:
        allData.append(
            {
                "id": row[0],
                "Name": row[1],
                "NationalCode": row[2],
                "WithPicture": row[3],
                "WithFinger": row[4],
                "isRead": row[5],
                "Date": row[6],
                "Time": row[7],
                "RegisteredFinger": row[8],
                "RegisteredFace": row[9],
            }
        )
    return jsonify(allData)

@app.route('/reread',methods=['POST','GET'])
def reread():
    first_date = request.args["fdate"]
    second_date = request.args["sdate"]
    rows = db.selectAllDate(conn=db.connector(), date1=first_date, date2=second_date)
    allData = []
    for row in rows:
        allData.append(
            {
                "id": row[0],
                "Name": row[1],
                "NationalCode": row[2],
                "WithPicture": row[3],
                "WithFinger": row[4],
                "isRead": row[5],
                "Date": row[6],
                "Time": row[7],
                "RegisteredFinger": row[8],
                "RegisteredFace": row[9],
            }
        )
    return jsonify(allData)

@app.route('/removeall',methods=['POST','GET'])
def removeall():
    db.deleteAll(db.connector())
    return jsonify({"Status": "Success"})

@app.route('/removeuser',methods=['POST','GET'])
def removeuser():
    NationalCode = request.args["national"]
    db.deleteRow(conn=db.connector(), NatiCode=NationalCode)
    return jsonify({"Status": "success"})

@app.route('/register',methods=['POST','GET'])
def register():
    reg_type = request.args["regtype"]
    NationalCode = request.args["national"]
    Fullname = request.args["fullname"]
    result = db.search(db.connector(), NatiCode=NationalCode)
    allData = []
    for row in result:
        allData.append(
            {
                "id": row[0],
                "Name": row[1],
                "NationalCode": row[2],
                "WithPicture": row[3],
                "WithFinger": row[4],
                "isRead": row[5],
                "Date": row[6],
                "Time": row[7],
                "RegisteredFinger": row[8],
                "RegisteredFace": row[9],
            }
        )
    if allData:
            return jsonify({"Error":"exist!"})
    else:
        if reg_type == "picture":
            pic_enroll = 1
            fing_enroll = 0
            pic_enter = 0
            fing_enter = 0
            isread = 0
            date = datetime.today().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")
            position = -10
            db.insertData(db.connector(), Fullname, NationalCode, pic_enter, fing_enter, isread, date, time, pic_enroll, fing_enroll, position)
            return jsonify({"Status": "Face Record Insert"})


        elif reg_type == "finger":
            pic_enroll = 0
            fing_enroll = 1
            pic_enter = 0
            fing_enter = 0
            isread = 0
            date = datetime.today().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")
            position = -10
            db.insertData(db.connector(), Fullname, NationalCode, pic_enter, fing_enter, isread, date, time, pic_enroll, fing_enroll, position)
            return jsonify({"Status": "Finger Record Insert"})

        
    
if __name__ == "__main__":
    app.run(debug=True)
