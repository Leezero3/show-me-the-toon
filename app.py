from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
from bson import json_util
import certifi
from bson.objectid import ObjectId
client = MongoClient('mongodb+srv://sparta:test@cluster0.fjodnaz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toon' )
def review():    
    return render_template('toon.html')

##################################################################상우님
@app.route("/review", methods=["POST"])

def mars_post():
    name_receive = request.form['name_give'] #데이터를 찾음
    pw_receive = request.form['password_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    toonid_receive = request.form['toonid_give']


    doc = {
        'name':name_receive,
        'pw':pw_receive,
        'star':star_receive,
        'comment':comment_receive,
        'toonid':toonid_receive
    }##파이몽고에 넣기 위함
    db.comment.insert_one(doc)#mars로 이름변경
    return jsonify({'msg':'저장완료'})#메세지를 내려줌(직관적이게 저장완료로 바꿔줌)

##################################################################
@app.route("/review:commentid", methods=["POST"])
def comment_del():

    del_pw = request.form['pw_give']
    del_id = request.form['commentid_give']

    # print(del_id)   
    # print(del_pw) 
    find_one = db.comment.find_one({'_id': ObjectId(del_id),'pw':del_pw})  #comment 이름의 DB에서 Id, pw값일치하는 것 찾기

    # print(find_one) x

    if (None != find_one):    #Id값과 pw 확인하여 하나라도 다르면 None이 출력. -> else문으로.           
        db.comment.delete_one({'_id': ObjectId(del_id),'pw':del_pw})  
        return jsonify({'msg':'삭제완료'})
    else:        
        return jsonify({'msg':'pw가 일치하지 않습니다.'})    
####################메인화면 시작하면 보내는 GET#####################################

@app.route("/webtoon", methods=["GET"])
def webtoon_get():
    toon_lists = list(db.toons.find({}))      #toon 이란 이름의 DB에 저장된 것들 메인페이지로
    for mv in toon_lists:
        mv["_id"] = str(mv["_id"])  #이렇게 하니 id 값도 넘어감
    return jsonify({'result':toon_lists})
#########################################################################

@app.route("/tooncomment", methods=["GET"])
def tooncomment_get():
    tooncommnet_list = db.toons.find_one({'name':'bobby'})

    # toon_lists = list(db.toons.find({}))      #toon 이란 이름의 DB에 저장된 것들 메인페이지로
    # for mv in toon_lists:
    #     mv["_id"] = str(mv["_id"])  #이렇게 하니 id 값도 넘어감
    # return jsonify({'result':tooncommnet_list})



@app.route("/toonrender", methods=["POST"])
def toon_get():
    objectId = request.form['objectId_give']
    toon = db.toons.find_one({'_id':ObjectId(objectId)})
    # comment = db.comment.find({'toonid':ObjectId(objectId)})
    # comment_list = [comment_dict for comment_dict in comment]
    # result = {'toon': toon, 'comment': comment_list}
    
    #print(toon)
    # return jsonify(json_util.dumps({'result':toon}))
    return json_util.dumps(toon)
@app.route("/commentrender", methods=["POST"])
def comment_get():
    objectId = request.form['objectId_give']
    print(objectId)
    comment = list(db.comment.find({'toonid':objectId},{'_id':False}))
    print(comment)
    return jsonify(comment)

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))




if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)