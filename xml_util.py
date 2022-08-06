import bz2
import xml.etree.ElementTree as xml

import pandas as pd

# data conversions schema
conversions = [
    ('vendor',int),
    ('people',int),
    ('tip',float),
    ...
    ]

def iter_rides(file_name):
    with bz2.open(file_name,'rt') as fp:
        tree = xml.parse(fp)

    rides = tree.getroot()
    for elem in rides:
        record = {}
        for tag, func in conversion:
            text = elem.find(tag).text
            record[tag] = func(text)
        field record

def load_xml(file_name):
    records = iter_rides(file_name)
    return pd.DataFrame.from_records(records)

if __name__ == "__main__":
    df = load_xml('taxi.xml.bz2')
    print(df.dtypes)
    print(df.head())
