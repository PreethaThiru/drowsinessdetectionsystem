from flask import Flask,render_template  # import flask object from flask library and render template access html file
import Code
app=Flask(__name__)  # representing the flask object by an instance




@app.route('/')    
def home():
    return render_template("index.html")



@app.route('/code.py')    
def code():
     return "Website content goes here!"



@app.route('/run.html')    
def run():
    Code.start1()
    return render_template("run.html")

@app.route('/test.html')    
def test():
    return render_template("test.html")

@app.route('/timeline.html')    
def timeline():
    return render_template("timeline.html")    

@app.route('/index.html')    
def index():
    return render_template("/index.html")    


if __name__=="__main__":
    app.run(debug=True)