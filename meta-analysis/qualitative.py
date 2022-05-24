import pandas as pd
import numpy as np

data_file = './all_data_unverified_for_testing.csv'
# Change this to final data

data = pd.read_csv(data_file)
#Imports data

data = data.loc[data['Reviewer Name'] == 'James Higginson']
# includes only data from those reviewed by me. Change in final analysis to 'Consensus'

supporting_text = data.filter(regex='supporting', axis=1)
supporting_text.index=data['Study ID']

cols_to_keep = [
       'Study ID', 
       'Title', 
       'First Author Name', 
       'Year of publication',
       'Could the selection of patients have introduced bias?',
       'Is there concern that the included patients do not match the review question?',
       'Could the conduct or interpretation of the index test have introduced bias?',
       'Is there concern that the index test, its conduct, or interpretation differ from the review question?',
       'Could the reference standard, its conduct, or its interpretation have introduced bias?',
       'Is there concern that the target condition as defined by the reference standard does not match the review question?',
       'Could the patient flow have introduced bias?',
       'What SORT score is this ?'
]

data = data[cols_to_keep]
