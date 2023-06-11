import pandas as pd
import pandas_datareader.data as web
df = web.DataReader(
    '&'.join([		
		'dataset=EI_ETEA_M', 
		'from=2022-01-01', 
		'h=TIME', 
		'to=2022-12-01', 
		'v=Geopolitical entity (reporting)', 
		'FREQ=[M]', 
		'GEO=[AT,BE,BG,HR,CY,CZ,DK,EE,FI,FR,DE,EL,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SI,ES,SE]', 
		'INDIC=[ET-T]', 
		'STK_FLOW=[IMP]', 
		'UNIT=[MIO-EUR-NSA]']),
    'econdb')

desired_column = 'Geopolitical entity (reporting)'

# Get the column names that match the desired column
column_mapping = {col: desired_column for col in df.columns if desired_column in col}

# Rename the columns using the mapping dictionary
df.rename(columns=column_mapping, inplace=True)

training_set = df.iloc[:,0:108].values
test = pd.DataFrame(training_set, columns=['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland',
                                           'France', 'Germany', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta',
                                           'Netherlands', 'Poland', 'Greece', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden'])
# test.to_csv('imports.csv')