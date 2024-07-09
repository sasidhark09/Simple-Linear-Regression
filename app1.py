from flask import Flask

'''
It Creates an instance of the flask class
which will be your WSGI application
'''

##WSGI APPLICATION
app=Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this Flask Course. This would be Amazing!"

@app.route("/index")
def index():
    return "Welcome to index page!"


### Entry Point of .py file
## Execution starts from here
if __name__=="__main__" :
    app.run(debug=True)

## debug=True makes changes without manually restarting server