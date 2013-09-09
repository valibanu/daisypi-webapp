import random
import json
import time
import argparse

import requests


parser = argparse.ArgumentParser(description='Generate random entries '
    'for a Daisy Pi feed.')
parser.add_argument('count', action='store', nargs='?', default=1,
    type=int, help='the number of entries to generate (default: 1)',
    metavar='N')
parser.add_argument('--debug', '-d', action='store_true',
    dest='debug_mode',
    help='in debug mode the entries will be sent to 127.0.0.1, '
    'not on the production server')
parser.add_argument('--feed', '-f', action='store', nargs='?',
    default=1, type=int, help='the feed ID of the entries (default: 1)',
    metavar='ID', dest='feed_id')
args = parser.parse_args()

if args.debug_mode:
    url = 'http://127.0.0.1:5000/update'
else:
    url = 'http://daisy-py-17103.euw1.actionbox.io:5000/update'
print('Sending {0} entries to {1}'.format(args.count, url))

for index in range(args.count):
    entry = {'feed_id': args.feed_id, 'value': random.randint(0, 1000)}
    print('Sending {0} to {1}'.format(entry, url))
    requests.post(url, data=json.dumps(entry),
        headers={'content-type': 'application/json'})
    time.sleep(1)


