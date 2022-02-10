from flask import Flask, render_template
from dynamodb_access import get_all_readings

app = Flask(__name__)


@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings)


if __name__ == '__main__':
    app.run()
