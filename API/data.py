"""
Reads in data from csv into pandas dataframes
"""


import pandas as pd
import glob


# read all csv data into a python dictionary

preds = {}

for filename in glob.glob('data-production/*.csv'):
    if "predictions" in filename:
        preds[filename[28:-4]] = pd.read_csv(filename,
                                            header=0,
                                            index_col='player',
                                            names=['player', 'first', 'last', 'name', 'position', 'week-cur',
                                                   'week-pred', 'week-act', 'week-diff', 'week-pct', 'rank-cur',
                                                   'rank-pred', 'rank-act'])
