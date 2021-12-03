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
import numpy as np
warnings.simplefilter("ignore")


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
            year = files[file].split('_')[1].split('.')[0]  # Splitting year from filename to include as a column in dataframe
            df = files[file]
            df = pd.read_csv('data/' + file_name + '/' + files[file] + '', skiprows=2)
            df['Year'] = year
            indexNames = df[df['Location'] == 'Notes'].index[0]
            df = df.iloc[:indexNames - 1, :]    # Removing extra rows
            df.drop(df.index[df['Location'] == 'United States'], inplace=True)  # Dropping the total row
        elif file_name == 'unemployment':
            df = files[file]
            df = pd.read_excel('data/' + file_name + '/' + files[file] + '', skiprows=10, engine='openpyxl')
            indexNames = df[df['Year'] == 2021.0].index[0]
            df = df.iloc[:indexNames - 1, :]    # Dropping the rows containing data of year 2021 since we are
            # considering previous 10 years data (2011-2020)
            df = df[['Year', 'unemployment']]   # Filtering the requried columns

        elif file_name == 'hatecrime':
            df = files[file]
            df = pd.read_csv('data/' + file_name + '/' + files[file] + '')
            startIndex = df[df['DATA_YEAR'] == 2011].index[0]
            df = df.iloc[startIndex:, :]    # Removing rows with year earlier than 2011
            hatecrime_drop_columns = ['INCIDENT_ID', 'ORI', 'PUB_AGENCY_NAME', 'PUB_AGENCY_UNIT', 'DIVISION_NAME',
                                      'POPULATION_GROUP_CODE', 'POPULATION_GROUP_DESC', 'INCIDENT_DATE',
                                      'ADULT_VICTIM_COUNT',
                                      'JUVENILE_VICTIM_COUNT', 'JUVENILE_OFFENDER_COUNT', 'TOTAL_OFFENDER_COUNT',
                                      'ADULT_OFFENDER_COUNT', 'JUVENILE_OFFENDER_COUNT', 'OFFENSE_NAME',
                                      'TOTAL_INDIVIDUAL_VICTIMS',
                                      'LOCATION_NAME', 'VICTIM_TYPES', 'MULTIPLE_OFFENSE', 'MULTIPLE_BIAS']

            df = df.drop(hatecrime_drop_columns, axis=1)    # Dropping columns which are not required

            hatecrime_filter_df = df[['DATA_YEAR', 'STATE_NAME', 'REGION_NAME', 'OFFENDER_RACE', 'VICTIM_COUNT']]
        else:
            pass
    all_df.append(df)
    dfs = pd.concat(all_df)
    all_df.clear()
    return dfs

if __name__ == '__main__':

    # Reading data from the folder
    unemployment_df = get_data('unemployment')
    population_df = get_data('population')
    hatecrime_df = get_data('hatecrime')