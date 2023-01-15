from peewee import SqliteDatabase, Model, CharField, PrimaryKeyField, TextField
from flask import Flask, redirect, request
from datetime import datetime
import os

app = Flask(__name__)
db = SqliteDatabase("taskbase.db")

class Base(Model):
    class Meta:
        database = db

class Tasks(Base):
    id = PrimaryKeyField()
    user_create = CharField()
    for_user = CharField()
    date = CharField()
    label = CharField()
    task = TextField()
    status = CharField()


@app.route("/add", methods=["POST"])
def r_add():
    try:
        for_user = request.headers.get("user")
        label = request.headers.get("label")
        text = request.headers.get("text")
        creator = request.headers.get("creator")
        date = datetime.strftime(datetime.now(),"%H:%M %d:%m:%y")
        
        t = Tasks(user_create=creator, for_user=for_user, date=date, label=label, task=text, status="0")
        t.save()
        return f"Task add for:{for_user} in:{creator} id:{t.id} date:{t.date}"
    except Exception as e:
        print(e)
        return "Error add task"

if __name__ == "__main__":
    if not os.path.exists("taskbase.db"):
        Tasks.create_table()
    app.run(debug=True, port=6311)