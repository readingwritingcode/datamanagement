# common datetime problems

# source code: https://github.com/BindiChen/machine-learning/tree/main/data-analysis/008-pandas-datetime

# convert string to datetime
df = pd.DataFrame({'date': ['3/10/2000', '3/11/2000', '3/12/2000'],
                   'value': [2, 3, 4]})

df['date'] = pd.to_datetime(df['date']) # this will parse string with month first (MM/DD, MM DD, or MM-DD) 
                                        # If you would like Pandas to consider day first instead of month,
                                        # you can set the argument dayfirst to True.

# customize format
df = pd.DataFrame({'date': ['2016-6-10 20:30:0', 
                            '2016-7-1 19:45:30', 
                            '2013-10-12 4:5:1'],
                   'value': [2, 3, 4]})
df['date'] = pd.to_datetime(df['date'], format="%Y-%d-%m %H:%M:%S")
df

    # Speed up parsing with infer_datetime_format
    # Make up 3000 rows
df = pd.DataFrame({'date': ['3/11/2000', '3/12/2000', '3/13/2000'] * 1000 })

%timeit pd.to_datetime(df['date'], infer_datetime_format=True)
100 loops, best of 3: 10.4 ms per loop

%timeit pd.to_datetime(df['date'], infer_datetime_format=False)
1 loop, best of 3: 471 ms per loop

    # Handle parsing error
df = pd.DataFrame({'date': ['3/10/2000', 'a/11/2000', '3/12/2000'],
                   'value': [2, 3, 4]})
df['date'] = pd.to_datetime(df['date'])

df['date'] = pd.to_datetime(df['date'], errors='ignore')
    # or
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df
    
    # -> 4 tricks you should know to parse date columns with Pandas read_csv()
        # 1. select a column as date index
df = pd.read_csv('data/data_3.csv', parse_dates=['date'])
df.info()
        # 2. datetime format with day firts
pd.read_csv('data/data_1.csv', 
            parse_dates=['date'], 
            dayfirst=True)
       # 3. assemble multiple columns in one datetime
year,month,day,product,price
2019,1,1,A,10
2019,1,2,B,20
2019,1,3,C,30
2019,1,4,D,40

df = pd.read_csv('data/data_4.csv',
                 parse_dates=[['year', 'month', 'day']])

    # 4. customize datetime format advance
from datetime import datetime

custom_date_parser = lambda x: datetime.strptime(x, "%Y-%d-%m %H:%M:%S")

df = pd.read_csv('data/data_6.csv',
                 parse_dates=['date'],
                date_parser=custom_date_parser)

# assemble a datetime from multiple columns
df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5]})df['date'] = pd.to_datetime(df)
df

# get year, month and day
df = pd.DataFrame({'name': ['Tom', 'Andy', 'Lucas'],
                   'DoB': ['08-05-1997', '04-28-1996', '12-16-1995']})
df['DoB'] = pd.to_datetime(df['DoB'])

df['year']= df['DoB'].dt.year
df['month']= df['DoB'].dt.month
df['day']= df['DoB'].dt.day
df

# get the week of year, the day of the week, and leep year
df['week_of_year'] = df['DoB'].dt.week
df['day_of_week'] = df['DoB'].dt.dayofweek
df['is_leap_year'] = df['DoB'].dt.is_leap_year
df

    # mapping
dw_mapping={
    0: 'Monday', 
    1: 'Tuesday', 
    2: 'Wednesday', 
    3: 'Thursday', 
    4: 'Friday',
    5: 'Saturday', 
    6: 'Sunday'
} 
df['day_of_week_name']=df['DoB'].dt.weekday.map(dw_mapping)

# get the age from the date of birth -> !#!#!#!# get the periods of capital
today = pd.to_datetime('today')
df['age'] = today.year - df['DoB'].dt.year

# improve performance by setting date column as the index
df = pd.read_csv('data/city_sales.csv',parse_dates=['date'])
df.info()

    # set the column as the index
df = df.set_index(['date'])
df

# select  data with a specific year and perform aggregation
df.loc['2018']
df.loc['2018','num'].sum()

    # Get the total num for each city in 2018

df['2018'].groupby('city').sum()

# select data with a specific month and a specific day of the month
df.loc['2018-5']

# select data between two dates
df.loc['2016' : '2018']

df.loc['2018-5-2 10' : '2018-5-2 11' ]

df.between_time('10:30','10:45')

# handle missing values
df['rolling_sum'] = df.rolling(3).sum()
df.head()

df['rolling_sum_backfilled'] = df['rolling_sum'].fillna(method='backfill')
df.head()
