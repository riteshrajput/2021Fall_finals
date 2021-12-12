"""
Visualization functions for datasets of the project
"""

# Libraries
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
sns.set()


def visualize_population(population_dataframe):
    """
    Function to plot charts for population dataset
    :param population_dataframe: Population dataframe
    :return: Bar plot for different race vs state
    """
    population_dataframe['Asian %'] = (population_dataframe['Asian'] / population_dataframe['Total']) * 100
    population_dataframe['Black %'] = (population_dataframe['Black'] / population_dataframe['Total']) * 100
    population_dataframe['White %'] = (population_dataframe['White'] / population_dataframe['Total']) * 100
    population_dataframe['Hispanic %'] = (population_dataframe['Hispanic'] / population_dataframe['Total']) * 100

    fig, axes = plt.subplots(2, 2, figsize=(25, 30))
    axes = axes.flatten()

    asian_state = sns.barplot(x='Asian %', y='Location', data=population_dataframe, ax=axes[0])
    asian_state.bar_label(asian_state.containers[0])

    black_state = sns.barplot(x='Black %', y='Location', data=population_dataframe, ax=axes[1])
    black_state.bar_label(black_state.containers[0])

    white_state = sns.barplot(x='White %', y='Location', data=population_dataframe, ax=axes[2])
    white_state.bar_label(white_state.containers[0])

    hispanic_state = sns.barplot(x='Hispanic %', y='Location', data=population_dataframe, ax=axes[3])
    hispanic_state.bar_label(hispanic_state.containers[0])

    plt.suptitle("POPULATION RATE IN USA")
    plt.show()
    return plt


def visualize_hatecrime(hatecrime_dataframe, column_name):
    """
    Function to plot charts for hatecrime dataset
    :param hatecrime_dataframe: hatecrime dataframe
    :param column_name: Name of the column for the chart
    :return: Bar plot of the requested column name
    """
    if column_name == 'offender race':
        plt.figure(figsize=(20, 10))
        hatecrime_dataframe['OFFENDER_RACE_COUNT'] = hatecrime_dataframe.groupby('OFFENDER_RACE')[
            'OFFENDER_RACE'].transform('count')
        ax = sns.barplot(x="OFFENDER_RACE_COUNT", y="OFFENDER_RACE", data=hatecrime_dataframe)
        ax.set(xlabel='OFFENDER RACE COUNT', ylabel='OFFENDER RACE')
        ax.bar_label(ax.containers[0])
        plt.title('OFFENDER RACE')
        plt.grid(True)

    elif column_name == 'victim count':
        hatecrime_dataframe['VICTIMS COUNT'] = hatecrime_dataframe.groupby('DATA_YEAR')['VICTIM_COUNT'].transform(
            'count')

        plt.figure(figsize=(20, 10))
        ax = sns.lineplot(x="DATA_YEAR", y="VICTIMS COUNT", data=hatecrime_dataframe)
        ax.set(xlabel='YEAR', ylabel='VICTIMS COUNT"')
        plt.title('NUMBERS OF VICTIM OVER THE YEARS')
        plt.grid(True)

    elif column_name == 'anti-asian':
        hatecrime_dataframe_as = hatecrime_dataframe[['DATA_YEAR', 'BIAS_DESC', 'VICTIM_COUNT']]
        hatecrime_dataframe_as = hatecrime_dataframe_as[hatecrime_dataframe_as['BIAS_DESC'] == 'Anti-Asian']
        hatecrime_dataframe_as = hatecrime_dataframe_as.groupby(['DATA_YEAR','BIAS_DESC'], as_index=False)['VICTIM_COUNT'].sum()

        plt.figure(figsize=(20, 10))
        ax = sns.lineplot(x="DATA_YEAR", y="VICTIM_COUNT", data=hatecrime_dataframe_as)
        ax.set(xlabel='YEAR', ylabel='Anti-Asian Victim Count')
        plt.title('NUMBERS OF ANTI-ASIAN VICTIM OVER THE YEARS')
        plt.grid(True)
        plt.show()
    return plt


def visualize_unemployment(unemployment_dataframe):
    """
    Function to plot charts for unemployment dataset
    :param unemployment_dataframe: Unemployment dataframe
    :return: Bar plot of unemployment vs year
    """
    unemployment_dataframe['unemployment %'] = unemployment_dataframe['unemployment'] / unemployment_dataframe[
        'unemployment'].sum() * 100
    plt.figure(figsize=(20, 10))
    sns.barplot(x="Year", y="unemployment %", data=unemployment_dataframe)
    plt.title("Unemployment Rate")
    plt.grid(True)
    plt.show()
    return plt


def visualize_hatecrime_unemployment(hatecrime_unemployment_dataframe):
    """
    Function to plot data of merged dataset (hatecrime and unemployment)
    :param hatecrime_unemployment_dataframe: Merged dataset of hatecrime and unemployment
    :return: Bar plot of the unemployment rate, victims count, offender race count Vs State
    """
    fig, axes = plt.subplots(1, 2, figsize=(50, 25))
    axes = axes.flatten()

    unemployment_state = sns.barplot(x='unemployment %', y='state',
                                     data=hatecrime_unemployment_dataframe, ax=axes[0])
    unemployment_state.bar_label(unemployment_state.containers[0])

    hatecrime_unemployment_dataframe = hatecrime_unemployment_dataframe[hatecrime_unemployment_dataframe['BIAS_DESC'] == 'Anti-Asian']

    ue_victims_count_state = sns.barplot(x='VICTIMS COUNT', y='state',
                                         data=hatecrime_unemployment_dataframe, ax=axes[1])
    ue_victims_count_state.bar_label(ue_victims_count_state.containers[0])

    plt.show()
    return plt


def visualize_hatecrime_population(hatecrime_population_dataframe, race):
    """
    Function to plot data of merged dataset (hatecrime and population)
    :param hatecrime_population_dataframe: Merged dataset of hatecrime and population
    :return: Bar plot of the different state, victims count, offender race count Vs State
    """
    fig, axes = plt.subplots(1, 2, figsize=(50, 25))
    axes = axes.flatten()

    if race == 'asian':
        race_state = sns.barplot(x='Asian %', y='STATE_NAME',
                                 data=hatecrime_population_dataframe, ax=axes[0])
        race_state.bar_label(race_state.containers[0])

    elif race == 'black':
        race_state = sns.barplot(x='Black %', y='STATE_NAME',
                                 data=hatecrime_population_dataframe, ax=axes[0])
        race_state.bar_label(race_state.containers[0])

    elif race == 'hispanic':
        race_state = sns.barplot(x='Hispanic %', y='STATE_NAME',
                                 data=hatecrime_population_dataframe, ax=axes[0])
        race_state.bar_label(race_state.containers[0])

    elif race == 'white':
        race_state = sns.barplot(x='White %', y='STATE_NAME',
                                 data=hatecrime_population_dataframe, ax=axes[0])
        race_state.bar_label(race_state.containers[0])

    hatecrime_population_dataframe = hatecrime_population_dataframe[hatecrime_population_dataframe['BIAS_DESC'] == 'Anti-Asian']

    po_victims_count_state = sns.barplot(x='VICTIMS COUNT', y='STATE_NAME',
                                         data=hatecrime_population_dataframe, ax=axes[1])
    po_victims_count_state.bar_label(po_victims_count_state.containers[0])

    plt.show()
    return plt
