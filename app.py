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
#######################################################################

@app.route("/review", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)