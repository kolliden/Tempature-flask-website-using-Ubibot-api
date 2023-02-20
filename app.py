from flask import Flask, render_template
from Interface import Interface

app = Flask(__name__)
interface = Interface()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
async def weather():

    temp, humidity, lightLevel = await interface.main()
    return render_template('page.html', temp=temp, humidity=humidity, lightLevel=lightLevel)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')