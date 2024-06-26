# -*- coding: utf-8 -*-
"""Timesplitter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y38erEbHA-IPGc2_9N2Lg3B2KmleDJPv
"""
import pandas as pd
import holidays

class TimeSplitter:
    def __init__(self, df, datetime_column, date_format=None, timezone=None):
        """
        Initializes the TimeSplitter class.

        Parameters:
        df (pd.DataFrame): The DataFrame containing datetime data.
        datetime_column (str): The column in the DataFrame containing datetime values.
        date_format (str, optional): The format of the datetime values. Defaults to None.
        timezone (str, optional): The timezone of the datetime values. Defaults to None.
        """
        self.df = df
        self.datetime_column = datetime_column
        self.date_format = date_format
        self.timezone = timezone

    def split_by_year(self):
        """
        Splits the DataFrame by year.

        Parameters:
        None

        Returns:
        None
        """
        self.df['year'] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format).dt.year

    def split_by_month(self):
        """
        Splits the DataFrame by month.

        Parameters:
        None

        Returns:
        None
        """
        self.df['month'] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format).dt.month

    def split_by_time(self):
        """
        Splits the DataFrame by time (hour, minute, second).

        Parameters:
        None

        Returns:
        None
        """
        self.df['hour'] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format).dt.hour
        self.df['minute'] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format).dt.minute
        self.df['second'] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format).dt.second

    def plot_time_distribution(self):
        """
        Plots the distribution of datetime data in the DataFrame.

        Parameters:
        None

        Returns:
        None
        """
        self.df[self.datetime_column] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format)
        self.df = self.df.dropna(subset=[self.datetime_column])

        plt.figure(figsize=(10, 6))
        sns.histplot(
            data=self.df,
            x=self.datetime_column,
            kde=True,
            element="step"
        )
        plt.xlabel('Datetime', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.title('Time Distribution', fontsize=14)
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)
        plt.show()

    def convert_to_timezone(self, target_timezone):
        """
        Converts the datetime column to the specified target timezone.

        Parameters:
        target_timezone (str): The target timezone to convert the datetime column to.

        Returns:
        None
        """
        self.df[self.datetime_column] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format)
        if self.timezone:
            self.df[self.datetime_column].dt.tz_localize(self.timezone, nonexistent='NaT', ambiguous='NaT')
        self.df[self.datetime_column].dt.tz_convert(target_timezone)

    def detect_holidays(self, country='US', include_holiday=True):
        """
        Detects holidays in the datetime column based on the specified country.

        Parameters:
        country (str, optional): The country to check holidays for. Defaults to 'US'.
        include_holiday (bool, optional): Whether to include or exclude holiday records. Defaults to True.

        Returns:
        pd.DataFrame: The DataFrame filtered based on holiday detection.
        """
        holidays_country = holidays.CountryHoliday(country)
        self.df[self.datetime_column] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format)
        holiday_mask = self.df[self.datetime_column].apply(lambda x: x in holidays_country)

        if include_holiday:
            return self.df[holiday_mask]
        else:
            return self.df[~holiday_mask]

    def handle_missing_data(self, method='fill', value=None):
        """
        Handles missing data in the datetime column based on the specified method.

        Parameters:
        method (str, optional): The method for handling missing data ('fill' or 'drop'). Defaults to 'fill'.
        value (any, optional): The value to fill missing data with if method is 'fill'. Defaults to None.

        Returns:
        None
        """
        if method == 'fill':
            self.df[self.datetime_column].fillna(value, inplace=True)
        elif method == 'drop':
            self.df.dropna(subset=[self.datetime_column], inplace=True)
        else:
            raise ValueError("Invalid missing data handling method. Choose 'fill' or 'drop'.")

    def calculate_relative_time(self, time_interval, new_column_name):
        """
        Calculates the specified time interval and stores the result in a new column.

        Parameters:
        time_interval (str): The time interval to calculate ('days', 'months', 'years').
        new_column_name (str): The name of the new column to store the calculated time interval.

        Returns:
        None
        """
        self.df[self.datetime_column] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format)

        if time_interval == 'days':
            self.df[new_column_name] = self.df[self.datetime_column].dt.day
        elif time_interval == 'months':
            self.df[new_column_name] = self.df[self.datetime_column].dt.month
        elif time_interval == 'years':
            self.df[new_column_name] = self.df[self.datetime_column].dt.year
        else:
            raise ValueError("Invalid time interval. Choose 'days', 'months', or 'years'.")

    def split_date_and_time(self, date_col_name='date', time_col_name='time'):
        """
        Splits the datetime column into separate date and time columns.

        Parameters:
        date_col_name (str, optional): The name of the new date column. Defaults to 'date'.
        time_col_name (str, optional): The name of the new time column. Defaults to 'time'.

        Returns:
        None
        """
        self.df[self.datetime_column] = pd.to_datetime(self.df[self.datetime_column], format=self.date_format)
        self.df[date_col_name] = self.df[self.datetime_column].dt.date
        self.df[time_col_name] = self.df[self.datetime_column].dt.time
