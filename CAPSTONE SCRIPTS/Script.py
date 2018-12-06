# import modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, roc_auc_score, roc_curve, auc


def main():
	# load csv files 

	df = pd.read_csv('/home/clintone/MIMICmaterialized/oasis.csv')

	# Create dataframe with icustay_id and icustay_expire_flag
	df_flag = df[['icustay_id', 'icustay_age_group','icustay_expire_flag']].copy()



	# create target variable
	y = df['icustay_expire_flag'].copy()

	# create X variable
	X = df[['age_score', 'preiculos_score', 'gcs_score', 'heartrate_score', \
		                      'meanbp_score', 'resprate_score', 'temp_score','urineoutput_score', \
		                      'mechvent_score','electivesurgery_score']].copy()


	# train-test split	
	X_train, X_test, y_train, y_test = train_test_split(X, y, 
		                                        test_size=.33,
		                                        random_state=0,
		                                       stratify=y)

	# Train and fit model                                                   
	rf = GradientBoostingClassifier(random_state=0, learning_rate= 0.01, \
		                        max_features='sqrt', max_leaf_nodes=12, 
		                        n_estimators=1250 )

	# Created dataframe with subsection of X_test data
	# We will be using this to get the predicted probablities from the published OASIS model. 
	# We will use these predicted probabilites to creat our ROC curve, and use that as our baseline/yardstick. 	
	y_ind_prob = df.loc[X_test.index]

	# Fit model
	rf.fit(X_train, y_train)

	# Test Prediction
	pred = rf.predict(X_test)
	print('Accuracy score: {:.3}'.format(rf.score(X_test, y_test)))

	# Get predicted probabilites 	
	y_predict_proba = rf.predict_proba(X_test)

	# Get predicted probabilites of 1 (Death)
	y_proba = y_predict_proba[:,1]

	# Get AUROC score
	print('AUROC: {:.3}'.format(roc_auc_score(y_test, y_proba)))

	# Calculate Standard Mortality Rate (SMR) 
	SMR = sum(y_test)/sum(pred)
	print('SMR: {:.3}'.format(SMR))
	# (different way) print('SMR: {:.3}'.format(sum(y_test)/sum(pred)))

	# Calculate Brier score the long way
	difference = y_proba - y_test
	squared = np.square(difference)
	Brier = np.mean(squared)
	print('Brier Score: {:.3}'.format(Brier))
	
	# I later found out that SkLearn has its own method to calculate Brier score, I added this as a check to make sure my code was correct. 
	print('Brier Score [SKLEARN]: {:.3}'.format(brier_score_loss(y_test, y_proba)))
	
	# (different way) to do the above ---> print('Brier Score: {:.3}'.format(np.mean(np.square(y_proba - y_test))))
	
	# This is to calculate Brier score for the published OASIS predicted scores 
	print('Brier Score [IND]: {:.3}'.format(np.mean(np.square(y_ind_prob['oasis_prob'] - y_test))))


	# calculate the fpr and tpr for all thresholds of the classification
	# probs = model.predict_proba(X_test)
	# preds = probs[:,1]
	fpr, tpr, threshold = roc_curve(y_test, y_proba)
	roc_auc = auc(fpr, tpr)

	# ROC curve for published OASIS model 
	fpr_IND, tpr_IND, threshold = roc_curve(y_test, y_ind_prob['oasis_prob'])
	roc_auc_IND = auc(fpr_IND, tpr_IND)

	# Plot ROC curves

	plt.title('Receiver Operating Characteristic')

	plt.plot(fpr, tpr, 'b', label = 'AUC_OASIS = %0.3f' % roc_auc)
	plt.plot(fpr_IND, tpr_IND, 'g', label = 'AUC_IND = %0.3f' % roc_auc_IND)


	plt.legend(loc = 'lower right')
	plt.plot([0, 1], [0, 1],'r--')
	plt.xlim([0, 1])
	plt.ylim([0, 1])
	plt.ylabel('True Positive Rate')
	plt.xlabel('False Positive Rate')
	plt.show()

if __name__ == "__main__":
	main()
