"""Add a newly received JSON to the table of data."""

from . import DB
from one_table import Reading


def update(json_dic):
    # print("************" + json_dic)
    r = Reading(json_dic['feed_id'], json_dic['value'])
    DB.session.add(r)
    DB.session.commit()
    print('Added {0}'.format(r))
