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
    
        ui.input_radio_buttons("plot_type", "Type of plot", choices=["Heat", "Bar all", "Bar by identity"]),
    
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
    @reactive.event(input.plot_type, ignore_none=True)
    
    def plot1():
     
#        fig, ax = plt.subplots(nrows=1, ncols=1)
        
        ##load in the data
        
        if input.plot_type()=="Heat":
            
            if input.input_data()!=None:
            
                all_loaded_file=input.input_data()
                
                loaded_file=all_loaded_file[0]
                
                print(loaded_file)
                
                print(loaded_file['datapath'])
                
                file_name=loaded_file['datapath']
                
#            else:
                
 #               file_name="situated_assessment_survey_responses.csv"#"J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv"

                all_data=pd.read_csv(file_name)

                print("all_data")

                print(all_data)

                useful_columns_df_w_nas=all_data.copy()#.filter(like="stress.")

                del useful_columns_df_w_nas["student"]
                del useful_columns_df_w_nas["Identity"]

                useful_columns_df_wide=useful_columns_df_w_nas.fillna(-1)

                useful_columns_df=useful_columns_df_wide.transpose()

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

        if input.plot_type()=="Bar by identity":
            
            if input.input_data()!=None:
            
                all_loaded_file=input.input_data()
                
                loaded_file=all_loaded_file[0]
                
                print(loaded_file)
                
                print(loaded_file['datapath'])
                
                file_name=loaded_file['datapath']
            
            #file_name="situated_assessment_survey_responses.csv"#"J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv"

                all_data=pd.read_csv(file_name)

                print("all_data")

                print(all_data)
                
                useful_columns_df=all_data.copy()
                
                del useful_columns_df["student"]

                print("useful_columns_df")

                print(useful_columns_df)


                grouped_means=useful_columns_df.groupby('Identity').mean()

                #grouped_means.index.head="Identity"

                grouped_means=grouped_means.rename_axis("Identity").reset_index()

                #grouped_means=grouped_means.reset_index(inplace=True)

                print("grouped_means")

                print(grouped_means)

                useful_columns_long_df=pd.melt(grouped_means, id_vars="Identity")

                print("useful_columns_long_df")

                print(useful_columns_long_df)


                #fig, ax = plt.subplots(nrows=1, ncols=1)

                #ax=sns.barplot(grouped_means, x="body_mass_g", y="island", hue="Identity")

                #ax=sns.barplot(useful_columns_long_df, x="Situation", y="stress.s", hue="Identity")

                ax=sns.barplot(useful_columns_long_df, y="variable", x="value", hue="Identity")

                ax.set_xlabel("Average stress")

                ax.set_ylabel("")
            
        if input.plot_type()=="Bar all":
            
            if input.input_data()!=None:
            
                all_loaded_file=input.input_data()
                
                loaded_file=all_loaded_file[0]
                
                print(loaded_file)
                
                print(loaded_file['datapath'])
                
                file_name=loaded_file['datapath']
 #           
  #          file_name="situated_assessment_survey_responses.csv"#"J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv"

                all_data=pd.read_csv(file_name)

                print("all_data")

                print(all_data)
                
                useful_columns_df=all_data.copy()
                
                del useful_columns_df["student"]

                print("useful_columns_df")

                print(useful_columns_df)


                grouped_means=useful_columns_df.groupby('Identity').mean()

                #grouped_means.index.head="Identity"

                grouped_means=grouped_means.rename_axis("Identity").reset_index()

                #grouped_means=grouped_means.reset_index(inplace=True)

                print("grouped_means")

                print(grouped_means)

                useful_columns_long_df=pd.melt(grouped_means, id_vars="Identity")

                print("useful_columns_long_df")

                print(useful_columns_long_df)


                #fig, ax = plt.subplots(nrows=1, ncols=1)

                #ax=sns.barplot(grouped_means, x="body_mass_g", y="island", hue="Identity")

                #ax=sns.barplot(useful_columns_long_df, x="Situation", y="stress.s", hue="Identity")

                ax=sns.barplot(useful_columns_long_df, y="variable", x="value", errorbar=None, color="blue")#, hue="Identity")

                ax.set_xlabel("Average stress")

                ax.set_ylabel("")
            
        return ax
     
     
app = App(app_ui, server)





















































