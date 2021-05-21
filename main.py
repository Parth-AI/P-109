import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics

df = pd.read_csv('StudentsPerformance.csv')
maths_list = df['math score'].to_list()

m_m = statistics.mean(maths_list)
m_me = statistics.median(maths_list)
m_mo = statistics.mode(maths_list)
m_std = statistics.stdev(maths_list)

print(f'Mean is: {m_m}')
print(f'Median is: {m_me}')
print(f'Mode is: {m_mo}')
print(f'Standard Deviation is: {m_std}')

m_std_first, m_std_end = m_m - m_std, m_m + m_std
m_std_sec_s, m_std_sec_e = m_m - (m_std*2), m_m + (m_std*2)
m_std_third_s, m_std_third_e = m_m - (m_std*3), m_m + (m_std*3)

maths_l = [result for result in maths_list if result > m_std_first and result < m_std_end]
print('{}% of data with in 1 standard deviation'.format(len(maths_l) * 100.00/len(maths_list)))

maths_l1 = [result for result in maths_list if result > m_std_sec_s and result < m_std_sec_e]
print('{}% of data with in 1 standard deviation'.format(len(maths_l1) * 100.00/len(maths_list)))

maths_l2 = [result for result in maths_list if result > m_std_third_s and result < m_std_third_e]
print('{}% of data with in 2 standard deviation'.format(len(maths_l2) * 100.00/len(maths_list)))

