from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        print(get_weather(city, state, country))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)