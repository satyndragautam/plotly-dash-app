# 📈: Discover how the US Population changes over time? 
This project aims to develop a web-based analytic dashboard allowing users to explore the dynamic landscape of population changes across the USA. Users can delve into detailed insights on age groups, racial demographics, gender, and more through interactive charts at the national, state, and county levels.


![US Map](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/pop_test.png)

<br>

<hr>

<br>

## **<span style="color:#424dc1; font-family:montserrat;">:mag: Background </span>**

After finalizing the app layout, I used Plotly Dash and many other tools to create an interactive dashboard for US population data from [The US Census Bureau](https://data.census.gov/). [This dashboard](https://sites.google.com/view/satyndrakgautam/us-national-statistics) covers demographic trends across all US counties from 2010 to 2022, catering to researchers, policymakers, and those interested in population dynamics. For more details, click here.

##### **<span style="color:rgba(51, 55, 75, 0.95); font-family:montserrat;">Skills Enhancement </span>**

I recently completed the [IBM Data Science Professional Certification](https://www.coursera.org/account/accomplishments/professional-cert/SMB6GDH3KV6R) on Coursera, aligning with my goal of advancing skills in Data Science & Software development. Throughout the program, I learned Plotly Dash, HTML, CSS, and many other tools, resulting in the development of my first web-based application.

Moreover, last December 2023, I was at first position as the top researcher/reader in the Plotly community. While building my app with Plotly Dash, I spent a significant amount of time exploring the platform, reading through about 925 posts in 25 days, to ensure I could learn more and deliver the best possible solutions. Prior to this, I had been exploring Plotly for a long time without signing up in there. However, I eventually signed up in October or November, though I honestly don't recall the exact date. Engaging with the community's posts has been invaluable for my growth.

![US Map](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/toplist.png)

<br>

<hr>

<br>

## :gear: Methodology
  ### :file_folder: 1. Data Understanding & Data collection 
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

<br> 

 ###  :construction: 2. Data Wrangling
 
The data wrangling process for both collected data was performed separately and highlighted in the notebook and the data wrangling process encompassed various tasks, including the removal of unnecessary columns, cleaning of data inconsistencies, conversion of data types, renaming of columns for consistency and more. Additionally, transformations such as creating dictionaries to map state names with their initials were performed to facilitate data access and manipulation. 

#### :wrench: Data Wrangling - Part 1: 
The data wrangling process was performed separately for each dataset, focusing on refining data quality and consistency. This involved removing unnecessary columns to streamline data analysis, addressing data inconsistencies to ensure accuracy, and converting data types for better compatibility across datasets. Column names were standardized for consistency, and transformations such as creating dictionaries for mapping state names with their initials were implemented to facilitate data access and manipulation. Additionally, dataframes were merged by year and race to create a comprehensive dataset for further analysis.

#### :wrench: Data Wrangling - Part 2: 
During the data wrangling process, a systematic approach was taken to enhance data quality and integrity. Initially, a list of uploaded dataframes was compiled, and key tasks included adding a year column to establish temporal context, standardizing column names based on the structure of the 2010 dataframe to maintain consistency, and dropping unnecessary columns to focus on relevant data points. Data types were standardized across all dataframes to ensure compatibility and streamline data processing. Furthermore, null values were checked and addressed, and data types were validated against the 2010 dataframe to ensure consistency. Finally, a final dataframe was created by merging all relevant dataframes, and data points were thoroughly verified and validated to ensure accuracy and reliability in subsequent analysis.


After combining all refined and cleaned data, I uploaded the data into SQL DB where I performed a couple of tasks related to adjusting the population for age-group of 35yr-49yr and 50yr-64yr with respect to race and gender. 

<hr>

<br>

##  :clipboard: Early Mockup Iterations

I initially created different dashboard designs to use space well and show lots of information. It was sort of challenging to finish the design because I wanted to make sure to maximize the information delivery. 
Even though I struggled and made a few designs I didn't like, I kept trying different versions. I came up with a design that aligns with the scope of project while offering valuable data-driven insights to the audience. 

It's interesting, when my wife isn't around, my kid tends to play around me and sometimes interrupts me while I'm working. However, I always make sure she gets all the attention and love she needs. During the layout design process, things became enjoyable when my daughter joined me for some sketches 😍🤣🤣 She drew her part, and I drew mine, taking turns and collaborating together. 😉💖

#### Layout Deisgn Iteration: 

![Layout Design Iterations](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/layout_design.png)

<br>

#### My 4yrs old's drawings: 

![Vinny's Sktechs](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/vinny_drawing.png)

In addition to this, through persistent efforts, countless hours, and iterative design processes, I successfully navigated challenges to develop an efficient dashboard layout. Screenshots of app for your kind review:

<br>

<hr>

## :camera: Some Snaps:

Check out the final app, a user-friendly tool for exploring US population dynamics. Included are snapshots from the VS Code workbench and key code snippets to showcase the app's implementation details.

#### App Pics: 

![Page_1](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/app_pic1.png)

![Page_2](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/app_pic2.png)

![Page_3](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/app_pic3.png)

<hr>
<br>

#### Workbench and some code snippets: 

![Page_1](https://github.com/satyndragautam/plotly-dash-app/blob/main/images/app_pic1.png)

## :globe_with_meridians: Navigate to App: 

[Add Contents and links]

## :toolbox: Resources Used: 

[Add contents and links]


<hr>

#### Please note - about app.py:

Thank you for visiting this repository! As you explore the functionalities and features of the deployed advanced analytic app, you may notice that the app.py file is not included in this repository. This decision was made to protect the confidentiality of the codebase, as the app is deployed in a public domain. While the app's functionality and user interface are publicly accessible, I have chosen not to share the app.py file to prevent unauthorized copying or replication of the proprietary code. However, I am more than happy to provide detailed documentation, code samples, or discuss the technical aspects of the app during interviews or discussions or collaboration. Apologies for any inconvenience caused. Your understanding and respect for the confidentiality of this codebase are greatly appreciated. 
