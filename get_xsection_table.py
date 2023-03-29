
import pandas as pd

xsect_data = pd.read_csv('C:\\Users\\akselfe\\Documents\\st-l\\profildata_IPE_HE.csv',sep = ';')

xsect_data.to_hdf('xsect_data_IPE_HE.h5', key='xsect_data', mode='w')  



