import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    days_list = ['saturday', 'sunday', 'monday', 'tuesday', 'thursday', 'wednesday', 'friday', 'all', 'none']
    months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                   'november', 'december', 'none', 'all']
    print ('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ("Enter the city that you want to filter(chicago, new york city, washington) or none \n").lower ()
    while city not in CITY_DATA.keys ():
        city = input (
            "(Invalid Error 404 {} doesn't exists ),Enter a valid City (chicago, new york city, washington)\n".format (
                city)).lower ()
    # get user input for month (all, january, february, ... , june)
    month = input ("Enter the month that you want to filter(all, january, february, ... , june) or none \n").lower ()
    while month not in months_list:
        month = input (
            "(Invalid Error 404 {} doesn't exists ),Enter a valid month from (all, january, february, ... , june) or none \n".format (
                month)).lower ()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("Enter the day that you want to filter (all, monday, tuesday, ... sunday) or none \n").lower ()
    while day not in days_list:
        day = input (
            "(Invalid Error 404 {} doesn't exists ),Enter a valid day from (all, monday, tuesday, ... sunday) or none \n".format (
                day)).lower ()
    print ('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv (CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime (df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index (month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title ()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print ('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time ()

    # display the most common month
    print ("The most common month is {}".format (df['month'].mode ()[0]))

    # display the most common day of week
    print ("The most common day is {}".format (df['day_of_week'].mode ()[0]))

    # display the most common start hour
    print ("The most common start hour is {}".format (df['Start Time'].mode ()[0]))

    print ("\nThis took %s seconds." % (time.time () - start_time))
    print ('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print ('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time ()

    # display most commonly used start station
    print ("The most common start station is {}".format (df['Start Station'].mode ()[0]))

    # display most commonly used end station
    print ("The most common end station is {}".format (df['End Station'].mode ()[0]))

    # display most frequent combination of start station and end station trip
    df2 = df['Start Station'] + df['End Station']
    print ("The most common combination of start station and end station is {} ".format (df2.mode ()[0]))

    print ("\nThis took %s seconds." % (time.time () - start_time))
    print ('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print ('\nCalculating Trip Duration...\n')
    start_time = time.time ()

    # display total travel time
    print ("total travel time is {}".format (df['Trip Duration'].sum ()))

    # display mean travel time
    print ("mean travel time is {}".format (df['Trip Duration'].mean ()))

    print ("\nThis took %s seconds." % (time.time () - start_time))
    print ('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print ('\nCalculating User Stats...\n')
    start_time = time.time ()

    # Display counts of user types
    print (df['User Type'].value_counts ())
    try:
        # Display counts of gender
        print (df['Gender'].value_counts ())
    except:
        print ("Sorry there are some missing data ,Gender column doesn't exist !")
        # Display earliest, most recent, and most common year of birth
    try:

        print ("earliest year of birth is {}".format (df['Birth Year'].dropna ().astype (int).min ()))
        print ("most recent year of birth is {}".format (df['Birth Year'].dropna ().astype (int).max ()))
        print ("most common year of birth is {}".format (df['Birth Year'].dropna ().astype (int).mode ()[0]))
    except:

        print ("Sorry there are some missing data ,Birth Year column doesn't exist !")
    print ("\nThis took %s seconds." % (time.time () - start_time))
    print ('-' * 40)


def main():
    while True:
        city, month, day = get_filters ()
        df = load_data (city, month, day)

        time_stats (df)
        station_stats (df)
        trip_duration_stats (df)
        user_stats (df)
        iteration = 5

        while True:
            raw = input ("would you like to see 5 lines of raw data ? \n").lower ()
            if raw == "no":
                break
            elif raw=="yes":
                print (df.head (iteration))
                iteration += 5
            else:
                print("please type only yes or no ")
        restart = input ('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower () != 'yes':
            break


if __name__ == "__main__":
    main ()
