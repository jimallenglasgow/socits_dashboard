##code for plotting the bar charts in python

##############################

##location: cd Github/socits_dashboard/dev

##to run: python plot_bar_charts.py

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

useful_columns_df=all_data

#print(all_data.Identity)

#useful_columns_df=all_data.filter(like="stress.")

#useful_columns_df=useful_columns_df_w_nas#.fillna(-1)

##load in the situation names

#situations_file_name="situations_with_full_names_sch_3_timepoint_1.csv"

#all_situation_names=pd.read_csv(situations_file_name)

#print("all_situation_names")

#print(all_situation_names)

#short_sit_names=all_situation_names.Abbr

#useful_columns_df.columns=short_sit_names

#all_sit_ids=useful_columns_df.columns

#print("all_sit_ids")

#print(all_sit_ids)

del useful_columns_df["student"]

#useful_columns_df['Identity']=all_data.Identity

print("useful_columns_df")

print(useful_columns_df)


grouped_means=useful_columns_df.groupby('Identity').mean()

#grouped_means.index.head="Identity"

grouped_means=grouped_means.rename_axis("Identity").reset_index()

#grouped_means=grouped_means.reset_index(inplace=True)

print("grouped_means")

print(grouped_means)

useful_columns_long_df=pd.melt(grouped_means, id_vars="Identity")

#useful_columns_long_df=pd.wide_to_long(grouped_means, stubnames="stress.s", i="Identity", j="Situation")

#useful_columns_long_df=useful_columns_long_df.rename_axis(["Identity", "Situation"]).reset_index()

print("useful_columns_long_df")

print(useful_columns_long_df)


#fig, ax = plt.subplots(nrows=1, ncols=1)

#ax=sns.barplot(grouped_means, x="body_mass_g", y="island", hue="Identity")

#ax=sns.barplot(useful_columns_long_df, x="Situation", y="stress.s", hue="Identity")

ax=sns.barplot(useful_columns_long_df, y="variable", x="value", hue="Identity")

ax.set_xlabel("Stress")

ax.set_ylabel("")

plt.show()

























