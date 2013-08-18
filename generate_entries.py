
import sys
import random
import json

import requests

# import daisypi


if len(sys.argv) >= 2:
    count = int(sys.argv[1])
else:
    count = 1
print('Generating {0} entries'.format(count))

# url = 'http://{0}:{1}/update'.format(daisypi.HOST, daisypi.PORT)
url = 'http://127.0.0.1:5000/update'
for index in range(count):
    entry = {'feed_id': random.randint(1, 10), 'value': random.randint(0, 100)}
    print('Sending {0} to {1}'.format(entry, url))
    requests.post(url, data=json.dumps(entry),
        headers={'content-type': 'application/json'})

