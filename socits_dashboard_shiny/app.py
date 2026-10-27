##shiny run --reload --launch-browser Github/socits_dashboard/socits_dashboard_shiny/app.py

########################################################

##libraries

import random
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd

import scipy as sp

from shiny import reactive, Inputs, ui, App, render

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

###############################################################



#situations_file_name="Github/socits_dashboard/dev/situations_with_full_names_sch_3_timepoint_1.csv"

#all_situation_names=pd.read_csv(situations_file_name)

#print("all_situation_names")

#print(all_situation_names)

#short_sit_names=all_situation_names.Abbr


###############################################################

app_ui = ui.page_sidebar(

    ui.sidebar(
    
        ui.input_file("input_data", "Choose a file to upload:"),
        
        ui.input_text("selected_measure_input", "Selected measure:"),
        
        ui.input_text("selected_grouping_input", "Selected grouping:"),
    
        ui.input_radio_buttons("plot_type", "Type of plot", choices=["Heat", "Average measure by situation", "Average measure by situation and grouping"]),
        
        ui.input_action_button("plot_button", "Make plot"),
    ),
    
    ui.output_plot("plot1"),

    
)

###############################################################


def server(input, output, session):
    
        
    @render.plot
    # ignore_none=False is used to instruct Shiny to render this plot even before the
    # input.run button is clicked for the first time. We do this because we want to
    # render the empty 3D space on app startup, to give the user a sense of what's about
    # to happen when they run the simulation.
    #@reactive.event(ignore_none=False)
    @reactive.event(input.plot_button, ignore_none=True)
    
    def plot1():
     
#        fig, ax = plt.subplots(nrows=1, ncols=1)
        
        ##load in the data
        
        selected_measure=input.selected_measure_input()#"loneliness"
        
        print("selected_measure = ", selected_measure)

        selected_grouping=input.selected_grouping_input()#"attendance"
        
        all_loaded_file=input.input_data()
                
        loaded_file=all_loaded_file[0]
        
        print(loaded_file)
        
        print(loaded_file['datapath'])
        
        file_name=loaded_file['datapath']
        
#            else:
        
#               file_name="situated_assessment_survey_responses.csv"#"J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv"

        all_data=pd.read_excel(file_name)

        print("all_data")

        print(all_data)
        
        if input.plot_type()=="Heat":
            
            if input.input_data()!=None:
            
#                useful_columns_df_w_nas=all_data.copy()#.filter(like="stress.")

 #               del useful_columns_df_w_nas["student"]
  #              del useful_columns_df_w_nas["Identity"]

   #             useful_columns_df_wide=useful_columns_df_w_nas.fillna(-1)
   
                print("selected_measure = ", selected_measure)
   
                selected_columns=Heatmap_Data_Wrangling(all_data, selected_measure)

                useful_columns_df=selected_columns.transpose()

                print("useful_columns_df")

                print(useful_columns_df)
                
                ax=sns.clustermap(useful_columns_df, method="single", cmap="vlag", xticklabels=False, cbar_pos=(0.1, -0.1, 0.03, 0.4))

                ax.ax_row_dendrogram.set_visible(False)

                ax.ax_col_dendrogram.set_visible(False)

                ax.tick_params(left=False, right=False)

                ax.tick_params(left=False, right=False)

#        plt.show()

    #    plt.show()
        
#        fig.suptitle("SOCITS data")

        if input.plot_type()=="Average measure by situation and grouping":
            
            if input.input_data()!=None:
                
                useful_columns_df=Heatmap_Grouping_Variable(all_data, selected_measure, selected_grouping)

                print("useful_columns_df")

                print(useful_columns_df)

                grouped_means=useful_columns_df.groupby('grouping_variable').mean()

                #grouped_means.index.head="Identity"

                grouped_means=grouped_means.rename_axis("grouping_variable").reset_index()

                #grouped_means=grouped_means.reset_index(inplace=True)

                print("grouped_means")

                print(grouped_means)

                useful_columns_long_df=pd.melt(grouped_means, id_vars="grouping_variable")

                #useful_columns_long_df=pd.wide_to_long(grouped_means, stubnames="stress.s", i="Identity", j="Situation")

                #useful_columns_long_df=useful_columns_long_df.rename_axis(["Identity", "Situation"]).reset_index()

                print("useful_columns_long_df")

                print(useful_columns_long_df)


                #fig, ax = plt.subplots(nrows=1, ncols=1)

                #ax=sns.barplot(grouped_means, x="body_mass_g", y="island", hue="Identity")

                #ax=sns.barplot(useful_columns_long_df, x="Situation", y="stress.s", hue="Identity")

                #ax=sns.lineplot(useful_columns_long_df, y="variable", x="value", hue="grouping_variable")
                #ax=sns.scatterplot(useful_columns_long_df, y="variable", x="value", hue="grouping_variable")

                ax=sns.pointplot(useful_columns_long_df, y="variable", x="value", hue="grouping_variable")

                #ax=sns.pointplot(all_means, y="variable", x="value")

                ax.legend(title=selected_grouping)

                ax.set_xlabel("Stress")

                ax.set_ylabel("")
            
        if input.plot_type()=="Average measure by situation":
            
            if input.input_data()!=None:
                
                selected_columns=Heatmap_Data_Wrangling(all_data, selected_measure)

                useful_columns_long_df=pd.melt(selected_columns)#, id_vars="grouping_variable")

                print("useful_columns_long_df")

                print(useful_columns_long_df)

                ax=sns.pointplot(useful_columns_long_df, y="variable", x="value", errorbar=None)

                xlabel_text="Average "+selected_measure

                ax.set_xlabel(xlabel_text)

                ax.set_ylabel("")
            
        return ax
     
     
app = App(app_ui, server)





















































