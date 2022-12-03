
# Impact of COVID-19 on Big Pharma and Health Insurance Stock Prices

# Overview

- __PROJECT TEAM:__ Joseph Trybala, Manas Bharadwaaj Subramanian, Miko Wieczorek, Ritu Kukreja
- __DATE CREATED:__ 2022-12-02

## Stock Data

- 2-3 sentences on this data and time window

## COVID Data

- 2-3 sentences on this data and time window used

## access rights

- <<license? brief about access rights>>

# About project directory

The following summarizes contents of the project directory:

## data

### rawdata

- `vaccinations.csv`: <<where does it come from and what it contains>>
- `epidemiology.csv`: <<where does it come from and what it contains>>
- `covid_events.csv`: major events throughout COVID-19 pandemic to have potentially impacted stock price trends.
- `fullstockdata.csv`: rawdata retrieved from the API for selected stock tickers <<list link>>

### processed

- `covid_stock_dataset.csv`: clean, merged dataset of COVID-19 and Stock data

## python

- `data_processing.py`: Python script with custom data acquisition and pre-processing functions
- `data_viz.py`: Python script with custom data visualization functions

## virtualenv

We used virtualenv to isolate Python dependencies. The `requirements.txt` lists all Python packages used in order to reproduce our results. After repo is cloned, run the following to restore the requirements into your local project space:

- `virutalenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## documents

Our presentation with more details on this project and potential users and applications of this dataset can be found here: `Project-Presentation.pptx`

# Running Code

Jupyter notebook file, **`data_manage.ipynb`**, is used as orchestrator to manage data retrieval, processing, cleaning, and writing. Make sure that your current working directory is the project root.

# GitHub Repo

- [covid_stock_data](https://github.com/bluemaw/covid-stock-data)
