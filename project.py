"""
IS 597: Final Project
Project: Analysis of Hate Crimes during COVID-19 Pandemic
Python version: 3.9
@author: (1) Ritesh Rajput | riteshr2@illinois.edu
         (2) Nishit Singh | ns1601@illinois.edu
"""
# Libraries
import os
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

warnings.simplefilter("ignore")
plt.style.use('seaborn-whitegrid')
sns.set()
pd.set_option('display.max_columns', None)


def get_data(file_name, all_df=[]):
    """
    Function to read the data files, create a concatenated dataframe
    :param file_name: Name of the the folder to read
    :param all_df: Initializing list to collect all dataframe created
    :return: Concatenated dataframe
    """
    files = os.listdir('./data/' + file_name + '')  # Files available in the directory
    print(files)
    for file in range(len(files)):
        if file_name == 'population':  # Reading all files from folder named "population"
            year = files[file].split('_')[1].split('.')[
                0]  # Splitting year from filename to include as a column in dataframe
            df = files[file]
            df = pd.read_csv('data/' + file_name + '/' + files[file] + '', skiprows=2)
            df['Year'] = year
            indexNames = df[df['Location'] == 'Notes'].index[0]
            df = df.iloc[:indexNames - 1, :]  # Removing extra rows
            df.drop(df.index[df['Location'] == 'United States'], inplace=True)  # Dropping the total row
        elif file_name == 'unemployment':
            df = files[file]
            df = pd.read_excel('data/' + file_name + '/' + files[file] + '', skiprows=10, engine='openpyxl')
            indexNames = df[df['Year'] == 2021.0].index[0]
            df = df.iloc[:indexNames - 1, :]  # Dropping the rows containing data of year 2021 since we are
            # considering previous 10 years data (2011-2020)
            df = df[['Year', 'unemployment']]  # Filtering the requried columns

        elif file_name == 'hatecrime':
            df = files[file]
            df = pd.read_csv('data/' + file_name + '/' + files[file] + '')
            startIndex = df[df['DATA_YEAR'] == 2011].index[0]
            df = df.iloc[startIndex:, :]  # Removing rows with year earlier than 2011
            hatecrime_drop_columns = ['INCIDENT_ID', 'ORI', 'PUB_AGENCY_NAME', 'PUB_AGENCY_UNIT', 'DIVISION_NAME',
                                      'POPULATION_GROUP_CODE', 'POPULATION_GROUP_DESC', 'INCIDENT_DATE',
                                      'ADULT_VICTIM_COUNT',
                                      'JUVENILE_VICTIM_COUNT', 'JUVENILE_OFFENDER_COUNT', 'TOTAL_OFFENDER_COUNT',
                                      'ADULT_OFFENDER_COUNT', 'JUVENILE_OFFENDER_COUNT', 'OFFENSE_NAME',
                                      'TOTAL_INDIVIDUAL_VICTIMS',
                                      'LOCATION_NAME', 'VICTIM_TYPES', 'MULTIPLE_OFFENSE', 'MULTIPLE_BIAS']

            df = df.drop(hatecrime_drop_columns, axis=1)  # Dropping columns which are not required

            df = df[['DATA_YEAR', 'STATE_NAME', 'REGION_NAME', 'OFFENDER_RACE', 'VICTIM_COUNT']]
        else:
            pass
    all_df.append(df)
    dfs = pd.concat(all_df)
    all_df.clear()
    return dfs


if __name__ == '__main__':
    # Reading data
    unemployment_df = get_data('unemployment')
    population_df = get_data('population')
    hatecrime_df = get_data('hatecrime')

    print(hatecrime_df.head())
    # Population plot - Seaborn - Different Races
    population_df['Asian %'] = (population_df['Asian'] / population_df['Total']) * 100
    population_df['Black %'] = (population_df['Black'] / population_df['Total']) * 100
    population_df['White %'] = (population_df['White'] / population_df['Total']) * 100
    population_df['Hispanic %'] = (population_df['Hispanic'] / population_df['Total']) * 100

    fig, axes = plt.subplots(2, 2, figsize=(18, 21))
    axes = axes.flatten()
    sns.barplot(x='Asian %', y='Location', data=population_df, ax=axes[0])
    sns.barplot(x='Black %', y='Location', data=population_df, ax=axes[1])
    sns.barplot(x='White %', y='Location', data=population_df, ax=axes[2])
    sns.barplot(x='Hispanic %', y='Location', data=population_df, ax=axes[3])
    # axes[0].set_title("Asian")
    # axes[1].set_title("Black")
    plt.suptitle("Population Rate")
    plt.show()

    # Unemployment plot - Seaborn
    plt.figure(figsize=(15, 10))
    unemployment_df['unemployment %'] = unemployment_df['unemployment'] / unemployment_df['unemployment'].sum() * 100
    sns.barplot(x="Year", y="unemployment %", data=unemployment_df)
    plt.title('Unemployment Rate')
    plt.grid(True)
    plt.show()

    # Hatecrime plot - Seaborn
    plt.figure(figsize=(20, 10))
    # hatecrime_df_2020 = hatecrime_df[hatecrime_df['DATA_YEAR'] == 2020]
    hatecrime_df['OFFENDER_RACE_COUNT'] = hatecrime_df.groupby('OFFENDER_RACE')['OFFENDER_RACE'].transform('count')
    sns.barplot(x="OFFENDER_RACE_COUNT", y="OFFENDER_RACE", data=hatecrime_df)
    plt.title('Offender Race')
    plt.grid(True)
    plt.show()

    # Hatecrime plot - Seaborn - Victim
    plt.figure(figsize=(15, 10))
    hatecrime_df['VICTIMS COUNT'] = hatecrime_df.groupby('DATA_YEAR')['VICTIM_COUNT'].transform('count')
    sns.barplot(x="DATA_YEAR", y="VICTIMS COUNT", data=hatecrime_df)
    plt.title('VICTIM COUNT')
    plt.grid(True)
    plt.show()

    # # Population plot - Seaborn - Asian
    # plt.figure(figsize=(12, 15))
    # population_df['Asian %'] = (population_df['Asian'] / population_df['Total']) * 100
    # sns.barplot(x="Asian %", y="Location", data=population_df, orient='h')
    # plt.show()
    #
    # # Population plot - Matplotlib
    # plt.figure(figsize=(20, 20))
    # population_df['Asian_percent'] = (population_df['Asian'] / population_df['Total']) * 100
    # plt.xlabel('Population %')
    # plt.ylabel('Location')
    # plt.title('Population Rate')
    # plt.grid(True)
    # plt.barh(population_df['Location'], population_df['Asian_percent'])
    # plt.show()
    #
    # # Unemployment plot
    # unemployment_df['unemployment_%'] = unemployment_df['unemployment'] / unemployment_df['unemployment'].sum() * 100
    # plt.bar(unemployment_df['Year'], unemployment_df['unemployment_%'])
    # plt.xlabel('Year')
    # plt.ylabel('Unemployment %')
    # plt.title('Unemployment Rate')
    # plt.grid(True)
    # plt.show()
