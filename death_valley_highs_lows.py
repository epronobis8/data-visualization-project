import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        #if data is found missing it'll print an error and keep going through the loop.
        except ValueError:
            print(f"Missing data for {current_date}")
        #this will print out the data, even if values are missing.
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
#plot the high values to red points
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, high, lows, facecolor='blue', alpha=0.1)

# Format Plot
title = "Daily high and low tempatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Tempature (F)", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
