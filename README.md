# Prediction of mortality in the Intensive Care Unit (ICU)


Please check out a 4 minute video to get a quick overview of my project (clicking link will redirect to video on YouTube). 

[![Please click here](https://img.youtube.com/vi/W07OEYwsi5Y/0.jpg)](http://www.youtube.com/watch?v=W07OEYwsi5Y "Link to video on YouTube")

[Link to Google Slides used in video above.](https://docs.google.com/presentation/d/12dy6UMHZK6b0LIdAluXxPv_bag-uVws0q15YsxB-Fb4/edit?usp=sharing)

## Introduction 
In hospitals, the intensive care unit (ICU) admits severely ill patients in order to provide life saving treatment. One of the most important outcomes measured in ICUs are mortality rates (death rates). Doctors use [scoring systems](https://en.wikipedia.org/wiki/Medical_Scoring_Systems) in order to predict a patient's mortality risk during their ICU stay. 

There have been several different scoring systems developed and in use including: 
  * [The Oxford Acute Severity of Illness Score (OASIS)](https://www.ncbi.nlm.nih.gov/pubmed/23660729)
  * Simplified Acute Physiology Score (SAPS) 
  * Logistic Organ Dysfunction Score (LODS) 

My capstone evaluated each of these 3 different scoring systems ability to predict patient mortality. I also combined the 3 scoring systems into one 'super scorer' and test it's predicitve ability.

## Prior research 

Past studies have tested the predictive power of individual scoring systems. The studies also used the whole adult population as one, irregardless of clinical diagnoses. Also, in my clinical experience, hospitals tend to use/favor one scoring system based on doctor preference, tradition or the hospital sub-culture. Rarely, if ever do, hospitals use all three. Also clinicans/heathcare professionals tend to use the same scoring system for the entire adult patient population in the ICU (children and newborns tend to have different scoring systems). 

## Data Sources

The [MIMIC-III (Medical Information Mart for Intensive Care) Clinical Database](https://mimic.physionet.org/) developed by the MIT Lab for Computational Physiology. It is a large collection of de-identified electronic medical records for over 40,00 patients admitted to the Beth Israel Deaconess Medical Center in Boston, MA, USA between 2001 and 2012. The database consists of 26 comma-separated-value (CSV) files. The total size of the uncompressed files is 47GB. All tables combined there are 534 columns and 728,556,685 rows. I had to complete an online course and submit an official application requesting access to the database. 

## Oxford Acute Severity of Illness Score (OASIS)

The Oxford Acute Severity of Illness Score (OASIS) is a parsimonious severity score developed using a hybrid genetic algorithm and particle swarm optimization approach which allowed direct optimization of a severity score in a clinically relevant form with simultaneous multivariate feature selection (Johnson, 2013). The score is calculated using 10 variables (see below). Each variable is given a sub-score based on patient data upto 24 hours after admission to the ICU. 

![OASIS-sub-scores](https://github.com/clinstone/Capstone/blob/master/CAPSTONE%20SCRIPTS/OasisPictures/OasisVariables.png)

[Source](http://alistairewj.github.io/project/oasis/)

Pre-ICU LOS = Length of Hospital Stay prior to admission to ICU
GCS = Glasgow Coma Scale
MAP = Mean Arterial Pressure

References:
Johnson, Alistair EW, Andrew A. Kramer, and Gari D. Clifford. "A new severity of illness scale using a subset of acute physiology and chronic health evaluation data elements shows comparable predictive accuracy*." Critical care medicine 41, no. 7 (2013): 1711-1718.


