from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.th8mwq2.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

# POST 방식
@app.route('/users', methods=['POST']) 
def test_post():  
   comment_receive = request.form['comment_give']

   doc = {
      'comment' : comment_receive
   }
   db.users.insert_one(doc)

   return jsonify({'msg':'저장완료!'}) 

# GET 방식
@app.route("/users", methods=["GET"])       #get의 fetch에서 users로 데이터가 날아옴       
def users_get():
    users_data = list(db.users.find({},{'_id':False}))

    return jsonify({'result':users_data})    #'result':mars_data 로 다시 html로 내린다



# Delete 방식
@app.route('/users', methods=['DELETE'])
def users_del():
   comment_receive = request.form['comment_del']
   db.users.delete_one({'comment': comment_receive})
   return jsonify({'msg': '삭제 완료!'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)