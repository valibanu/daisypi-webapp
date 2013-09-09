import os
import json

import flask
from sqlalchemy import desc

import data
import data.one_table
import data.update_one_table


DEBUG = os.environ.get('DEBUG') == 'on'
PORT = int(os.environ.get('PORT', 5000))
HOST = '127.0.0.1' if DEBUG else '0.0.0.0'
if DEBUG and os.environ.get('DEBUG_IN_PRODUCTION') == 'on':
    HOST = '0.0.0.0'

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
    'sqlite:////tmp/daisypi.db')
if DEBUG:
    app.config['SQLALCHEMY_ECHO'] = True
data.DB.init_app(app)
with app.app_context():
    data.DB.create_all()


@app.route('/')
def index():
    return flask.render_template('hello_world.html')


@app.route('/update', methods=['POST'])
def update():
    data.update_one_table.update(flask.request.json)
    return 'OK!'


@app.route('/show', methods=['GET'])
def show_feed():
    if 'feed_id' in flask.request.args:
        str_feed_id = flask.request.args.get('feed_id')
        try:
            feed_id = int(str_feed_id)
        except ValueError:
            return flask.render_template('index.html',
                error='Invalid Feed ' + str_feed_id)
        entries = data.one_table.Reading.query.filter_by(feed_id=feed_id)
    else:
        entries = data.one_table.Reading.query.all()
    return flask.render_template('index.html', entries=entries)


@app.route('/get_feed', methods=['GET'])
def get_feed():
    response = {'status': 'OK'}
    if 'feed_id' in flask.request.args:
        str_feed_id = flask.request.args.get('feed_id')
        try:
            feed_id = int(str_feed_id)
        except ValueError:
            response['status'] = 'ERR: Invalid Feed ' + str_feed_id
        else:
            entries = data.one_table.Reading.query.filter_by(
                feed_id=feed_id).order_by(
                desc(data.one_table.Reading.timestamp)).limit(100).all()
            pairs = []
            for entry in entries:
                pairs.append({'timestamp': entry.timestamp.isoformat(),
                    'value': entry.value})
            response['pairs'] = pairs
    return json.dumps(response)


@app.route('/show_graph', methods=['GET'])
def show_graph():
    if 'feed_id' in flask.request.args:
        str_feed_id = flask.request.args.get('feed_id')
        try:
            feed_id = int(str_feed_id)
        except ValueError:
            return flask.render_template('index.html',
                error='Invalid Feed ' + str_feed_id)
        return flask.render_template('graph.html', feed_ids=[feed_id]);
    else:
        #TODO: replace data.FEED_IDS with a query
        return flask.render_template('graph.html', feed_ids=list(data.FEED_IDS));
        # return flask.redirect(flask.url_for('get_feed'));


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)

