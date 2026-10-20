##code for plotting the heatmap in python

##############################

##location: cd Github/socits_dashboard/dev

##to run: python plot_heatmap.py

###############################

##libraries

import random
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd

import scipy as sp

#########################################

##load in the data

data_file_name="situated_assessment_survey_responses.csv"#"J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv"

all_data=pd.read_csv(data_file_name)

print("all_data")

print(all_data)

useful_columns_df_w_nas=all_data#.filter(like="stress.")

del useful_columns_df_w_nas["student"]
del useful_columns_df_w_nas["Identity"]

useful_columns_df_wide=useful_columns_df_w_nas.fillna(-1)

useful_columns_df=useful_columns_df_wide.transpose()

print("useful_columns_df")

print(useful_columns_df)

##load in the situation names

#situations_file_name="Github/socits_dashboard/dev/situations_with_full_names_sch_3_timepoint_1.csv"

#all_situation_names=pd.read_csv(situations_file_name)

#print("all_situation_names")

#print(all_situation_names)

#short_sit_names=all_situation_names.Abbr

#useful_columns_df.columns=short_sit_names

#fig, ax = plt.subplots(nrows=1, ncols=1)

ax=sns.clustermap(useful_columns_df, method="single", cmap="vlag", xticklabels=False, cbar_pos=(0.12, 0.2, 0.03, 0.4))

ax.ax_row_dendrogram.set_visible(False)

ax.ax_col_dendrogram.set_visible(False)

ax.tick_params(left=False, right=False)

ax.tick_params(left=False, right=False)

plt.show()

























