######################################################################################

##create a dataframe for testing the analysis programme

library(tidyverse)

####################################################################################

##original data frame

original_data<-read.csv("J:/SPHSU/Projects/projects/SOCITS S00606/Data/AnonymisedData/Surveys/school_3_time_1/dataframes/2100_SOCITS_school_3_timepoint_1_raw.csv")

measure_wide.df <- original_data %>% dplyr::select("socits_ID", grep(paste0("stress",".s"), names(original_data)), "Identity")

situation_info<-read.csv("~/Github/socits_dashboard/dev/situations_with_full_names_sch_3_timepoint_1.csv")

situation_names<-situation_info$Name

names(measure_wide.df)<-c("student", situation_names, "Identity")

write.csv(measure_wide.df, "~/Github/socits_dashboard/dev/situated_assessment_survey_responses.csv", row.names = F)




