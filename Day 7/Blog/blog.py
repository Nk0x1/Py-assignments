import requests
from flask import Flask,render_template
app=Flask(__name__)
r=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
allblogs=r.json()



@app.route('/')
def port():
     return render_template("index.html",posts=allblogs)


     

@app.route('/read<int:i>')
def read(i):
     return render_template("post.html",title=allblogs[i]["title"],body=allblogs[i]['body'])



if __name__=="__main__":
    app.run(debug=True)





