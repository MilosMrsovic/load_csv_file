import pandas as pd
import time
from mm import get_missing_data

df = pd.read_csv('books.csv')
 
df['first_sentence'] = ''
df['subject'] = ''
df['place'] = ''
df['time'] = ''
 
for index, row in df.iterrows():
    # extract and transform data from web service
    missing_data = get_missing_data(row['title'], row['author'])
 
    if missing_data["first_sentence"] is not None:
        df.at[index, 'first_sentence'] = ', '.join(missing_data["first_sentence"])
 
    if missing_data["subject"] is not None:
        df.at[index, 'subject'] =  ', '.join(missing_data["subject"]) 
     
    if missing_data["place"] is not None:
        df.at[index, 'place'] = ', '.join(missing_data["place"])
 
    if missing_data["time"] is not None:
        df.at[index, 'time'] =  ', '.join(missing_data["time"])
 
    # add some sleep to stay under the service limit
    time.sleep(3)
 
    # load data
    df.to_xml('books.xml', parser='etree', root_name='library', row_name='book', index=False,  attr_cols=['id'], elem_cols=['title','author', 'published', 'genre', 'first_sentence', 'subject', 'place', 'time'])
