# -*- coding: utf-8 -*-
"""
unit tests covering most of the package’s functionality. 

@author: praneeth
"""

import pandas as pd
import numpy as np
import unittest
from datetime import datetime
from holidays import CountryHoliday
from pandas._testing import assert_frame_equal
import timesplitter

class TestTimeSplitter(unittest.TestCase):
    def setUp(self):
        data = {
            'datetime': [
                '2022-01-01 08:00:00',
                '2022-02-15 12:30:45',
                '2022-03-20 17:45:30',
                '2022-04-10 10:00:00',
                '2022-05-05 20:15:00',
                '2022-06-30 14:45:00',
                '2022-07-25 09:20:00',
                '2022-08-25 18:30:00',
                '2022-09-05 07:00:00',
                '2022-10-20 16:30:00',
                '2022-11-15 11:45:00',
                '2022-12-05 23:55:00',
                pd.NaT  # Wanted added a missing data value
            ]
        }
        self.df = pd.DataFrame(data)
        self.ts = timesplitter.TimeSplitter(self.df, 'datetime')

    def test_split_by_year(self):
        self.ts.split_by_year()
        self.assertIn('year', self.df.columns)
        self.assertTrue(self.df['year'].equals(pd.to_datetime(self.df['datetime']).dt.year))

    def test_split_by_month(self):
        self.ts.split_by_month()
        self.assertIn('month', self.df.columns)
        self.assertTrue(self.df['month'].equals(pd.to_datetime(self.df['datetime']).dt.month))

    def test_split_by_time(self):
        self.ts.split_by_time()
        self.assertIn('hour', self.df.columns)
        self.assertIn('minute', self.df.columns)
        self.assertIn('second', self.df.columns)


    def test_detect_holidays(self):
        # Testing detecting holidays
        holiday_df = self.ts.detect_holidays(country='US', include_holiday=True)
        # Ensuring holiday_df is not empty
        self.assertFalse(holiday_df.empty)
        #When include holiday is true we get only values which contains holidays in our 
        #df we have two holidays so we need to get len as 2
        self.assertEqual(len(holiday_df), 2)
        # Test excluding holidays
        non_holiday_df = self.ts.detect_holidays(country='US', include_holiday=False)
        # Ensure non_holiday_df does not contain holiday dates
        
        self.assertTrue(holiday_df.index.intersection(non_holiday_df.index).empty)
        self.assertEqual(len(non_holiday_df), 11)

    def test_handle_missing_data(self):
        # Test filling missing-data
        self.ts.handle_missing_data(method='fill', value=datetime(2022, 1, 1))
        # Ensure missing-values are filled
        self.assertFalse(self.df['datetime'].hasnans)
        # Test dropping missing-data
        self.ts.handle_missing_data(method='drop')
        # Ensure missing-values are dropped
        self.assertTrue(self.df['datetime'].notna().all())
        

    def test_calculate_relative_time(self):
        # Test calculating days
        self.ts.calculate_relative_time('days', 'days')
        self.assertIn('days', self.df.columns)
        # Test calculating months
        self.ts.calculate_relative_time('months', 'months')
        self.assertIn('months', self.df.columns)
        # Test calculating years
        self.ts.calculate_relative_time('years', 'years')
        self.assertIn('years', self.df.columns)

    def test_split_date_and_time(self):
        self.ts.split_date_and_time(date_col_name='date', time_col_name='time')
        self.assertIn('date', self.df.columns)
        self.assertIn('time', self.df.columns)

if __name__ == '__main__':
    unittest.main()
