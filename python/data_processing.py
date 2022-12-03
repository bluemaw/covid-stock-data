
import pandas as pd
import requests

def retrieve_stock_data(symbols, x=True, y=True):
    allstock_df = pd.DataFrame({'A': []})
    allstock_symbol_df = pd.DataFrame({'A': []})
    for symbol in symbols:
        post_covid_stock = requests.get('http://api.marketstack.com/v1/eod', params={
            'access_key' : '091f82f185fe19a44ea425263489ffbd',
            'symbols' : symbol,
            'sort': 'DESC',
            'date_from':'2016-11-01',
            'date_to':'2019-11-01',
            'limit': 1000})
            
        pre_covid_stock = requests.get('http://api.marketstack.com/v1/eod', params={
            'access_key': '091f82f185fe19a44ea425263489ffbd',
            'symbols': symbol,
            'sort': 'DESC',
            'date_from':'2019-11-01',
            'date_to':'2022-11-01',
            'limit': 1000})
            
        post_jdata = post_covid_stock.json()
        pre_jdata = pre_covid_stock.json()
        post_stock_df = pd.DataFrame(post_jdata["data"])
        pre_stock_df = pd.DataFrame(pre_jdata["data"])
        
        try:
            allstock_df
        except NameError:
            frames = [pre_stock_df, post_stock_df]
            allstock_df = pd.concat(frames, ignore_index=True)
        else:
            frames = [pre_stock_df, post_stock_df, allstock_df]
            allstock_df = pd.concat(frames, ignore_index=True)

        symbol_frame = allstock_df
        allstock_df_symbol = pd.concat([allstock_symbol_df, symbol_frame], ignore_index=True)
    
    return allstock_df_symbol

  
def process_stock_data(data):
    ##grouping the stocks back again based on symbol
    d = dict(tuple(data.groupby('symbol')))

    for key in d:
    #################################
        d[key] = d[key].drop(columns=['high','low','adj_low','adj_high','split_factor','dividend','exchange','A'])
        d[key] = d[key].drop(columns=['close','adj_close','adj_open','adj_volume','symbol','volume'])
        d[key] = d[key].rename(columns={"open":key+" open"})
        d[key]['date'] = pd.to_datetime(d[key].date,format='%Y-%m-%d', errors='coerce')
        d[key]['date'] = d[key]['date'].dt.strftime('%Y-%m-%d')
        d[key] = d[key].set_index('date')
    ###################################

    flag = False
    for key in d:
        if flag == False:
            newstock_df = d[key]
            print('key dataframe added')
            flag = True
        else:
            newstock_df = newstock_df.join(d[key], how='outer')

    newstock_df.reset_index(inplace=True)
    newstock_df = newstock_df.rename(columns = {'index':'date'})
    newstock_df['date'] = pd.to_datetime(newstock_df.date,format='%Y-%m-%d', errors='coerce')
    newstock_df['date'] = newstock_df['date'].dt.strftime('%Y-%m-%d')

    newstock_df['dt'] = pd.to_datetime(newstock_df['date'])
    newstock_df['month'] = newstock_df['dt'].dt.strftime('%b-%y')

    newstock_df = newstock_df.drop_duplicates(subset='date', keep="first")
    newstock_df = newstock_df.set_index('date')

    return newstock_df

def process_covid_data(epidemiology_df, vaccinations_df):
    ##The location key is determined by its level: So, country-level data for the United States would use the location key US; state-level data for California, US_CA; and Santa Clara County data, with an FIPS code of 06085, would use US_CA_06085.
    us_epidemiology_df = epidemiology_df[epidemiology_df.location_key == 'US']
    us_vaccinations_df = vaccinations_df[vaccinations_df.location_key == 'US']

    print('US Only')
    covid_df = pd.merge(us_epidemiology_df, us_vaccinations_df, how = 'outer', on = 'date')
    print('Merged')
    ###Cut down the covid dataframe
    covid_df = covid_df.drop(columns=['new_recovered','cumulative_recovered','location_key_x', 'location_key_y','new_persons_vaccinated_pfizer','cumulative_persons_vaccinated_pfizer','new_persons_vaccinated_moderna','cumulative_persons_vaccinated_moderna','new_persons_vaccinated_janssen','cumulative_persons_vaccinated_janssen','new_persons_vaccinated_sinovac','total_persons_vaccinated_sinovac','new_persons_fully_vaccinated_sinovac','total_persons_fully_vaccinated_sinovac','new_vaccine_doses_administered_sinovac','total_vaccine_doses_administered_sinovac'])

    covid_df['date'] = pd.to_datetime(covid_df.date,format='%Y-%m-%d', errors='coerce')
    covid_df['date'] = covid_df['date'].dt.strftime('%Y-%m-%d')
    covid_df = covid_df.set_index('date')

    print("COVID data processed")
    return covid_df
