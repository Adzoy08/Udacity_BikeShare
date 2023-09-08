# Explore US Bike Share Data
By: S. D. Boadi<br>
Created on: September 2023


### Overview
In this project, we will utilize Python to investigate data concerning bike share systems in three prominent U.S. cities: Chicago, New York City and Washington.


### Files used
All datasets were from [Chicago](https://www.divvybikes.com/system-data), [New York](https://www.citibikenyc.com/system-data) and [Washington](https://www.capitalbikeshare.com/system-data).
The original files were significantly larger and less organized. To simplify the analysis and evaluation process, some data cleaning was carried out, resulting in the condensation of these files into six columns.


### The Datasets
Data from the initial six months of 2017 has been randomly chosen and is available for all three cities. Each of these data files shares a common set of six (6) core columns:
* Start Time (e.g., 2017-05-02 00:08:59)
* End Time (e.g., 2017-06-07 00:22:45)
* Trip Duration (in seconds - e.g., 856)
* Start Station (e.g., Clark St & Randolph St)
* End Station (e.g., Desplaines St & Jackson Blvd)
* User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year


### Statistics Computed 
**Popular times of travel**
* most common month
* most common day of week
* most common hour of day

**Popular stations and trip**
* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

**Trip duration**
* total travel time
* average travel time

**User info**
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Prerequisities
The Python 3 and these libraries were used for this project are:
- panda  
- NumPy
- time


### Credits
Grateful to [Udacity](https://www.udacity.com/) for providing all the necessary resources and instruction to complete the project.

Thanks to [Motivate](https://www.motivateco.com/) for making their data available for this project.