import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

model = ['a', 'b', 'c']

for name in model:

def clean_up(model):
    
	# import dataframe
	df_name = pd.read_csv(filename)

	# keep only adult cases
	df_adult = df.loc[df['icustay_age_group'] == 'adult']

	# DECIDE ABOUT DROPPING NULL VALUES AND INSERT HERE
	df_adult_dropped = df_adult.dropna().copy()

	# create dataframe based on raw values
	df_raw = df_adult[['subject_id', 'hadm_id', 'icustay_id', 'age', 'preiculos', 'gcs', 'heartrate', 'meanbp', \
		 'resprate', 'temp', 'urineoutput', 'mechvent','electivesurgery', 'hospital_expire_flag']].copy()

	# create dataframe based on computed scores
	df_scores = df_adult_dropped[['oasis_prob','icustay_id', 'age_score', 'preiculos_score', 'gcs_score', 'heartrate_score', \
                              'meanbp_score', 'resprate_score', 'temp_score','urineoutput_score', \
                              'mechvent_score','electivesurgery_score', 'icustay_expire_flag']].copy()

	# create target variable
	y = df_scores['icustay_expire_flag'].copy()

	# create X variable
	
	X = df_scores[['age_score', 'preiculos_score', 'gcs_score', 'heartrate_score', \
                              'meanbp_score', 'resprate_score', 'temp_score','urineoutput_score', \
                              'mechvent_score','electivesurgery_score']].copy()

	# train-test split	
	X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=.33,
                                                    random_state=0,
                                                   stratify=y)
	# Train and fit model                                                   
	rf = RandomForestClassifier(n_estimators = 300, random_state=0,n_jobs=-1)

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

	# Calculate Standard Mortality Rate (SMR) 
	SMR = sum(y_test)/sum(pred)
	print('SMR: {:.3}'.format(SMR)))
	# (different way) print('SMR: {:.3}'.format(sum(y_test)/sum(pred)))

	# Calculate Brier score
	difference = y_proba - y_test
	squared = np.square(difference)
	Brier = np.mean(squared)
	print('Brier Score: {:.3}'.format(Brier)))
	# (different way) print('Brier Score: {:.3}'.format(np.mean(np.square(y_proba - y_test))))

	# Create dataframe with icustay_id and icustay_expire_flag	
	df_flag = df[['icustay_id', 'icustay_age_group','icustay_expire_flag']].copy()	

	# Merge two dataframes on icustay_id	
	lods_merged = lods.merge(df_flag, on='icustay_id')

	# calculate the fpr and tpr for all thresholds of the classification
	# probs = model.predict_proba(X_test)
	# preds = probs[:,1]
	fpr, tpr, threshold = roc_curve(y_test, y_proba)
	roc_auc = auc(fpr, tpr)
	fpr_LODS, tpr_LODS, threshold = roc_curve(y_test_LODS, y_proba_LODS)
	roc_auc_LODS = auc(fpr_LODS, tpr_LODS)

	# Plot ROC curves
	
	plt.title('Receiver Operating Characteristic')
	
	plt.plot(fpr, tpr, 'b', label = 'AUC_OASIS = %0.3f' % roc_auc)
	plt.plot(fpr_LODS, tpr_LODS, 'g', label = 'AUC_LODS = %0.3f' % roc_auc_LODS)
	

	plt.legend(loc = 'lower right')
	plt.plot([0, 1], [0, 1],'r--')
	plt.xlim([0, 1])
	plt.ylim([0, 1])
	plt.ylabel('True Positive Rate')
	plt.xlabel('False Positive Rate')
	plt.show()

	# To get industry standard	
	y_ind_prob = df_scores.loc[X_test.index]
	




    
    

