import os

import pandas as pd

directory = "../data/wards"

df_list = []

columns = [
    'Unique Code (Do not Fill)', 'ICMR ID', 'SNo', 'Patient ID/IPD ID',
    'Name', 'Age', 'Sex (M/F)', 'Date of Admission',
    'Municipal Ward of patient Residence (to be filled by MCGM)',
    'District of patient residence', 'Address of patient', 'Contact Number',
    'Facility where admitted',
    'Current Outcome (Admitted/\n Discharge/\n Death/\n Transfer/\n LAMA/\n DAMA)',
    'Date of Outcome',
    'In case of Transfer, transferred to which hospital/Facility',
    'Symptomatic (Y/N)', 'Current Health Status (Stable/Critical)',
    'Is patient in ICU? (Y/N)',
    'If Critical mention intervention (Nasal O2, Facemask O2, HFNC, NRBM, NIV, Ventilator)',
    'On dialysis (Y/N', 'Dates of latest positive test (to be left blank)',
    'Date of last test (to be left blank)',
    'Result of last test (to be left blank)', 'Sample Collected (Y/N)',
    'Date of Sample Collection (FIRST)',
    'Result of Sample (Positive/\n Negative/\n Awaited/\n Inconclusive)',
    'Date of Sample Collection (Second)', 'Result of Sample(second)',
    'Date of Sample Collection (Third)', 'Result of Sample(Third)',
    'Date of Sample Collection (Fourth)', 'Result of Sample (Fourth)',
    'Date of Sample Collection (Fifth)', 'Result of Sample (Fifth)',
    'Date of Sample Collection (Sixth)', 'Result of Sample (Sixth)',
    'Remarks'
]

df = pd.DataFrame(columns=columns)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".xlsx") and not filename.startswith('~$') and 'Ward' in filename:
        wb = os.path.join(directory, filename)
        df = pd.read_excel(wb, usecols=columns, na_values=[''])
        df.insert(0, column='filename', value=filename)
        df_list.append(df)

df = pd.concat(df_list, sort=False, ignore_index=True)
df = df.dropna(subset=['SNo'])
df.to_csv('../consolidated-wards.csv', index=False)
