import os
import flask

from data import DB


DEBUG = os.environ.get('DEBUG') == 'on'
PORT = int(os.environ.get('PORT', 5000))


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
    'sqlite:////tmp/daisypi.db')
if DEBUG:
    app.config['SQLALCHEMY_ECHO'] = True
DB.init_app(app)
with app.app_context():
    DB.create_all()


@app.route('/')
def hello_world():
    return flask.render_template('hello_world.html')


if __name__ == '__main__':
    host = '127.0.0.1' if DEBUG else '0.0.0.0'
    app.run(debug=DEBUG, port=PORT, host=host)



