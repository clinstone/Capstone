
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[30]:


from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error, roc_auc_score


# In[2]:


df = pd.read_csv('/home/ubuntu/MIMICmaterialized/oasis.csv')


# In[4]:


df.describe(include='all')


# In[5]:


df.info()


# In[6]:


df_adult = df.loc[df['icustay_age_group'] == 'adult']


# In[7]:


df_adult.info()


# In[10]:


df_adult.describe(include='all')


# In[12]:


df_adult_dropped = df_adult.dropna().copy()


# In[13]:


df_adult_dropped.info()


# In[14]:


df_adult_dropped.describe(include='all')


# In[17]:


df_scores_hos = df_adult_dropped[['age_score', 'preiculos_score',                      'gcs_score', 'heartrate_score', 'meanbp_score',                  'resprate_score', 'temp_score', 'urineoutput_score', 'mechvent_score',                      'electivesurgery_score', 'hospital_expire_flag']].copy()


# In[20]:


y = df_scores_hos.pop('hospital_expire_flag')


# In[21]:


y


# In[22]:


X = df_scores_hos.copy()


# In[23]:


X.shape


# In[25]:


X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=.33,
                                                    random_state=0,
                                                   stratify=y)


# In[26]:


# Train and fit model                                                   
rf = RandomForestClassifier(random_state=0,n_jobs=-1)

rf.fit(X_train, y_train)
                                     
# Test Prediction
pred = rf.predict(X_test)
print('Accuracy score: {:.3}'.format(rf.score(X_test, y_test)))


# In[34]:


y_predict_proba = rf.predict_proba(X_test)


# In[31]:


y_pred = rf.predict(X_test)


# In[32]:


roc_auc_score(y_test, y_pred)


# In[39]:


y_proba = y_predict_proba[:,1]


# In[40]:


roc_auc_score(y_test, y_proba)


# In[41]:


rf

