import os
import flask

import data
import data.one_table
import data.update_one_table


DEBUG = os.environ.get('DEBUG') == 'on'
PORT = int(os.environ.get('PORT', 5000))
HOST = '127.0.0.1' if DEBUG else '0.0.0.0'


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
    'sqlite:////tmp/daisypi.db')
if DEBUG:
    app.config['SQLALCHEMY_ECHO'] = True
data.DB.init_app(app)
with app.app_context():
    data.DB.create_all()


@app.route('/hello')
def hello_world():
    return flask.render_template('hello_world.html')

@app.route('/')
def index():
    entries = data.one_table.Reading.query.all()
    for entry in entries:
        print('Printing ' + str(entry))
    return flask.render_template('index.html',
        entries=entries)

@app.route('/update', methods=['POST'])
def update():
    # print(flask.request)
    data.update_one_table.update(flask.request.json)
    return 'OK!'


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)

