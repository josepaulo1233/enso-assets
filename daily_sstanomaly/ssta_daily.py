from netCDF4 import Dataset

file = Dataset('https://www.star.nesdis.noaa.gov/pub/sod/mecb/crw/data/5km/v3.1_op/nc/v1.0/daily/ssta/2023/ct5km_ssta_v3.1_20230802.nc#mode=bytes')

print(file.variables.keys())