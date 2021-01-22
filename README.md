# Predicting Horror Movie IMDB Scores for a Female Audience


**Description**
In my Metis linear regression project I created models for predicting the IMDB score for horror movies with a female audience. I focused on creating models for 3 potential use cases for the models; predicting the score of a film already released, a film that has not yet been released, and a film that is still in the pitching or pre-production stages. My final models used GridSearchCV with Ridge Regression, however I also used GridSearchCV with Lasso Regression to view my most important features for each model.

**Features and Target Variables**
Target Variable
- Women's IMDB Score

Features
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
    
**Data Used**
- IMDB Horror Movies with 10,000 or more votes

**Tools Used**
- BeautifulSoup
- Seaborn
- Pandas
- GridSearchCV
- Lasso Regression
- Ridge Regression
- Robust Scaler
- Standard Scaler

**Possible impacts**

Depending on the use these models could be use to predict potential positive audience response for adding a movie to a streaming service, screening a new movie at a theater, or when determining to fund a pitch movie. 


**Guide to the Repo**

Presentation Slides

- RegressionPresentationJNE.pdf

Functions used

- my_functions.py

Webscraping

- Testing BeautifulSoup and inital scraping
    - Initial_scraping.ipynb
    
- Scraping for specific plot tags
    - Cultfilm.ipynb
    - FemaleProtagonist.ipynb
    - Monsters.ipynb
    - Murder_tag.ipynb
    
- Scraping votes tables
    - Tablescrape.ipynb
    
- Merging scraping dataframes and most of EDA
    - Page_Scraping_And_EDA.ipynb
    
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