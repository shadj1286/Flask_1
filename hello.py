from flask import Flask, render_template

#create a flask instance 
app=Flask(__name__)
 #create a route decorator 
@app.route('/')
# def index():
#     return "<h1>Hello World</h1>"
def index():
    stuff="This is <strong>Bold</strong> text"
    favourite_Pizza=["peperroni","cheese","Mushroom",56]
    return render_template("index1.html",stuff=stuff,pizza=favourite_Pizza)
#localhost:5000/user/John 
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",name=name)

#create custom error pages :
#invalid URL ERROR
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server ERROR 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500
    
if __name__ == '__main__':
    app.run(debug=True)
