from flask import *
import sqlite3 as sql
import os
import config as cf
import json
import pandas as pd
import mainfile as md

app = Flask(__name__)

@app.route("/get-all-data")
def get_all_data():
    c = db_connect()
    c[0].execute("SELECT * FROM historical_data")
    all_data = c[0].fetchall()
    db_close(c) 
    return json.dumps(all_data)

@app.route("/particular-day-data")
def get_particular_day_data():
    c = db_connect()
    date = request.args.get('Date')
    c[0].execute("SELECT * FROM historical_data WHERE Date = ?",(date,))
    all_data = c[0].fetchall()
    db_close(c)    
    return json.dumps(all_data)

@app.route("/particular-company-day-data")
def get_particular_company_day_data():
    c = db_connect()
    date = request.args.get('Date')
    company = request.args.get('company')
    c[0].execute("SELECT * FROM historical_data WHERE company = ? AND Date = ? ",(company,date))
    all_data = c[0].fetchall()
    db_close(c)    
    return json.dumps(all_data)

@app.route("/particular-company-data")
def get_particular_company_data():
    c = db_connect()
    company = request.args.get('company')
    c[0].execute("SELECT * FROM historical_data WHERE company = ?",(company,))
    all_data = c[0].fetchall()
    db_close(c)    
    return json.dumps(all_data)

@app.route("/update-stock-company-data", methods = ['POST'])
def update_stock_data():
    c = db_connect()
    date = request.form.get('Date')
    app.logger.info(date)
    company = request.form.get('company')
    open_price = request.form.get('Open')
    high_price = request.form.get('High')
    low_price = request.form.get('Low')
    close_price = request.form.get('Close')
    volume = request.form.get('Volume')
    c[0].execute("UPDATE historical_data SET Open = ?, High = ?, Low = ?, Close = ?, Volume = ? WHERE company = ? AND Date = ?", (open_price, high_price, low_price, close_price, volume, company, date))
    all_data = c[0].fetchall()
    app.logger.info(all_data)
    db_close(c)
    return "Stock updated successfully"

@app.route("/update-db")
def update_db():
    return md.main_db()


def db_connect():
    conn = sql.connect(cf.path) 
    cursor = conn.cursor()
    return cursor,conn


def db_close(c):
    c[1].commit()
    c[0].close()

app.run(debug = True, port = 8888)









