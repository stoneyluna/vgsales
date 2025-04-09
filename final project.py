import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

dataset_1 = pd.read_csv('vgsales.csv')
dataset_2 = pd.read_csv('vgsales-12-4-2019-short.csv')
dataset_3 = pd.read_csv('vgsales-12-4-2019.csv')

# print(dataset_1.columns)
# # (['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales',
# #        'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
# #       dtype='object')
# print(dataset_2.columns)
# # (['Rank', 'Name', 'Genre', 'ESRB_Rating', 'Platform', 'Publisher',
# #        'Developer', 'Critic_Score', 'User_Score', 'Total_Shipped',
# #        'Global_Sales', 'NA_Sales', 'PAL_Sales', 'JP_Sales', 'Other_Sales',
# #        'Year'],
# #       dtype='object')
# print(dataset_3.columns)
# # (['Rank', 'Name', 'basename', 'Genre', 'ESRB_Rating', 'Platform',
# #        'Publisher', 'Developer', 'VGChartz_Score', 'Critic_Score',
# #        'User_Score', 'Total_Shipped', 'Global_Sales', 'NA_Sales', 'PAL_Sales',
# #        'JP_Sales', 'Other_Sales', 'Year', 'Last_Update', 'url', 'status',
# #        'Vgchartzscore', 'img_url'],
# #       dtype='object')

print(dataset_3.describe())