import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'all': 0,
              'january': 1,
              'febuary': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6,
              'july': 7,
              'august': 8,
              'september': 9,
              'october': 10,
              'november': 11,
              'december': 12}

WEEK_DATA = {'all': 0,
             'sunday': 1,
             'monday': 2,
             'tuesday': 3,
             'wednesday': 4,
             'thursday': 5,
             'friday': 6,
             'saturday': 7}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the city you want to look at: ').lower()
    # verify that the city is a valid choice
    while city not in CITY_DATA.keys():
        print('Not a valid choice please enter (Chicago, New York City, Washington)')
        city = input('Please enter the city you want to look at: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter the month (eg. all, january, february): ').lower()
    while month not in MONTH_DATA.keys():
        print('Not a valid choice please try again')
        month = input('Enter the month (eg. all, january, february): ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of the week (all, monday, tuesday, etc): ').lower()
    while day not in WEEK_DATA.keys():
        print('Not a valid choice please try again')
        day = input('Enter the day of the week (all, monday, tuesday, etc): ').lower()

    print('-'*40)
    return city, month, day


def clean_data(df):
    """ This will clean the data as needed 
    Args:
        (df) dataframe - The dataframe of data"""

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Make the Birth Year into an int instead of a float
    try:
        df['Birth Year'] = df['Birth Year'].fillna(0)
        df['Birth Year'] = df['Birth Year'].astype(int)
    except:
        pass
    
    return df


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
    df = pd.read_csv(CITY_DATA[city])
    
    df = clean_data(df)

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_index = MONTH_DATA[month]
        # filter by month to create the new dataframe
        df = df[df['month'] == month_index]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def print_most_common_data(key, value):
    """ Prints out a Most common message """
    print("The most common {} is {}".format(key, value)

          
def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (df) dataframe - The dataframe of data
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
#     common_month_index = df['month'].mode()[0]
#     month_list = list(MONTH_DATA.keys())
#     month_index_list = list(MONTH_DATA.values())
#     ind = month_index_list.index(common_month_index)

    try:
        print('The most common month is {}'.format(df['month'].mode()[0].title()))
    except:
        pass
    
    # TO DO: display the most common day of week
    try:
        common_day_of_week = df['day_of_week'].mode()[0]
    except:
        common_day_of_week = 'None'
        
    print_most_common_data('week', common_day_of_week)
    # TO DO: display the most common start hour
    try:
        df['start_hour'] = df['Start Time'].dt.hour
        common_start_hour = df['start_hour'].mode()[0]
    except:
        common_start_hour = 'None'
          
    print_most_common_data('Start Hour', common_start_hour)    
    
    try:
        common_end_hour = df['End Time'].dt.hour.mode()[0]
    except:
        common_end_hour = 'None'
    print_most_common_data('End Hour', common_start_hour)    

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
    
def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (df) dataframe - The dataframe of data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station is {}.'.format(common_start_station))
                           
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common Start Station is {}.'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    station_combo = (df['Start Station'] + " --> " + df['End Station']).mode()[0]
    print('The most common Start --> End Station Combo is {}.'.format(station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        (df) dataframe - The dataframe of data
    """
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   
    # TO DO: display total travel time
    # TODO: Make this display the hours
    
    print('The total travel time is {:.0f} secs'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is {:.1f} secs'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    
    Args:
        (df) dataframe - The dataframe of data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = dict(df['User Type'].value_counts())

    for user, value in user_types.items():
        print('{} users where {} '.format(value, user))
    # TO DO: Display counts of gender
    try:
       gender_counts = dict(df['Gender'].value_counts())
       for gender, value in gender_counts.items():
           print('{} users where {}'.format(value, gender))
    except:
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest Bith Year is {}'.format(df[df['Birth Year'] > 0]['Birth Year'].min()))
        print('The most recent Birth Year is {}'.format(df[df['Birth Year'] > 0]['Birth Year'].max()))
        print('The most common Birth Year is {}'.format(df[df['Birth Year'] > 0]['Birth Year'].mode()[0]))
    except:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_raw_data(df):
    """ Display the raw data 5 rows at a time"""
    i = 5
    while i < df.shape[0]:
       print(df.iloc[i-5: i])
       i += 5
       exit = input('Want to see 5 more lines? (yes or no): ')
       if exit == 'no' or exit == 'n':
           break
       


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data = input('\nWould you like to see the raw data? Enter yes or no: ')
        if display_data.lower() == 'yes':
            display_raw_data(df)
                             
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
