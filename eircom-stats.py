#!/usr/bin/env python

import argparse
from getpass import getpass
import re
import sys

import requests

def get_stats(username, password, show_graph=False):
    url = 'http://dslstats.eircom.net/commoncgi/dslstats/showstats.cgi?' \
                'stype=total&username=%s&' \
                'password=%s&DCSext.clickedFrom=' % (username, password)
    r = requests.get(url)
    if r.status_code == 200:
        m = re.findall('[0-9\.]{1,99} [GBM]{2} \([\.0-9 ]{0,99} GB\)', r.text)
        if len(m) > 2:
            print 'Total downloads: ' + m[0]
            print 'Total uploads:   ' + m[1]
            print 'Combined total:  ' + m[2]
            if show_graph:
                print re.findall('IMG SRC="[a-zA-Z0-9=\-&\.\?/]{1,500}"',
                            r.text)[0]
        else:
            print 'Unable to retrieve data.'
            return False
    else:
        print 'Error:', r.status_code, r.reason
        return False
    return True


if __name__ == '__main__':
    # replace the default for phone number and account number
    # if you don't want to pass them as arguments and aren't
    # concerned about anyone seeing them :)
    parser = argparse.ArgumentParser(
            description='View your Eircom broadband usage on the cli.')
    parser.add_argument('-p', '--phone-number',
            required=True, help='Phone number in this format - 555-1234567',
            default=None)
    parser.add_argument('-a', '--account-number',
            help='Account number', default=None)
    parser.add_argument('-g', '--graph-link', action='store_true',
            help='Show url to graph', default=False)
    options = parser.parse_args()

    if not options.account_number:
        options.account_number = getpass('Account number: ')

    if not get_stats(options.phone_number, options.account_number,
            options.graph_link):
        sys.exit(1)
