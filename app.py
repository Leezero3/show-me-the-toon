from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toon')
def review():
    return render_template('toon.html')
##################################################################
@app.route("/review:commentid", methods=["POST"])
def comment_del():

    del_pw = request.form['pw_give']
    del_id = request.form['commentid_give']

    # print(del_id)   
    # print(del_pw) 
    find_one = db.comment.find_one({'_id': ObjectId(del_id),'pw':del_pw})

    # print(find_one)

    if (None != find_one):       
        # print("PW가 일치합니다.")
        db.comment.delete_one({'_id': ObjectId(del_id),'pw':del_pw})
        return jsonify({'msg':'삭제완료'})
    else:
        #  print("pw가 일치하지 않습니다.")
         return jsonify({'msg':'pw가 일치하지 않습니다.'})    
####################메인화면 시작하면 보내는 GET#####################################

@app.route("/webtoon", methods=["GET"])
def webtoon_get():
    webtoon_lists = list(db.webtoon.find({}))      #webtoon 이란 이름의 DB에 저장된 것들 메인페이지로
    for mv in webtoon_lists:
        mv["_id"] = str(mv["_id"])  #이렇게 하니 id 값도 넘어감
    return jsonify({'result':webtoon_lists})
#########################################################################

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)