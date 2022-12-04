# COVID-19 Pandemic vs Health Adjacent Stock Prices

# Overview

- __PROJECT TEAM:__ Joseph Trybala, Manas Bharadwaaj Subramanian, Miko Wieczorek, Ritu Kukreja
- __DATE CREATED:__ 2022-12-02

## Stock Data

Stock data is stored in one .csv file `fullstockdata.csv` that is organized chronologically. Included details of data are opening prices, closing prices, volume, symbols, and dates among others. 

The chonological limits of our data are arranged around what is presumed to be close to the original infection date for Covid-19, 11-01-19. 3 years of data after that date chronicle the data under the effects of the pandemic. 3 years of data before act as a foil against which to compare.

## COVID Data

COVID data is stored in two .csv files that document the spread and fight against COVID 19, the data is organized chronologically. `epidemiology.csv` contains details regarding infections, deaths, recoveries, and other metrics across the world. 

`vaccinations.csv` contains details regarding the vaccination efforts worldwide.

The chonological limits of our data are from the beginning of records keeping regarding the COVID-19 pandemic until the project start.

## Access Rights and Distributions Approach

We have acquired, pre-processed, and deployed our final dataset from two publicly available sources of data, as elucidated earlier.

Stock data is freely available from many vendors as it is handed out to many parties and brokerages from the New York Stock Exchange. The web service that we are utilizing includes a free tier which was sufficient enough for our use case.
Covid-19 data has been freely available to the public through multiple avenues including through the CDC web portal, Johns Hopkins University's Center for Systems Science and Engineering, and the Covid Tracking Project.

Our combined dataset is released publicly under a Creative Commons 4.0 Attribution (CC BY 4.0) license (`LICENSE.md`), on GitHub repository titled [covid-stock-data](https://github.com/bluemaw/covid-stock-data) for use by any interested parties.

The dataset will undergo further modifications and updated versions will be released. The dataset is distributed in the comma separated values (.csv) format for ease of handling. The repository will be updated with further code snippets for acquiring, slicing, and organizing the dataset.

# About Project Directory

The following summarizes contents of the project directory:

## data

### rawdata

- `vaccinations.csv`: contains details regarding the vaccination efforts worldwide
- `epidemiology.csv`: `epidemiology.csv` contains details regarding infections, deaths, recoveries, and other metrics across the world
- `covid_events.csv`: major events throughout COVID-19 pandemic to have potentially impacted stock price trends.
- `fullstockdata.csv`: rawdata retrieved from the API for selected stock tickers

### processed

- `covid_stock_dataset.csv`: clean, merged dataset of COVID-19 and Stock data. Columns names include: 'ABBV open', 'AET open', 'PFE open', 'dt', 'cumulative confirmed', and 'cumulative vaccinated'. Data types include: strings and datetime objects.

## python

- `data_processing.py`: Python script with custom data acquisition and pre-processing functions
- `data_viz.py`: Python script with custom data visualization functions

## venv

We used [virtualenv](https://virtualenv.pypa.io/en/latest/#) to isolate Python dependencies. The `requirements.txt` lists all Python packages used in order to reproduce our results. After repo is cloned, run the following to restore the requirements into your local project space:

- `virutalenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## documents

Our presentation with more details on this project and potential users and applications of this dataset can be found here: **`Project-Presentation.pptx`** or **`Project-Presentation.pdf`**.

# Running Code

Jupyter notebook file, **`data_manage.ipynb`**, is used as orchestrator to manage data retrieval, processing, cleaning, and writing. Make sure that your current working directory is the project root. In this notebook the aforementioned data_processing.py (which contains our API pull script code) and data_viz.py (which contains our plotting script code) are imported as modules.

# Challenges and Limitations

- Our stock data is limited to the United States stock exchange data
- The issue with COVID data is that reporting is not uniform across all parties involved
- The API we are utilizing for stock data acquisition has a limit for API calls, which limits our data

# GitHub Repo

Please click link to our GitHub Repository titled [covid stock data](https://github.com/bluemaw/covid-stock-data).