import pandas as pd
import numpy as np

data_file = './2022-06-13_final_consensus_data.csv'
# Change this to final data

data = pd.read_csv(data_file)
#Imports data

# includes only data from those reviewed by me. Change in final analysis to 'Consensus'

supporting_text = data.filter(regex='supporting', axis=1)
supporting_text.index=data['Study ID']

cols_to_keep = [
       'Study ID', 
       'Title', 
       'modality_group',
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
data = data.drop_duplicates(subset='Title', ignore_index=True)
