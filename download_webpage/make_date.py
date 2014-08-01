#! /usr/bin/env python
# make_date.py
# David Prager Branner
# 20140801

"""Construct a date-time string."""

import datetime

def make_date():
    date_and_time = datetime.datetime.today()
    return date_and_time.strftime('%Y%m%d-%H%M')

