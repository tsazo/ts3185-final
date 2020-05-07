

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/columbia')
def columbia():
    return render_template('columbia.html')

#start the server
if __name__ == "__main__":
    app.run()