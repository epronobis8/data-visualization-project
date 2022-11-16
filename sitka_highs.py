import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #next function, returns the next line in the file when passed the reader object. 
    #in prceeding list, we call next only once so we get the first line of the file, 
    #which containers the file headers

    # Get high tempatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        #pulling the data from index high which is the max temp column
        highs.append(high)

print(highs)

    #plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format Plot
ax.set_title("Daily high tempatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Tempature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()