"""Model all the data in one big table."""

import datetime

from . import DB


class Reading(DB.Model):
    '''Model an arbitrary sensos reading.'''
    feed_id = DB.Column(DB.Integer, primary_key=True)
    timestamp = DB.Column(DB.DateTime, primary_key=True)
    value = DB.Column(DB.Integer)

    def __init__(self, feed_id, value, timestamp=None):
        self.feed_id = feed_id
        self.value = value
        if timestamp is None:
            timestamp = datetime.datetime.now()
        self.timestamp = timestamp

    def __repr__(self):
        return '<Reading entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)
