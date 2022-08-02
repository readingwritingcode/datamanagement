#!/usr/bin/python3

'''load and convert data from csv file using python built-in csv module'''
import bz2
import csv
from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'src dest convert')

def parse_timestamp(text):
    return datetime.strptime(text,"%Y-%m-%d %H:%M:%S")

columns = [
    Column('VendorID','vendor_id',int),
    ...,
    ]

def iter_records(file_name):
    with bz2.open(file_name,'rt') as fp:
        reader = csv.DicReader(fp)
        for csv_record in reader:
            record = {}
            for col in columns:
                value = csv_record[col.src]
                record[col.dest] = col.convert(value)
            yield record

def example():
    from pprint import pprint

    for i,record in enumerate(iter_records('taxi.csv.bz2')):
        if i >= 10:
            break
        ppritn(record)
