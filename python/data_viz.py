import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np

def plot_data(merged_df):
    plt.clf()

    df = merged_df

    matplotlib.rc_file_defaults()
    ax1 = sns.set_style(rc=None )
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax2 = ax1.twinx()

    ################Pharma Stock Data########################
    sns.lineplot(data = df['MRK open'], sort = False, ax=ax1, alpha=0.55,label = 'MRK Open Price')
    sns.lineplot(data = df['NVS open'], sort = False, ax=ax1, alpha=0.55,label = 'NVS Open Price')
    sns.lineplot(data = df['ABBV open'], sort = False, ax=ax1, alpha=0.55,label = 'ABBV Open Price')
    ####Pharma companies not in the vaccine market in the US have dashed lines to act as controls
    ax1.lines[0].set_linestyle("--")
    ax1.lines[1].set_linestyle("--")
    ax1.lines[2].set_linestyle("--")

    sns.lineplot(data = df['PFE open'], sort = False, ax=ax1, label = 'PFE Open Price')
    sns.lineplot(data = df['BNTX open'], sort = False, ax=ax1, label = 'BNTX Open Price')
    sns.lineplot(data = df['JNJ open'], sort = False, ax=ax1, label = 'JNJ Open Price')
    sns.lineplot(data = df['MRNA open'], sort = False, ax=ax1, label = 'MRNA Open Price')
    ###############Covid Data###############

    color = 'tab:red'
    ax2.set_ylabel('Covid Data (100 Million(s))', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    #sns.histplot(data = df, x='date', y='cumulative_confirmed', alpha=0.25, color=color, label = 'Cumulative Confirmed Cases', ax=ax2) ####??


    sns.lineplot(data = df['cumulative_confirmed'],  alpha=0.40,linewidth = 10, color=color, label = 'Cumulative Confirmed Cases', ax=ax2)
    color = 'tab:grey'
    sns.lineplot(data = df['cumulative_persons_vaccinated'] , alpha=0.40, linewidth = 10, color=color, label = 'Cumulative Vaccinations', ax=ax2)

    #Format
    color = 'tab:green'
    ax1.set_ylabel('Stock Price (USD)',color=color)
    ax1.tick_params(axis='y', labelcolor=color)


    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    years_fmt = mdates.DateFormatter('%Y')
    # format the ticks
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)

    # round to nearest years.
    datemin = np.datetime64(df['dt'][0], 'Y')
    datemax = np.datetime64(df['dt'].iloc[-1], 'Y') + np.timedelta64(1, 'Y')
    ax1.set_xlim('2016-11-01', '2022-11-01')

    # format the coords message box
    ax1.format_xdata = mdates.DateFormatter('%b-%Y')
    # ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax1.format_ydata = lambda x: '$%1.2f' % x  # format the price.
    ax1.grid(True)

    ax1.legend(loc=2)
    ax2.legend(loc=1)

    return plt