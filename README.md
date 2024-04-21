What is TimeSplitter?

TimeSplitter is a Python package that provides a TimeSplitter class with various methods to handle datetime data effectively. It offers functionalities such as:

Automated Time Splitting: Easily split datetime data into different time intervals like year, month, and time (hour, minute, second).

Conversion of Timezones(convert_to_timezone): Hassle-free conversion of datetime columns to different timezones.

split_date_and_time : Split Date and time into seperate columns

Holiday Detection (detect_holidays): Identify holidays in datetime data based on specified countries.

Handling Missing Data: Convenient methods to handle missing data in datetime columns.

Visualization (plot_time_distribution): Visualize the distribution of datetime data and engagement trends over time.

calculate_relative_time: Calculate the specified time interval and store the result in a new column.



Files Overview

timesplitter.py: This is the main Python file containing the TimeSplitter class definition. 
It provides all the methods necessary for time manipulation and analysis, including splitting datetime data into different intervals, handling missing data, converting timezones, detecting holidays, and more.

Unit Testing.py: This file contains unit tests for the TimeSplitter class. These tests ensure that each method behaves as expected and produces the correct results. 

Elon_musk_tweets.csv: This CSV file contains a dataset of Elon Musk's tweets, which is used as a sample dataset to demonstrate the functionalities of the TimeSplitter class.
The dataset includes columns such as the tweet date, text, retweets, hastags and favorites.

Elon Musk tweet dataset using timesplitter().py: This Notebook provides examples of how to use the TimeSplitter class with the Elon Musk tweets dataset. 
It demonstrates how time splitter can be used to perform various time-based analyses, such as plotting engagement trends over different time intervals. 

Contribution

We welcome contributions from the community! Whether it's bug fixes, feature enhancements, or documentation improvements, your contributions help make TimeSplitter better for everyone. 
