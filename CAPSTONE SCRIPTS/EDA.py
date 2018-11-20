import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

def clean_up(filename):
    
    # import dataframe
    df = pd.read_csv(filename)
    
    # keep only adult cases
    df_adult = df.loc[df['icustay_age_group'] == 'adult']
    
    # DECIDE ABOUT DROPPING NULL VALUES AND INSERT HERE
    
    # create dataframe based on raw values
    df_raw = df_adult[['subject_id', 'hadm_id', 'icustay_id', 'age', 'preiculos', 'gcs', 'heartrate', 'meanbp', \
                 'resprate', 'temp', 'urineoutput', 'mechvent','electivesurgery', 'hospital_expire_flag']].copy()
    
    # create dataframe based on computed scores
    df_scores = df_adult[['subject_id', 'hadm_id', 'icustay_id', 'age_score', 'preiculos_score', 'gcs_score', 'heartrate_score', 'meanbp_score', \
                 'resprate_score', 'temp_score', 'urineoutput_score', 'mechvent_score','electivesurgery_score', 'hospital_expire_flag']].copy()
    
    

