# 📈: Discover how the US Population changes over time? 
This project aims to develop a web-based analytic dashboard allowing users to explore the dynamic landscape of population changes across the USA. Users can delve into detailed insights on age groups, racial demographics, gender, and more through interactive charts at the national, state, and county levels.


![US Map](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/pop_test.png)

<br>

## **<span style="color:#424dc1; font-family:montserrat;">:page_facing_up: Background </span>**

After finalizing the app layout, I used Plotly Dash and many other tools to create an interactive dashboard for US population data from [The US Census Bureau](https://data.census.gov/). [This dashboard](https://sites.google.com/view/satyndrakgautam/us-national-statistics) covers demographic trends across all US counties from 2010 to 2022, catering to researchers, policymakers, and those interested in population dynamics. For more details, click here.

##### **<span style="color:rgba(51, 55, 75, 0.95); font-family:montserrat;">Skills Enhancement </span>**

I recently completed the [IBM Data Science Professional Certification](https://www.coursera.org/account/accomplishments/professional-cert/SMB6GDH3KV6R) on Coursera, aligning with my goal of advancing skills in Data Science & Software development. Throughout the program, I learned Plotly Dash, HTML, CSS, and many other tools, resulting in the development of my first web-based application.

Moreover, last December 2023, I was at first position as the top researcher/reader in the Plotly community. While building my app with Plotly Dash, I spent a significant amount of time exploring the platform, reading through about 925 posts in 25 days, to ensure I could learn more and deliver the best possible solutions. Prior to this, I had been exploring Plotly for a long time without signing up in there. However, I eventually signed up in October or November, though I honestly don't recall the exact date. Engaging with the community's posts has been invaluable for my growth.

![US Map](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/toplist.png)

<br>

## :page_facing_up: Methodology
  ### 1. Data Understanding & Data collection 
  Data Source : [US Census Bureau](https://www.census.gov/)

To achieve goal of this project, I gathered data from The US Census Bureau’s Population and Housing Estimates Program (PEP), which provides detailed demographic information by county, including age, gender, race, and ethnicity. However, it's important to note that the reporting and categorization methods employed by the Census Bureau for these populations have evolved over time. Additionally, the estimated data available at the US Census for population spans from 2010 to 2022.

In addition to the initial data collection efforts, I explored the [US County Health Rankings & Roadmap](https://www.countyhealthrankings.org/) as a potential data source. This platform is recognized for providing comprehensive information on various metrics including population, clinical care, income, and more, all in one centralized location.

Upon reviewing the data from this source spanning the last three years (2021 to 2023), I encountered inconsistencies in some columns, particularly for data ranging from 2010 to 2020. Additionally, there was an overwhelming volume of data consolidated into a single repository. Upon closer examination, I realized that this data did not align with the specific scope of the project. Therefore, I made the decision to forgo the utilization of data collected from this source. Instead, I chose to focus on alternative data sources that better fit the project's objectives and requirements.

I collected two kinds of data from this source. First kind was data by race, gender, and age-group and second kind of data was by age-group and gender alone. I utilized these data and provided insights based on these data in the deployed app. 

  ##### Facts: 
    - First kind of collected data contains 78 datasets
    - second kind of collected data contains 13 datasets. 

<br>

<p style="color: red;"> Please Note: As I began this project and notebook, each step towards the end of this notebook became a learning experience. I made sure to learn at each step, and then I applied those lessons to the next steps. </p>

 ### 2. Data Wrangling
 
The data wrangling process for both collected data was performed separately and highlighted in the notebook and the data wrangling process encompassed various tasks, including the removal of unnecessary columns, cleaning of data inconsistencies, conversion of data types, renaming of columns for consistency and more. Additionally, transformations such as creating dictionaries to map state names with their initials were performed to facilitate data access and manipulation. 

#### Data Wrangling for first set of data: 
* First, we will ulitize the data for white race alone, and then we will create a list of dataframes and then, remove the unnecessary columns for this particular race.
* Cleaning the columns name using snake naming convention.
* Add a year column ranging from 2010 to 2022 to each dataframe respectively.
* Merge the data by years for this particular race.
* Rename some of the columns
* In order to differentiate between columns and its data, we will use prefix to each column except a few columns such as geo_id, state, county and more.
* Extract statecode, countycode, and fipscode from geo_id for later use such merging the data.
* Rearrange these newly created columns with code.
* Create a separate dataframe with unique state including United States along with their respective statecode.
* Create a dictonary with states name and thier initials and then, add a state column with initials mapping dictonary.
* Merge this separate state_name_with_code column dataframe with the final dataframe and then, rearrange the position of the state column.
* Merge entire data into one final df with respect to each race, gender, age-group, and year and respective columns.
* Adjust and verify & validate the final dataframe.
* Convert the data types of each column accordingly
* Wrapping up for this section.

#### Data Wrangling for second set of data: 
* Create a list of uploaded dataframe and then, retrieve some information
* Add a year column ranging from 2010 to 2022
* Extract the columns name of the first dataframe 2010 which has cleaned columns name and renamed the columns name of rest of the dataframes with respect to it
* Drop unnecessary columns and rename Geography to geo_id which will help us later in merging all the data
* Create a dataframe showing the columns name and datatypes with respect to each year as column
* Next convert the data types of each column of each dataframe by using convert_dtypes() method. (doesn't help in the first place)
* Check for null values, and check the same for particular dataset of 2010
* Convert the data types of each column of each dataframe with respect to data types of each column of dataframe 2010
* Verify and validate the data types of each column
* Create a final df for this data by merging all the respective data dataframes within and retrieve some info
* Verify and Validate the data points


After combining all refined and cleaned data, I uploaded the data into SQL DB where I performed a couple of tasks related to adjusting the population for age-group of 35yr-49yr and 50yr-64yr with respect to race and gender. 

<hr>

## :page_facing_up: Mockup Work

I initially created different dashboard designs to use space well and show lots of information. It was sort of challenging to finish the design because I wanted to make sure to maximize the information delivery. 
Even though I struggled and made a few designs I didn't like, I kept trying different versions. I came up with a design that aligns with the scope of project while offering valuable data-driven insights to the audience. 
Interestingly, the process became enjoyable when my daughter joined me for some sketches 😍🤣🤣 She drew her part, and I drew mine, collaborating together. 💖

[Add Pictures]

Anyway, through persistent efforts, countless hours, and iterative design processes, I successfully navigated challenges to develop an efficient dashboard layout. 

[Add Pictures]

## :page_facing_up: My workbench:

[Add contents]




## :page_facing_up: Navigate to App: 

[Add Contents]

## :page_facing_up: Resources Used: 

[Add contents]


<hr>

#### Please note - about app.py:

Thank you for visiting this repository! As you explore the functionalities and features of the deployed advanced analytic app, you may notice that the app.py file is not included in this repository. This decision was made to protect the confidentiality of the codebase, as the app is deployed in a public domain. While the app's functionality and user interface are publicly accessible, I have chosen not to share the app.py file to prevent unauthorized copying or replication of the proprietary code. However, I am more than happy to provide detailed documentation, code samples, or discuss the technical aspects of the app during interviews or discussions or collaboration. Apologies for any inconvenience caused. Your understanding and respect for the confidentiality of this codebase are greatly appreciated. 
