## Final Proposal

1. What are you trying to do?  Articulate your objectives using absolutely no jargon (i.e. as if
you were explaining to a salesperson, executive, or recruiter).

In hospitals, the intensive care unit (ICU) admits severely ill patients in order to provide life saving treatment. One of the most important outcomes measured in ICUs are mortality rates (death rates). Doctors use [scoring systems](https://en.wikipedia.org/wiki/Medical_Scoring_Systems) in order to predict a patient's mortality risk during their ICU stay. 

There have been several different scoring systems developed and in use including: 
  * [The Oxford Acute Severity of Illness Score (OASIS)](https://www.ncbi.nlm.nih.gov/pubmed/23660729)
  * [Simplified Acute Physiology Score II (SAPS II)](https://en.wikipedia.org/wiki/SAPS_II)
  * [Sequential Organ Failure Assessment (SOFA) score](https://en.wikipedia.org/wiki/SOFA_score) 

My capstone will evalute the ability of each of these 3 different scoring systems ability to predict patient mortality. I will be using 


2. How has this problem been solved before? If you feel like you are addressing a novel
issue, what similar problems have been solved, and how are you borrowing from those?

3. What is new about your approach, why do you think it will be successful?

4. Who cares?  If you're successful, what will the impact be?

ICUs will be able to use it to predict mortality. 


5. How will you present your work? 
  
The main way I will present my work is through a Powerpoint presentation, with slides explaining my results. However, time permitting, I would like to create a visualization of 'real-time' predictions of a subsection of patients. This will be a proof-of-concept that hospitals could then scale up to include all their patients. 

6. What are your data sources? What is the size of your dataset, and what is your storage format?

The MIMIC-III (Medical Information Mart for Intensive Care) Clinical Database developed by the MIT Lab for Computational Physiology. It is a large collection of de-identified electronic medical records for over 40,00 patients admitted to the Beth Israel Deaconess Medical Center in Boston, MA, USA between 2001 and 2012. The database consists of 26 comma-separated-value (CSV) files. The total size of the uncompressed files is 47GB. All tables combined there are 534 columns and 728,556,685 rows. 


7. What are potential problems with your capstone, and what have you done to mitigate these problems?

This is not a problem as such, but the [Gordian Knot](https://en.wikipedia.org/wiki/Gordian_Knot) I am faced with is to extract the 10 - 15 variables each that the 3 scoring systems are based on (lab values, vital signs, [comorbid diagnoses](https://en.wikipedia.org/wiki/Comorbidity), etc.) from the 534 columns and 728,556,685 rows. In order to mitigate this issue I have researched and found the [SchemaSpy](http://schemaspy.org/) of the database and printed out the connections between the 26 tables and identified the columns in each that I need to extract. This will the job of writing the SQL queries much easier. 


8. What is the next thing you need to work on?
  * Getting the data, not just some, likely all?
  * Understanding the data?
  * Building a minimum viable product?
  * Gauging how much signal might be in the data?
  
  * I already have downloaded all my data. The next step is for me to finalize how I am going to analyze the data: 
    * Spin up an AWS EC2 and use Postgres (the method suggested by MIT, the providers of the database). 
    * Spin up an AWS EMR and use Spark. 
    * Use Amazon Redshift. 
    * Use Dask (not very familiar with this, but links like [this](http://docs.dask.org/en/latest/spark.html) and [this](https://matthewrocklin.com/blog//work/2018/08/28/dataframe-performance-high-level) are promising. 
  
  * I am going to be conducting research into the feasibity and cost effectiveness of each method. 
  * I am going to write and run the SQL queries needed to extract the variables/features I need to run my models. 
