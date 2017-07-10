# -*- coding: utf-8 -*-
"""
SGDQ 2017 Analysis
 from: gdqstat.us data provided by /u/micro_apple

@author: Kier Groulx (kgroulx@uci.edu)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# make this consistent
np.random.seed(42)

# analyze chatlogs when i think of goals / get better at nlp
#chatlog = pd.read_csv("gdq_chats.csv")
donations = pd.read_csv("gdq_donations.csv")

# start with donations analysis
donations.head()
len(pd.notnull(donations["donor_id"])) # total donations
donations["donor_id"].dropna().nunique()
# about 2x as many donations as donors
donations.info()
donations.describe()
# as we can see, the donations are heavily skewed by outliers, such as company sponsors (e.g. theyetee)
#  the actual average (median) as we can see here is only $25, far different from
#  the mean of $59

# who donated the most times?
donations["donor_id"].value_counts()
mvd = donations[donations["donor_id"] == 325092]
mvd

# get donor_ids that showed up multiple times
from collections import Counter
cnt = Counter(donations["donor_id"])
multipleDonors = [k for k in cnt if cnt[k] > 1]
len(multipleDonors)
# quick statistics:
    # 29734 donations
    # 21667 donors with identification
    # 15416 uniquely identifiable donors
    # 3026 donors with identification that donated more than once
    # 42 donations from donor with most donations
    
# is more money donated when a donation has a comment?
commented = donations[donations["has_comment"] == True]
commented.describe()    
# seems like yes, but the variance increases too.

# where are spikes in overall donation amount?
import matplotlib.dates as mdates
donations['timeDonated'] = pd.to_datetime(donations["created_at"])
donations['timeDonated'].head()
donations.plot(kind="scatter", x="timeDonated", y="amount", alpha=0.2)

    
# work on these after donations analysis
kill_save = pd.read_csv("gdq_kill_vs_save_animals.csv")
timeseries = pd.read_csv("gdq_timeseries.csv")
kill_save.head()
timeseries.head()