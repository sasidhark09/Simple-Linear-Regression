from flask import Flask,render_template

'''
It Creates an instance of the flask class
which will be your WSGI application
'''

##WSGI APPLICATION
app=Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index1.html')

@app.route("/index")
def index():
    return "Welcome to index page!"


@app.route("/about")
def about():
    return render_template('about.html')


### Entry Point of .py file
## Execution starts from here
if __name__=="__main__" :
    app.run(debug=True)

## debug=True makes changes without manually restarting server