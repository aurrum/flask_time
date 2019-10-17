from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1 align="center">Welcome to aurrum</h1>
    <p align="center">It is currently {time}.</p>

    <img src="http://placeimg.com/700/500/tech" align="middle"/>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

