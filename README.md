# Predicting Horror Movie IMDB Scores for a Female Audience

In my Metis linear regression project I created models for predicting the IMDB score for horror movies with a female audience. As a life-long fan of horror films I knew I wanted horror to be the genre of focus for my predictive modeling, but it wasn't until I began looking closely at IMDB's demographic breakdown that I realized the majority of users voting identified as male. From the over 600 movies I scraped from IMDB, each with a minmum of 10,000 votes, only about 18% of the total votes were from users that identified as women. With this target demographic in mind, I focused on creating models for 3 potential use cases for the models; predicting the score of a film already released, a film that has not yet been released, and a film that is still in the pitching or pre-production stages. My final models used GridSearchCV with Ridge Regression, however I also used GridSearchCV with Lasso Regression to view my most important features for each model. A summary of my modeling results can be found [here](RegressionPresentationJNE.pdf).

## Features
- Numeric
    - Year
    - Runtime in minutes
    - Budget
    - Male IMDB Score
    - Metascore
- Categorical
    - Director
    - Genre
    - Novel Adaptation
    - Plot tags:
        - Monster
        - Cult Classic
        - Female Protagonist
        - Murder
- Categorical Features not yet incorportated to model
    - Stars
    - Country of origin
    

## Tools Used
- BeautifulSoup
- Seaborn
- Pandas
- GridSearchCV
- Lasso Regression
- Ridge Regression
- Robust Scaler
- Standard Scaler

## Data Collection

My data was collected from scraping using requests python library with BeautifulSoup to parse the collected html. The [inital scraping](Initial_scraping.ipynb) collected the general data from a list of horror films on IMDB with 10,000 or more votes, I chose to put a minimum vote limit on the films to avoid outliers such as films with artifically high scores due to lack of user input. From this inital scraping some of the data collected includes release year, runtime in minutes, budget, metascore, and subgenre. I also scraped for films that fit this search parameters but also contained a specific plot tag of interest, I chose cult films, female protagonist, monsters, and murder as plot tags of interest. These tags were used to create a dummified column of 0 not a plot tag for that film, or 1 a plot tag used for that film. Each movie on IMDB has a page that shows the demographic breakdown for its score, so I also scraped the tables from these pages to get the scores based off gender and the vote counts per gender. The initial, demographic information, and plot tags scrapping resulted in multiple pandas dataframes. I [merged](Page_Scraping_And_EDA.ipynb) the dataframes together and then performed some exploratory data analysis, this consisted of correcting formatting issues from the data collection process, removing duplicates, and converting data types.

**Possible impacts**

Depending on the use these models could be use to predict potential positive audience response for adding a movie to a streaming service, screening a new movie at a theater, or when determining to fund a pitch movie. 


**Guide to the Repo**


Functions used

- my_functions.py
    
Testing Models with Different Features

- Adding in some categorical features
    - Categories_Dummy.ipynb
    
- Modeling for Movies already released
    - Modeling_with_male_score.ipynb
    
- Modeling for Movies with upcoming release
    - Modeling_with_Metascore.ipynb
    
- Modeling for Movies in pitching or pre-produciton stages
    - Modeling_with_female_predictors.ipynb
    
- Modeling for pre-production with Male IMDB Score target
    - Modeling_with_male_predictors.ipynb
