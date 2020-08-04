import os

import pandas as pd

directory = "../data/hospitals"

# master column list
columns = [
    '(Do Not Modify) Hospital_Line_List', '(Do Not Modify) Row Checksum',
    '(Do Not Modify) Modified On', 'UPID', 'Sr. No.', 'ICMR ID', 'IPD No',
    'Name', 'Age', 'Gender', 'Date of Admission',
    'BMC Ward (To be filled by MCGM)', 'District of patient',
    'Address of patient', 'Contact Number', 'Hospital where admitted',
    'Outcome', 'Date of outcome', 'Transfer to Hospital', 'Symptomatic',
    'Current Health Status', 'Is patient in ICU',
    'If critical intervention used', 'On Dialysis',
    'Dates of latest positive test', 'Date of last test',
    'Result of last test', 'Sample collected', 'Date of Sample - First',
    'Result of sample - First', 'Date of sample -Second',
    'Result of test - Second', 'Date of sample - Third',
    'Result of test - Third', 'Date of sample - Fourth',
    'Result of test - Fourth', 'Date of sample - Fifth',
    'Result of test - Fifth', 'Updated by', 'Remarks'
]

mapping = {
    'Date of Outcome': 'Date of outcome',
    'Date of Outcome (DD/MM/YYYY)': 'Date of outcome',
    'Sr. No': 'Sr. No.',
    'SNo': 'Sr. No.',
    'Sr.No.': 'Sr. No.',
    'IPD NO': 'IPD No',
    'IPD': 'IPD No',
    '0': 'UPID',
    'UPID Number': 'UPID',
    'ICMR Id': 'ICMR ID',
    'ICMR Final': 'ICMR ID',
    'name': 'Name',
    'Name ': 'Name',
    'Date': 'Date of Admission',
    'District of patient residence': 'District of patient',
    'District of patient residence(Mmumbai city, Outside Mumbai, Mumbai Suburban)': 'District of patient',
    'Sample Collected': 'Sample collected',
    'Sample Collected (Y/N)': 'Sample collected',
    'Result of Sample (Positive/\nNegative/\nAwaited/\nInconclusive)': 'Result of sample - First',
    'Inconclusive': 'Result of sample - First',
    'Date of Sample Collection (FIRST)': 'Date of Sample - First',
    'Date of Sample Collection (Second)': 'Date of sample -Second',
    'Result of Sample(second)': 'Result of test - Second',
    'Result of Sample (Second)': 'Result of test - Second',
    'Date of Sample Collection (Third)': 'Date of sample - Third',
    'Result of Sample (Third)': 'Result of test - Third',
    'Result of Sample(Third)': 'Result of test - Third',
    'Date of Sample Collection (Fourth)': 'Date of sample - Fourth',
    'Result of Sample (Fourth)': 'Result of test - Fourth',
    'Date of Sample Collection (Fifth)': 'Date of sample - Fifth',
    'Result of Sample (Fifth)': 'Result of test - Fifth',
    'Date of Sample Collection (Sixth)': 'Date of sample - Sixth',
    'Result of Sample (Sixth)': 'Result of test - Sixth',
    'Sex': 'Gender',
    'Sex(M,F,O)': 'Gender',
    'Date of Last Positive Test': 'Dates of latest positive test',
    'Date of Latest Test': 'Date of last test',
    'Outcome of Latest Test': 'Result of last test',
    'Municipal Ward of patient Residence (to be filled by MCGM)': 'BMC Ward (To be filled by MCGM)',
    'Current Health Status (Stable/Critical)': 'Current Health Status',
    'Is patient in ICU? (Y/N)': 'Is patient in ICU',
    'If Critical mention intervention (Nasal O2, Facemask O2, HFNC, NRBM, NIV, Ventilator)': 'If critical intervention used',
    'If Critical, mention intervention (Nasal O2, Facemask O2, HFNC, NRBM, NIV, Ventilator)': 'If critical intervention used',
    'Updated By Fellow': 'Updated by',
    'Updated By': 'Updated by',
    'Updated by2': 'Updated by',
    'Hospital Where admitted': 'Hospital where admitted',
    'Hospital where Admitted': 'Hospital where admitted',
    'Remark': 'Remarks',
    'Symptomic': 'Symptomatic',
    'Symptomatic (Y/N)': 'Symptomatic',
    'SYesmptomatic': 'Symptomatic',
    'Outcome (Admitted/\nDischarge/\nDeath/\nTransfer/\nLAMA/\nDAMA/Absconding)': 'Outcome',
    'Outcome (Admitted/\nDischarge/\nDeath/\nTransfer/\nLAMA/\nDAMA)': 'Outcome',
    'Outcome (Admitted/ Discharged/ Death/ Transferred/ LAMA/ DAMA)': 'Outcome',
    'On dialysis (Y/N': 'On Dialysis',
    'On dialysis (Y/N) (Stable/Critical)': 'On Dialysis',
    'Date of Sample- Seventh': 'Date of sample - Seventh',
    'Result of Sample- Seventh': 'Result of test - Seventh',
    'In case of Transfer, transferred to which hospital/Facility': 'Transfer to Hospital',
    'In case of transfer, transferred to which hospital/facility': 'Transfer to Hospital',
    'ward': 'WARD',
    'Whether patient has any comorbidities': 'COMORBIDITIES',
    'Comorbidities (DM+HTN+Ca+CVD+CKD+Respiratory Illness+Mental Illness+ Ortho+Other)': 'COMORBIDITIES'
}

