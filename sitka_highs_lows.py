import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #next function, returns the next line in the file when passed the reader object. 
    #in prceeding list, we call next only once so we get the first line of the file, 
    #which containers the file headers

    # Get dates & high tempatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        #pulling the data from index high which is the max temp column
        highs.append(high)
        lows.append(low)

print(highs)

#plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
#plot the high values to red points
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, high, lows, facecolor='blue', alpha=0.1)

# Format Plot
ax.set_title("Daily high and low tempatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Tempature (F)", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()