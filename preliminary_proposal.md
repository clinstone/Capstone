## Proposal 1 - Predicting heroin/fentanyl overdoses from opioid prescriber data

**1. High level description of project.** 
The opioid epidemic is a huge problem in our country. My project tries to predict heroin/fentanyl usage using overdose data combined with opioid prescription/prescriber data. My intuition is that changes in prescription number (per county) will predict heroin/fentanyl overdoses. 

**2. What question or problem are you trying to solve?**
I am trying to figure out if an increase in number of prescribed/dispensed drugs in a countty can predict the rate of addiction (as measured by the rate of overdoses). Conversely, if the number of prescribed/dispensed drugs decreases, does the rate of overdoses remain the same, while the drug overdosed on change from prescribed drugs to illicit drugs (heroin/illegal fentanyl). 

**3. How will you present your work?**
* Ideally: with a map visualization of the United States that shows changes over time of overdose deaths per county color-coded to the type of opioid that caused the overdose (prescribed or illegal). I would chart this against the change in prescribed/dispensed amounts of opioids. 
* Backup plan: Powerpoint slides. 

**4. What are your data sources?**
* Opioid Overdose Deaths from the CDC website. 
* 'Medicare Provider Utilization and Payment Data: Part D Prescriber' dataset  from the Center for Medicare and Medicaid Services (CMS) website. 
* 'Opioid overdose deaths by type of opioid' dataset & 'Opioid EMS calls' dataset from Data.gov website. 
* Per-capita opioid prescription data by county dataset from CDC website. 


**5. What’s your next step towards making this your project.**
Currently I only have access to Medicare prescriber data. I am looking for sources/datasets to extend my scope beyond Medicare data. 


## Proposal 2 - Predicting weather from people's music choices

**1. High level description of project.**
Instead of building a music recommendation engine, I will be trying the opposite of sorts - trying to gather patterns in people's music listening habits and correlate it with weather data. If successful, I should be able to predict the weather based on meta-data from music currently being played across the United States. 

**2. What question or problem are you trying to solve?**
I am trying to study if there is a connection between the weather and the music being consumed in the United States. If successful, this could help the tuning of music recommendation engines by factoring in the current weather. Futher along the line, I could see this being useful for spontanous creation of ambient music tailored to the user's music preferences and the current weather (I fully acknowledge this is a *way-way* down the line idea).  

**3. How will you present your work?**
* Ideally: with a map visualization of the United States that shows changes in music choices by genre or mood overtime, and an overlay of weather patters. 
* Backup plan: Powerpoint slides. 


**4. What are your data sources?**
* MusicBrainz dataset which collects music listening histories of it's users. 
* AcousticBrainz database of the acoustic characteristics of music and includes low-level spectral information and information for genres, moods, keys, and scales.
* NOAA’s Global Historical Climatology Network database 


**5. What’s your next step towards making this your project.**
I will be checking to see if my intution that weather affects the music choise of listeners holds true, and its effect size. 

## Proposal 3 - Predciting ideal schedule for Uber/Lyft drivers 

**1. High level description of project.**
I will be using transportation datasets from Chicago to predict the ideal times of day/days of week and sections of the city a freelance Uber/Lyft driver should work to maximise his/her earnings. 

**2. What question or problem are you trying to solve?**
Freelance Uber/Lyft drivers who have the ability to pick their schedule are faced with the dilemma of when would be the most profitable time/section of the city to work. By analyzing years of taxi data, including trip length, and tip amount, I hope to seek out patterns that can be taken advantage of by an Uber/Lyft driver seeking to maximise his/her profit. 

**3. How will you present your work?**
* Ideally: A visualization in the form of a map of the city where the driver can input his/her desired shift length or the desired times of the day they would like to work. , The map will then let them know the ideal locations to work, based on the time of day or the ideal time slots to work, based on location. 
* Backup plan: Powerpoint slides. 

**4. What are your data sources?**
Transportation datasets from the City of Chicago Data Portal. 
* Datasets I will be *definitely* looking at include: Taxi Trips, Average Daily Traffic Counts and  Historical Congestion Estimates. 
* Datasets I *hope* to add in include historical weather data and historical event data to add additional predictive ability to my project. 

**5. What’s your next step towards making this your project.**
I will be looking into learning about map visualzations and GIS data wrangling packages. 
