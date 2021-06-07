import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#check if input user is correct
def check_input(input_str, input_type):
    while True:
        input_read=input(input_str)
        try:
            if input_read in ['chicago', 'new york city', 'washington'] and input_type == 1:
                break
            elif input_read in ['all','january', 'february', 'march', 'april', 'may', 'june'] and input_type == 2:
                break
            elif input_read in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday'] and input_read == 3:
                break
            else:
                if input_type == 1:
                    print('sorry, wrong city')
                if input_type == 2:
                    print ('sorry, wrong month')
                if input_type == 3:
                    print ('sorry, wrong day')
        except ValueError:
            print ('Sorry Input Error')
    return input_read         

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_input('chicago, new york or washington', 1)
    

    # get user input for month (all, january, february, ... , june)
    month = check_input(' which month? ', 2)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input ('which day?',3)


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['month'].mode()[0])
       
    # display the most common day of week
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['start station'].mode()[0])

    # display most commonly used end station
    print(df['end station'].mode()[0])

    # display most frequent combination of start station and end station trip
    combination_of_start_end = df.groupby(['start Station', 'end Station'])
    most_common_combination_station = combination_of_start_end.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of start station and end station trip:\n', most_common_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
      
        print(df['Gender'].value_counts())
        
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', most_common_year)
        
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:', most_recent_year)
        
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
