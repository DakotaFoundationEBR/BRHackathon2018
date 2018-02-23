# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

client = Socrata("data.brla.gov",
                  "yuigJiO02Y9CqY6NElnmQC74D",
                  username="dakota@foundationebr.org",
                  password="248202Db*")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("4w4d-4es6", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
df1 = results_df.loc[results_df['inci_type'] == '600']
df2 = results_df.loc[results_df['inci_type'] != '600']