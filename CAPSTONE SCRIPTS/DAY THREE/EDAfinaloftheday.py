
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, roc_auc_score


# In[3]:


df = pd.read_csv('/home/ubuntu/MIMICmaterialized/oasis.csv')


# In[4]:


df.describe(include='all')


# In[5]:


df.info()


# In[6]:


df_adult = df.loc[df['icustay_age_group'] == 'adult']


# In[7]:


df_adult.info()


# In[48]:


len(df_adult['subject_id'].unique())


# In[49]:


len(df_adult_dropped['subject_id'].unique())


# In[54]:


len(df_adult['icustay_id'].unique())


# In[53]:


len(df_adult_dropped['icustay_id'].unique())


# In[8]:


df_adult.describe(include='all')


# In[9]:


df_adult_dropped = df_adult.dropna().copy()


# In[38]:


df_adult_dropped.corr()


# In[10]:


df_adult_dropped.info()


# In[11]:


df_adult_dropped.describe(include='all')


# In[12]:


df_scores_hos = df_adult_dropped[['age_score', 'preiculos_score',                      'gcs_score', 'heartrate_score', 'meanbp_score',                  'resprate_score', 'temp_score', 'urineoutput_score', 'mechvent_score',                      'electivesurgery_score', 'hospital_expire_flag']].copy()


# In[55]:


df_scores_icu = df_adult_dropped[['age_score', 'preiculos_score',                      'gcs_score', 'heartrate_score', 'meanbp_score',                  'resprate_score', 'temp_score', 'urineoutput_score', 'mechvent_score',                      'electivesurgery_score', 'icustay_expire_flag']].copy()


# In[13]:


y = df_scores_hos.pop('hospital_expire_flag')


# In[56]:


y = df_scores_icu.pop('icustay_expire_flag')


# In[14]:


y


# In[57]:


X = df_scores_icu.copy()


# In[16]:


X.shape


# In[58]:


X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=.33,
                                                    random_state=0,
                                                   stratify=y)


# In[63]:


# Train and fit model                                                   
rf = RandomForestClassifier(random_state=0,n_jobs=-1,n_estimators=300 )

rf.fit(X_train, y_train)
                                     
# Test Prediction
pred = rf.predict(X_test)
print('Accuracy score: {:.3}'.format(rf.score(X_test, y_test)))


# In[64]:


y_predict_proba = rf.predict_proba(X_test)


# In[20]:


y_pred = rf.predict(X_test)


# In[21]:


roc_auc_score(y_test, y_pred)


# In[65]:


y_proba = y_predict_proba[:,1]


# In[66]:


roc_auc_score(y_test, y_proba)


# In[24]:


rf.get_params


# In[ ]:


param_grid = {'oob_score': [True, False],
            'n_estimators': [10, 20, 50, 100, 300, 1000],
            "max_depth": [3, None],
              "max_features": [1, 3, 10, 'sqrt', 'log2'],
              "min_samples_split": [2, 3, 10],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}


# In[67]:


n_estimators =  [10, 20, 50, 100, 300, 1000, 2000, 5000, 10000]
for i in n_estimators:
    rf1 = RandomForestClassifier(n_estimators = i, random_state=0,n_jobs=-1)
    rf1.fit(X_train, y_train)
    y_predict_proba = rf1.predict_proba(X_test)
    y_proba = y_predict_proba[:,1]
    print(i, roc_auc_score(y_test, y_proba), '\n''\n')


# In[29]:


n_estimators =  [10, 20, 50, 100, 300, 400, 500, 600, 700, 800, 900]
for i in n_estimators:
    rf1 = RandomForestClassifier(n_estimators = i, random_state=0,n_jobs=-1)
    rf1.fit(X_train, y_train)
    y_predict_proba = rf1.predict_proba(X_test)
    y_proba = y_predict_proba[:,1]
    print(i, roc_auc_score(y_test, y_proba), '\n''\n')


# In[30]:


max_features =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'sqrt', 'log2', 'auto']
for i in max_features:
    rf1 = RandomForestClassifier(n_estimators = 300, max_features = i, random_state=0,n_jobs=-1)
    rf1.fit(X_train, y_train)
    y_predict_proba = rf1.predict_proba(X_test)
    y_proba = y_predict_proba[:,1]
    print(i, roc_auc_score(y_test, y_proba), '\n''\n')


# In[34]:


df1 = pd.read_csv('/home/ubuntu/MIMICmaterialized/apsiii.csv')


# In[35]:


df1


# In[36]:


df1.info()


# In[37]:


df1['albumin_score'].unique()


# In[39]:


sofa = pd.read_csv('/home/ubuntu/MIMICmaterialized/sofa.csv')
qsofa = pd.read_csv('/home/ubuntu/MIMICmaterialized/qsofa.csv')
lods = pd.read_csv('/home/ubuntu/MIMICmaterialized/lods.csv')
mlods = pd.read_csv('/home/ubuntu/MIMICmaterialized/mlods.csv')
sirs = pd.read_csv('/home/ubuntu/MIMICmaterialized/sirs.csv')
saps = pd.read_csv('/home/ubuntu/MIMICmaterialized/saps.csv')


# In[40]:


sofa.info()


# In[41]:


sofa


# In[42]:


qsofa.info()


# In[43]:


qsofa


# In[45]:


lods.info()


# In[46]:


lods


# In[47]:


len(lods['subject_id'].unique())

