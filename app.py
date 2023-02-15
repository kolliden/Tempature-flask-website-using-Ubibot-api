from flask import Flask, render_template
from getWeather import getWeather
from env import config

app = Flask(__name__)
getter = getWeather()

app = config(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
async def weather():

    temp = await getter.main(app.secret_key)
    return render_template('page.html', temp=temp)

if __name__ == '__main__':
    app.run(debug=app.debug, host='0.0.0.0')