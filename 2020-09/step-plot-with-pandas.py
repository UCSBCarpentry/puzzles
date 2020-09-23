import pandas
import matplotlib.pyplot

# read the data into a pandas data frame with the time column as a date object rather than a string
building_df = pandas.read_csv('clean.csv', parse_dates=['time'])

# make a plot of the step style
building_df.plot(x="time", y=["count"], drawstyle='steps')

# show the plot
matplotlib.pyplot.show()
