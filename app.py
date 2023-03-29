from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toon')
def review():
    return render_template('review.html')


# ===========
@app.route("/review", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/review", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)