# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request



# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index(): 
    return render_template("index.html")
  
  

@app.route('/gethelp')
def gethelp():
    return render_template("gethelp.html")




@app.route('/log-in')
def login():
    return render_template("log-in.html")


@app.route('/sign-up')
def signup():
    return render_template("sign-up.html")


@app.route('/signed-in', methods= ["POST", "GET"])
def signedin():
    print(request.form["uname"])
    user_name = request.form["uname"]  
    if request.method == "POST": 
        return render_template("signed-in.html", user_name= user_name)
    elif request.method == "get":
        return "404 Error"

@app.route('/gethelp-signedin')
def gethelsn():
    return render_template("gethelp-signedin.html") 

@app.route('/chatroom-signedin') 
def chatrmsi():
    return render_template("chatroom-signedin.html")  

@app.route('/talk-signedin')
def talksi():
    return render_template("talk-signedin.html")

@app.route('/forgotpassword')
def forgorpws():
    return render_template("forgot-password.html")


@app.route('/chatroom')
def chatroom():
    return render_template("chatroom.html")


@app.route('/talk')
def talk():
    return render_template("talk.html")


@app.route('/chatroom-Anxiety')
def chatanx():
    return render_template("chat-anx.html")

@app.route('/chatroom-Bipolar')
def chatbi():
    return render_template("chat-bi.html")    

@app.route('/chatroom-Depression')
def chatdep():
    return render_template("chat-dep.html")

@app.route('/chatroom-ADHD')
def chatad():
    return render_template("chat-ad.html")

@app.route('/chatroom-Stress')
def chatstr():
    return render_template("chat-str.html")

@app.route('/chatroom-Schizophrenia')
def chatsch():
    return render_template("chat-sch.html")

@app.route('/chatroom-Anxiety-signedin')
def chatanxsi():
    return render_template("chat-anx-signedin.html")

@app.route('/chatroom-Bipolar-signedin')
def chatbisi():
    return render_template("chat-bi-signedin.html")    

@app.route('/chatroom-Depression-signedin')
def chatdepsi():
    return render_template("chat-dep-signedin.html")

@app.route('/chatroom-ADHD-signedin')
def chatadsi():
    return render_template("chat-ad-signedin.html")

@app.route('/chatroom-Stress-signedin')
def chatstrsi():
    return render_template("chat-str-signedin.html")

@app.route('/chatroom-Schizophrenia-signedin')
def chatschsi():
    return render_template("chat-sch-signedin.html")








