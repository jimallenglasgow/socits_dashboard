##code for plotting the bar charts in python

##############################

##location: cd Github/socits_dashboard/dev

##to run: python load_ms_forms_single_measure.py

###############################

##libraries

import random
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd

import scipy as sp

import re

#########################################

##function to get the correct data and column names for a particular measure

def Heatmap_Data_Wrangling(all_data, selected_measure):
    
    full_selected_measure=selected_measure+".*"

    selected_columns=all_data.filter(regex=re.compile(full_selected_measure, re.IGNORECASE))

    #print("selected_columns")

    #print(selected_columns)

    long_column_names=selected_columns.columns

    #print("long_column_names")

    #print(long_column_names)

    no_columns=len(long_column_names)

    all_situation_names=[]

    for sel_column in long_column_names:

        split_names1=sel_column.split(":")

    #    print("split_names1")

     #   print(split_names1)
        
        split_names2=split_names1[1]
        
        split_names=split_names2.split("\n")

      #  print("split_names")

       # print(split_names)
        
        situation_name=split_names[0]
        
        #print("situation_name")

        #print(situation_name)
        
        all_situation_names.append(situation_name)

    #print("all_situation_names")

    #print(all_situation_names)

    selected_columns.columns=all_situation_names
    
    return(selected_columns)


#########################################

##function to create a SAM2 dataframe with a grouping variable

def Heatmap_Grouping_Variable(all_data, selected_measure, selected_grouping):

    full_selected_measure=selected_measure+".*"

    full_selected_grouping=selected_grouping+".*"

    selected_columns=Heatmap_Data_Wrangling(all_data, selected_measure)

    selected_grouping_columns=all_data.filter(regex=re.compile(full_selected_grouping, re.IGNORECASE))

    selected_grouping_columns.columns=["grouping_variable"]

    #print("selected_grouping_columns")

    #print(selected_grouping_columns)

    grouped_df=pd.concat([selected_columns, selected_grouping_columns], axis=1)
    
    return(grouped_df)


#########################################

##set the required parameters

data_file_name="Situated assessment survey.xlsx"#"situated_assessment_survey_responses.csv"#"J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv"

all_data=pd.read_excel(data_file_name)

print("all_data")

print(all_data)

selected_measure="loneliness"

selected_grouping="attendance"

##and now generate the data into the required form 

selected_columns=Heatmap_Data_Wrangling(all_data, selected_measure)

print("selected_columns")

print(selected_columns)

#########################################################################################################

##and now do the same for adding the classification question

grouped_df=Heatmap_Grouping_Variable(all_data, selected_measure, selected_grouping)

print("grouped_df")

print(grouped_df)










