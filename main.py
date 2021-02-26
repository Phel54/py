import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import quandl
# Get attendees to get their own key.
quandl.ApiConfig.api_key = 'gYyp7CLTPWqhbsyFNAN2'

# Select a basket of stocks to work with. They can pick their own.
selected = ['CNP', 'F', 'WMT',  'GE', 'TSLA']

# Get the data from Quandl for these stock
data = quandl.get_table('WIKI/PRICES', ticker=selected,
                        qopts={ 'columns': ['ticker', 'date', 'adj_close']},
                        date ={ 'gte': '2014-1-1', 'lte': '2016-12-31'},
                        paginate=True)

# Check the data, what's it look like?
print(data.head(10))