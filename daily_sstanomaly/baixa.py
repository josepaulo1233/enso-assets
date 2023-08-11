import pandas as pd
import requests  
import os    
from datetime import datetime, timedelta

local_p = os.getcwd()

data_inicial = '1/1/1982'
data_final = datetime.now() - timedelta(days=1)
datarange = pd.date_range(start=data_inicial, end=data_final)

for data in datarange:

    data_folder_fmt = data.strftime('%Y%m')
    data_full_fmt = data.strftime('%Y%m%d')

    url1 = f'https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/{data_folder_fmt}/oisst-avhrr-v02r01.{data_full_fmt}.nc'
    url2 = f'https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/{data_folder_fmt}/oisst-avhrr-v02r01.{data_full_fmt}_preliminary.nc'
    file_name = f'oisst-avhrr-v02r01.{data_full_fmt}.nc'

    print(url1)
    print(url2)

    response1 = requests.get(url1) 
    response2 = requests.get(url2) 

    if response1.status_code == 200:

        if os.path.isfile(local_p + '/' + file_name) == False:
            print(f'Baixando o arquivo...{file_name}')
            file = requests.get(url1)
            open(local_p + '/' + file_name, 'wb').write(file.content)
        else:
            print(f'Já existe o arquivo ...{file_name}')

    if response2.status_code == 200:

        if os.path.isfile(local_p + '/' + file_name) == False:
            print(f'Baixando o arquivo...{file_name}')
            file = requests.get(url2)
            file_name = f'oisst-avhrr-v02r01.{data_full_fmt}.nc'
            open(local_p + '/' + file_name, 'wb').write(file.content)
        else:
            print(f'Já existe o arquivo ...{file_name}')