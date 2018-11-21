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
	df_scores_hos = df_adult[['subject_id', 'hadm_id', 'icustay_id', 'age_score', 'preiculos_score', 'gcs_score', 'heartrate_score', 'meanbp_score', \
		 'resprate_score', 'temp_score', 'urineoutput_score', 'mechvent_score','electivesurgery_score', 'hospital_expire_flag']].copy()

	# create target variable
	y = df_scores_hos.pop('hospital_expire_flag')

	# create X variable
	X = df_scores_hos.copy()

	# train-test split	
	X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=.33,
                                                    random_state=0,
                                                   stratify=y)
	# Train and fit model                                                   
	rf = RandomForestClassifier(random_state=0,n_jobs=-1)

	rf.fit(X_train, y_train)
		                     
	# Test Prediction
	pred = rf.predict(X_test)
	print('Accuracy score: {:.3}'.format(rf.score(X_test, y_test)))
	
	# Get predicted probabilites 	
	y_predict_proba = rf.predict_proba(X_test)

	# Get predicted probabilites of 1 (Death)
	y_proba = y_predict_proba[:,1]

	# Get AUROC score
	roc_auc_score(y_test, y_proba)




    
    

