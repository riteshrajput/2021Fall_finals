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

    ax = sns.barplot(x='Asian %', y='Location', data=population_dataframe, ax=axes[0])
    ax.bar_label(ax.containers[0])

    ax = sns.barplot(x='Black %', y='Location', data=population_dataframe, ax=axes[1])
    ax.bar_label(ax.containers[0])

    ax = sns.barplot(x='White %', y='Location', data=population_dataframe, ax=axes[2])
    ax.bar_label(ax.containers[0])

    ax = sns.barplot(x='Hispanic %', y='Location', data=population_dataframe, ax=axes[3])
    ax.bar_label(ax.containers[0])

    # axes[0].set_title("Asian")
    # axes[1].set_title("Black")
    plt.suptitle("POPULATION RATE IN USA")
    # plt.show()
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
        hatecrime_df_2020 = hatecrime_dataframe[hatecrime_dataframe['DATA_YEAR'] == 2020]
        hatecrime_dataframe['OFFENDER_RACE_COUNT'] = hatecrime_dataframe.groupby('OFFENDER_RACE')['OFFENDER_RACE'].transform('count')
        ax = sns.barplot(x="OFFENDER_RACE_COUNT", y="OFFENDER_RACE", data=hatecrime_dataframe)
        ax.set(xlabel='OFFENDER RACE COUNT', ylabel='OFFENDER RACE')
        ax.bar_label(ax.containers[0])
        plt.title('OFFENDER RACE')
        plt.grid(True)

    elif column_name == 'victim count':
        plt.figure(figsize=(15, 10))
        hatecrime_dataframe['VICTIMS COUNT'] = hatecrime_dataframe.groupby('DATA_YEAR')['VICTIM_COUNT'].transform('count')
        ax = sns.barplot(x="DATA_YEAR", y="VICTIMS COUNT", data=hatecrime_dataframe)
        ax.set(xlabel='YEAR', ylabel='VICTIMS COUNT"')
        ax.bar_label(ax.containers[0])
        plt.title('NUMBERS OF VICTIM OVER THE YEARS')
        plt.grid(True)

    elif column_name == 'anti-asian':
        # hatecrime_dataframe['Asian'] = hatecrime_dataframe[hatecrime_dataframe['BIAS_DESC'] == 'Anti-Asian']
        hatecrime_dataframe['Anti-Asian'] = hatecrime_dataframe.groupby('DATA_YEAR')['Asian'].transform('count')
        # anti_asian = hatecrime_dataframe[hatecrime_dataframe['BIAS_DESC'] == 'Anti-Asian'].count()
        ax = sns.barplot(x=hatecrime_dataframe['DATA_YEAR'], y=hatecrime_dataframe['Anti-Asian'])
        ax.set(xlabel='YEAR', ylabel='Anti-Asian Victim Count')
        ax.bar_label(ax.containers[0])
        plt.title('NUMBERS OF ANTI-ASIAN VICTIM OVER THE YEARS')
        plt.grid(True)
    return plt


def visualize_unemployment(unemployment_dataframe):
    """
    Function to plot charts for unemployment dataset
    :param unemployment_dataframe: Unemployment dataframe
    :return: Bar plot of unemploymeny vs year
    """
    unemployment_dataframe['unemployment %'] = unemployment_dataframe['unemployment'] / unemployment_dataframe['unemployment'].sum() * 100
    # fig, axes = plt.subplots(1, 2, figsize=(18, 21))
    # axes = axes.flatten()
    sns.barplot(x="Year", y="unemployment %", data=unemployment_dataframe)
    # sns.barplot(x="unemployment %", y="State", data=unemployment_dataframe, ax=axes[1])
    plt.title("Unemployment Rate")
    plt.grid(True)
    return plt
