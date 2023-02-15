from flask import Flask, render_template
from getWeather import getWeather

app = Flask(__name__)
getter = getWeather()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
async def weather():

    temp = await getter.main()
    return render_template('page.html', temp=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')