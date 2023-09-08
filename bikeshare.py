import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' }

month_dict = {'All': 0, 'Jan': 1, 'Feb': 2, 'Mar': 3, 
              'Apr': 4, 'May': 5, 'Jun': 6}

day_dict = {'All': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 
            'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}


def convert(seconds):
    """
    Converts seconds to days, hours, minutes and seconds
    Args:
        (str) seconds - seconds to convert
        
    Returns:
        (str) time_str - days, hours, minutes and seconds
    """
    # calculate the days
    days = int(seconds // (24 * 3600))
    
    # calculate the hours
    t = seconds % (24 * 3600)
    hours = int(t // 3600)

    # calculate the minutes
    t %= 3600
    minutes = int(t // 60)

    # calculate the seconds
    seconds = int(t % 60)
    
    # string whether day or days
    if days == 0:
        day_str = ''
    elif days == 1:
        day_str = str(days) + ' ' + 'day '
    elif days > 1:
        day_str = str(days) + ' ' + 'days '
    
    # string whether hour or hours
    if hours == 0:
        hrs_str = ''
    elif hours == 1:
        hrs_str = str(hours) + ' ' + 'hour '
    elif hours > 1:
        hrs_str = str(hours) + ' ' + 'hours '
    
    # string whether minute or minutes
    if minutes == 0:
        min_str = ''
    elif minutes == 1:
        min_str = str(minutes) + ' ' + 'minute '
    elif minutes > 1:
        min_str = str(minutes) + ' ' + 'minutes '

    # string whether second or seconds    
    if seconds == 0:
        sec_str = ''
    elif seconds == 1:
        sec_str = str(seconds) + ' ' + 'second'
    elif seconds > 1:
        sec_str = str(seconds) + ' ' + 'seconds'
    
    time_str = day_str + hrs_str + min_str +  sec_str
     
    return time_str


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). 
    city = ''
    city_list = ['Chicago', 'New York', 'Washington']
    while city.title() not in city_list:
        city = input("Would you like to see data for Chicago, New York or Washington? \nPlease enter the city name\n").title()    

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month.title() not in month_dict.keys():
        month = input("Which month or do you want to see all?\n"
                   "Please input {} \n" .format(str(month_dict.keys()).replace('dict_keys([', '').replace('])', ''))).title()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.title() not in day_dict.keys():
        day = input("Which day or do you want to see all?\n"
                "Please input {} \n" .format(str(day_dict.keys()).replace('dict_keys([', '').replace('])', ''))).title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data for the specified city
    raw_df = pd.read_csv(CITY_DATA[city.lower()])

    # know the month end date
    if month in ['Jan', 'Mar', 'May', 'Jul']:
        end_day = '-31'
    elif month in ['Apr', 'Jun']:
        end_day = '-30'
    elif month == 'Feb':
        end_day = '-28'

    #filter data by month
    if month == 'All':
        # No filter applied
        month_df = raw_df.copy()
    else:
        # filter applied
        date_start = '2017-0' + str(month_dict[month]) + '-01'
        date_end = '2017-0' + str(month_dict[month]) + end_day
        month_df = raw_df[(raw_df['Start Time'] >= date_start) & (raw_df['End Time'] <= date_end)] 

    #filter data by day
    if day == 'All':
        # No filter applied
        day_df = month_df.copy()
    else:
        # filter applied
        month_df['Start Time'] = pd.to_datetime(month_df['Start Time']).copy()
        day_df = month_df.loc[month_df['Start Time'].dt.weekday == day_dict[day]-1]

    df = day_df.copy()
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time']).copy()
    
    # display the most common month
    if month != 'All':
        print('Please note, you requested the month \'{}\' to analyze.' .format(month))
    else:
        common_month = df['Start Time'].dt.month_name().mode()[0]
        print('The most common month is', common_month)

    # display the most common day of week
    if day != 'All':
        print('Please note, you requested the day \'{}\' to analyze.' .format(day))
    else:
        common_day = df['Start Time'].dt.day_name().mode()[0]
        print('The most common day of the week is', common_day)

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is', common_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is', most_start_station)

    # display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is', most_end_station)

    # display most frequent combination of start station and end station trip
    most_start_end = df.groupby(['Start Station', 'End Station'])['Trip Duration'].count().idxmax()
    print('The most frequent combination of start station and end station trip is \n \'{}\' and \'{}\''
      .format(most_start_end[0], most_start_end[1]))
    
    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_secs = df['Trip Duration'].sum()
    #convert seconds to hours, minutes and seconds
    total_time = convert(total_secs)
    print('The total travel time is', total_time)

    # display mean travel time
    mean_secs = df['Trip Duration'].mean()
    #convert seconds to hours, minutes and seconds
    mean_time = convert(mean_secs)
    print('The mean travel time is', mean_time)

    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('-'*20)
    for i in range(len(user_type)):
        print('|{} - {}'.format(user_type.index[i], user_type[i]))
        print('-'*20)
    
    # Display counts of gender
    if city.lower() == 'washington':
        print('Please note that, the city selected, \'Washington\', \ndoes not have a Gender column for analysis.')
    else:
        gender_type = df['Gender'].value_counts()
        print('-'*15)
        for i in range(len(gender_type)):
            print('|{} - {}'.format(gender_type.index[i], gender_type[i]))
            print('-'*15)

    # Display earliest, most recent, and most common year of birth
    if city.lower() == 'washington':
        print('Please note that, the city selected, \'Washington\', \ndoes not have a Birth Year column for analysis.')
    else:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        recent_birth_year = str(int(df['Birth Year'].max()))
        common_birth_year = str(int(df['Birth Year'].mode()))
        print('The earliest year of birth is', earliest_birth_year)
        print('The most recent year of birth is', recent_birth_year)
        print('The most common year of birth is', common_birth_year)

    print("\nThis took %s seconds." % round((time.time() - start_time), 2))
    print('-'*40)


def display_data(df, city):
    """
    Displays 5 rows of raw data of a city
    Args:
        (df) df - the dataframe
        (str) city - name of the city to analyze
    Returns:
        Prints five rows of raw data
        
    """
    i = 0
    raw = input("Would you like to see the raw data for {}? Enter yes or no.\n" .format(city.title())).lower()
    
    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])
            raw = input('\nWould you like to see 5 more rows of the data? yes/no\n').lower()
            i += 5
        else:
            raw = input('Input valid. Please enter only \'yes\' or \'no\'')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() not in ['yes', 'no']:
            restart = input('Input valid. Please enter only \'yes\' or \'no\'\n')
            
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()