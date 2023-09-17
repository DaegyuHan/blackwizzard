from flask import Flask, render_template, request, jsonify

from bson.objectid import ObjectId
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import certifi
from numpy import string_
from datetime import datetime
import sys
import time

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.edvfknb.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.blackwizzard

application = app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def chrstat_post():
    URL1 = "https://maple.gg/u/%EB%8C%80%EB%80%A8%EC%A7%B1"
    headers1 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data1 = requests.get(URL1,headers=headers1)
    soup1 = BeautifulSoup(data1.text, 'html.parser')

    image1 = soup1.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level1 = soup1.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string
    union1 = soup1.select_one("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span").string





    URL2 = "https://maple.gg/u/%EC%9D%B4%EC%B0%AC%EC%9B%85"
    headers2 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data2 = requests.get(URL2,headers=headers2)
    soup2 = BeautifulSoup(data2.text, 'html.parser')

    image2 = soup2.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level2 = soup2.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string
    union2 = soup2.select_one("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span").string


    URL3 = "https://maple.gg/u/%EB%84%88%EB%B3%B4"
    headers3 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data3 = requests.get(URL3,headers=headers3)
    soup3 = BeautifulSoup(data3.text, 'html.parser')

    image3 = soup3.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level3 = soup3.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string

    URL27 = "https://maple.gg/u/%EC%A0%9C41%EB%8C%80"
    headers27 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data27 = requests.get(URL27,headers=headers27)
    soup27 = BeautifulSoup(data27.text, 'html.parser')

    image27 = soup27.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level27 = soup27.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string





    URL4 = "https://maple.gg/u/%ED%99%A9%EA%B8%88%EB%AA%A8%EB%9E%98%ED%8F%AD%ED%92%8D"
    headers4 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data4 = requests.get(URL4,headers=headers4)
    soup4 = BeautifulSoup(data4.text, 'html.parser')

    image4 = soup4.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level4 = soup4.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string
    union4 = soup4.select_one("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span").string

    URL5 = "https://maple.gg/u/%ED%98%B8%EB%96%A1%EB%A8%B9%EC%9D%84%ED%86%A0%EB%81%BC"
    headers5 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data5 = requests.get(URL5,headers=headers5)
    soup5 = BeautifulSoup(data5.text, 'html.parser')

    image5 = soup5.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level5 = soup5.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string
    union5 = soup5.select_one("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span").string

    URL6 = "https://maple.gg/u/%ED%95%9C%EC%A0%95%EA%B7%9C"
    headers6 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data6 = requests.get(URL6,headers=headers5)
    soup6 = BeautifulSoup(data6.text, 'html.parser')

    image6 = soup6.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level6 = soup6.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string
    union6 = soup6.select_one("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span").string


    URL7 = "https://maple.gg/u/%EB%80%A8%EB%AF%B8%EB%BB%AC%EC%96%B4"
    headers7 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data7 = requests.get(URL7,headers=headers5)
    soup7 = BeautifulSoup(data7.text, 'html.parser')

    image7 = soup7.select_one("#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img").string
    level7 = soup7.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)").string
    union7 = soup7.select_one("#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span").string


    level = [level1, level2, level27, level4, level5, level6, level7]
    union = [union1, union2, 8512, union4, union5, union6, union7]
    image = [image1, image2, image3, image4, image5, image6, image7]

    stat = {
        'level' : level,
        'union' : union,
        'image' : image
    }
    
    return jsonify({'result':stat})


@app.route("/savebtn", methods=["POST"])
def btn_post():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn", methods=["GET"])
def btn_get():
    all_btns = list(db.blackwizzard.find({},{'_id':False}))
    return jsonify({'result': all_btns})



@app.route("/savebtn14", methods=["POST"])
def btn_post14():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard14.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn14", methods=["GET"])
def btn_get14():
    all_btns14 = list(db.blackwizzard14.find({},{'_id':False}))
    return jsonify({'result': all_btns14})



@app.route("/savebtn27", methods=["POST"])
def btn_post27():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard27.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn27", methods=["GET"])
def btn_get27():
    all_btns27 = list(db.blackwizzard27.find({},{'_id':False}))
    return jsonify({'result': all_btns27})




@app.route("/savebtn71", methods=["POST"])
def btn_post71():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard71.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn71", methods=["GET"])
def btn_get71():
    all_btns71 = list(db.blackwizzard71.find({},{'_id':False}))
    return jsonify({'result': all_btns71})

@app.route("/savebtn63", methods=["POST"])
def btn_post63():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard63.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn63", methods=["GET"])
def btn_get63():
    all_btns63 = list(db.blackwizzard63.find({},{'_id':False}))
    return jsonify({'result': all_btns63})


@app.route("/savebtn35", methods=["POST"])
def btn_post35():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard35.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn35", methods=["GET"])
def btn_get35():
    all_btns35 = list(db.blackwizzard35.find({},{'_id':False}))
    return jsonify({'result': all_btns35})


@app.route("/savebtn45", methods=["POST"])
def btn_post45():
    name_receive = request.form['name_give']
    btn_receive = request.form['btn_give']
    date_receive = request.form['date_give']
    onlydate_receive = request.form['onlydate_give']
    text_receive = request.form['text_give']
    timeh_receive = request.form['timeh_give']
    timem_receive = request.form['timem_give']
    timea_receive = request.form['timea_give']

    doc = {
        'name':name_receive,
        'date':date_receive,
        'onlydate':onlydate_receive,
        'btn_id':btn_receive,
        'text':text_receive,
        'timeh':timeh_receive,
        'timem':timem_receive,
        'timea':timea_receive

    }
    db.blackwizzard45.insert_one(doc)
    

    return jsonify({'msg': '등록 완료!'})


@app.route("/savebtn45", methods=["GET"])
def btn_get45():
    all_btns45 = list(db.blackwizzard45.find({},{'_id':False}))
    return jsonify({'result': all_btns45})


@app.route("/notice", methods=["POST"])
def notice_post():
    notice_receive = request.form['notice_give']
    doc = {
        'notice_text':notice_receive
    }
    db.notice.insert_one(doc)

    return jsonify({'msg': '공지 저장 완료'})

@app.route("/notice", methods=["GET"])
def notice_get():
    all_notice = list(db.notice.find({},{'_id':False}))
    return jsonify({'result': all_notice})



@app.route("/sundaymaple", methods=["POST"])
def sunday_post():
    sunday_receive = request.form['sunday_give']
    doc = {
        'sunday_text':sunday_receive
    }
    db.sundaymaple.insert_one(doc)

    return jsonify({'msg': '선데이메이플 저장 완료'})

@app.route("/sundaymaple", methods=["GET"])
def sunday_get():
    all_sunday = list(db.sundaymaple.find({},{'_id':False}))
    return jsonify({'result': all_sunday})




if __name__ == "__main__":
    app.run()