# Welcome to my Capstone Project! 

Please check out a 4 minute video to get a quick overview of my project. 

[![Please click here](https://img.youtube.com/vi/W07OEYwsi5Y/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE "Link to video on YouTube")

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