sheet_dict = {
    'Wockhardt_New.xlsx': 'Active Hospital_Line_Lists',
    'Tata Hospital New.xlsx': 'Tata Hospital',
    'Sion Hospital _New.xlsx': 'Active Hospital_Line_Lists',
    'Bhatia Hospital_New.xlsx': 'Bhatia Hospital',
    'ESI Hospital.xlsx': 'ESI',
    'Apex Hospital_New.xlsx': 'Apex',
    'Bombay Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Bandra Bhabha Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'BDBA _New.xlsx': 'Active Hospital_Line_Lists',
    'Hiranandani_New.xlsx': 'Active Hospital_Line_Lists',
    'Breach Candy_New.xlsx': 'Active Hospital_Line_Lists',
    'Seven Hills MCGM_New.xlsx': 'Active Hospital_Line_Lists',
    'St.George_New.xlsx': 'Active Hospital_Line_Lists',
    'HN Reliance_New.xlsx': 'Sheet1',
    'Seven Hills Reliance_New.xlsx': 'Active Hospital_Line_Lists',
    'Thunga_New.xlsx': 'Active Hospital_Line_Lists',
    'S.L Raheja Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Nanavati Hospital.xlsx': 'Nanavati',
    'Apex Mulund_New.xlsx': 'Active Hospital_Line_Lists',
    'Nair Hospital_New.xlsx': 'UpdatedFile',
    'Apex Super Speciality Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'BSES MG_New.xlsx': 'Active Hospital_Line_Lists',
    'Holy Family Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Kasturba_08.06.2020.xls': 'Sheet1',
    'Bhagwati Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'SRV Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'CAMA Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Hinduja Hospital_New.xlsx': 'Hinduja',
    'KJ Somaiya Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Kokilaben Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Rajawadi_New.xlsx': 'Active Hospital_Line_Lists',
    'R.N Cooper Hospital _New.xlsx': 'Active Hospital_Line_Lists',
    'SRCC Hospital_New.xlsx': 'SRCC Hospital',
    'HJ Doshi Hindu Sabha Hospital_New.xlsx': 'HJ Doshi Hindu Sabha',
    'Fortis Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Jaslok Hospital_New.xlsx': 'Jaslok',
    'Vikhroli Sushrusha_New.xlsx': 'Active Hospital_Line_Lists',
    'Galaxy Multispeciality_New.xlsx': 'Active Hospital_Line_Lists',
    'Lilavati Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'MBPT Hospital_New.xlsx': 'MBPT',
    'JRH_New.xlsx': 'Active Hospital_Line_Lists',
    'KEM Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'Global Hospital_New.xlsx': 'Global',
    'Kohinoor Hospital_New.xlsx': 'Active Hospital_Line_Lists',
    'GT Hospital_New.xlsx': 'GT',
    'HBT Hospital.xlsx': 'HBT Hospital',
    'Nowrosjee Wadia Maternity Linelist.xlsx': 'Sheet1',
    'Masina Hospital_New.xlsx': 'Active Hospital_Line_Lists'
}

drop_columns = ['Column' + str(i) for i in range(1, 16346)]
drop_columns.extend(['Unnamed: ' + str(i) for i in range(1, 64)])
drop_columns.extend(['-+', 'a'])

df_list = []

for f in os.listdir(directory):
    filename = os.fsdecode(f)
    if (filename.endswith(".xlsx") or filename.endswith(".xls")) and not filename.startswith('~$'):
        wb = os.path.join(directory, filename)
        df = pd.read_excel(wb, sheet_name=sheet_dict[filename], na_values=[''], header=0)
        columns_to_drop = list(set(df.columns) & set(drop_columns))
        df = df.drop(columns_to_drop, axis=1)
        df = df.rename(columns=mapping)
        df.insert(0, column='filename', value=filename)
        df_list.append(df)

df = pd.concat(df_list, axis=0, sort=False, ignore_index=True)

df.to_csv('../data/consolidated-hospitals.csv', index=False)
