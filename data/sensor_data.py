"""Model the information received from a Daisy."""

import datetime

from . import DB


class Temperature(DB.Model):
    '''Model a temperature reading.'''
    feed_id = DB.Column(DB.Integer, primary_key=True)
    timestamp = DB.Column(DB.DateTime, primary_key=True)
    value = DB.Column(DB.Float)

    def __init__(self, feed_id, value, timestamp=None):
        self.feed_id = feed_id
        self.value = value
        if timestamp is None:
            timestamp = datetime.datetime.now()
        self.timestamp = timestamp

    def __repr__(self):
        return '<Temperature entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)


class Humidity(DB.Model):
    '''Model an air humidity reading.'''
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
        return '<Humidity entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)


class DewPoint(DB.Model):
    '''Model a dew point reading.'''
    feed_id = DB.Column(DB.Integer, primary_key=True)
    timestamp = DB.Column(DB.DateTime, primary_key=True)
    value = DB.Column(DB.Float)

    def __init__(self, feed_id, value, timestamp=None):
        self.feed_id = feed_id
        self.value = value
        if timestamp is None:
            timestamp = datetime.datetime.now()
        self.timestamp = timestamp

    def __repr__(self):
        return '<DewPoint entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)


class Light(DB.Model):
    '''Model a light sensor reading.'''
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
        return '<Light entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)


class Pressure(DB.Model):
    '''Model an air pressure reading.'''
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
        return '<Pressure entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)


class Analog(DB.Model):
    '''Model a reading from an analog sensor.'''
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
        return '<Analog entry ({0} , {1} , {2})>'.format(
            self.feed_id, self.timestamp.strftime('%c'), self.value)
