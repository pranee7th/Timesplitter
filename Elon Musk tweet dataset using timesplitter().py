import pandas as pd
import timesplitter
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df2 = pd.read_csv(r'C:\Users\prane\OneDrive\Desktop\elon_musk_tweets.csv')

timesplitter = timesplitter.TimeSplitter(df=df2, datetime_column='date', date_format=None)

# Convert the 'date' column to datetime
df2['date'] = pd.to_datetime(df2['date'])

# Use the TimeSplitter class methods
# Split by year and calculate engagement trends
timesplitter.split_by_year()
yearly_engagement = df2.groupby('year')[['retweets', 'favorites']].mean()

# Plot yearly engagement trends
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_engagement)
plt.title('Yearly Engagement Trends')
plt.xlabel('Year')
plt.ylabel('Mean Engagement')
plt.legend(['Retweets', 'Favorites'])
plt.show()

# Spliting by month and calculate engagement trends
timesplitter.split_by_month()
monthly_engagement = df2.groupby('month')[['retweets', 'favorites']].mean()

# Ploting monthly engagement trends
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_engagement)
plt.title('Monthly Engagement Trends')
plt.xlabel('Month')
plt.ylabel('Mean Engagement')
plt.legend(['Retweets', 'Favorites'])
plt.show()

# Calculate tweet length
df2['tweet_length'] = df2['text'].apply(len)

# Analyze correlation between tweets len & engagement
corr_length_retweets, _ = pearsonr(df2['tweet_length'], df2['retweets'])
corr_length_favorites, _ = pearsonr(df2['tweet_length'], df2['favorites'])

print(f"Correlation between tweet length and retweets: {corr_length_retweets:.2f}")
print(f"Correlation between tweet length and favorites: {corr_length_favorites:.2f}")


'''  
The TimeSplitter class simplifies the process of analyzing time-based data by providing methods that allow you to split a dataset into different time intervals and calculate various insights based on these intervals. Here's how it can save you time and effort in your analysis:

Automated Time Splitting:
The TimeSplitter class provides methods like split_by_year, split_by_month, and split_by_time that automatically extract the respective time intervals (year, month, hour, etc.) from the given datetime column.
Without these methods, you would have to manually extract the time intervals from the datetime column using different pandas operations. This process could be error-prone and time-consuming, especially for large datasets.
Ease of Analysis:
By splitting the data into different time intervals, the class allows you to quickly group and aggregate data by the desired time interval.
For example, after using split_by_time, you can easily group the data by the hour column and calculate mean engagement for each hour. This would be more complex if the data were not split in this way.
Consistent and Accurate Processing:
By providing standardized methods for time-based data processing, the TimeSplitter class ensures consistency and accuracy in your data manipulation.
This means you can focus more on analyzing insights rather than worrying about data preprocessing steps, which could lead to inconsistencies or errors.
Flexibility:
The class is designed to be flexible, allowing you to work with different types of time-based data (e.g., years, months, hours) depending on your analysis needs.
This flexibility makes the class a useful tool for a variety of analyses, saving you time from having to write custom code for each different time-based analysis.
Improved Code Readability:
The methods provided by the TimeSplitter class help keep your code clean and readable.
This can save you time in debugging and maintaining your code, as you don't have to deal with complex and repetitive time-based data manipulation code.
Overall, the TimeSplitter class streamlines the process of splitting time-based data, making it easier and faster to analyze trends and patterns based on different time intervals. This allows you to spend more time interpreting insights and less time on data manipulation.
'''