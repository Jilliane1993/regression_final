#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:25:12 2021

@author: etheredgej
"""


def get_value(soup, field_name):
    
    '''
    Takes a string attribute of a movie on the page and returns the string in
    the next sibling object (the value for that attribute) or None if nothing is found.
    '''
    import re
    obj = soup.find(text=re.compile(field_name))
    
    if not obj: 
        return None
    
    # this works for most of the values
    next_element = obj.findNext()
    
    if next_element:
        return next_element.text 
    else:
        return None
    
def get_movie_dict(link):
    """
    From Imdb link stub, request movie html, parse with BeautifulSoup, and collect:
      
        -Director
        -Stars
        -Budget
        
        -Country of Origin
        -based off novel
        
    Returns info as dictionary
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    
    base_url='https://www.imdb.com/'
    link=link
    
    #url to be scraped
    url=base_url+link
    
    #Request HTML and parse
    response=requests.get(url)
    page=response.text
    soup=BeautifulSoup(page,'html.parser')
    
    headers=['Director','Star','Budget',
            'Country','Novel Adaptation','Link stub']
    
    #director
    director=get_value(soup,'Director')
    
    #Star
    stars=[]
    star=get_value(soup,'Stars:')
    star2_regex=re.compile('Stars:')
    star2=soup.find(text=star2_regex).findNext().findNext().text
    star3_regex=re.compile('Stars:')
    star3=soup.find(text=star3_regex).findNext().findNext().findNext().text
    stars.append(star)
    stars.append(star2)
    stars.append(star3)
    
    #Budget
    bud_str=soup.find('h3',class_='subheading').findNext().text.replace('\nBudget:$','').replace('\n            (estimated)\n','').replace(',','')
    budget=bud_str
    
    
    #Country of origin
    country= get_value(soup,'Country')
    
    #novel adaptation
    novel=soup.find('div',class_='credit_summary_item').findNext().findNext().findNext().text
    adapt=adaptation(novel)
    
    #create dict and return
    movie_dict=dict(zip(headers,[director,
                                stars,
                                budget,
                                country,
                                adapt,link]))
    return movie_dict

def adaptation(novel):
    """returns if a movie is a novel adaptation in a binary value"""
    if "novel" in novel:
        return 1
    else:
        return 0
    
def get_demo_dict(link):
    """
    from Imdb link stub, request movie html, parse with beautiful soup, and collect:
    Male score
    Male total votes
    Female score
    Female total votes
    
    return info as dictionary
    """
    import requests
    from bs4 import BeautifulSoup
    
    base_url=base_url='https://www.imdb.com/'
    url_extension='ratings?ref_=tt_ov_rt'
    link=link
    url=base_url+link+url_extension
    
    response=requests.get(url)
    page=response.text
    soup=BeautifulSoup(page,'html.parser')
    
    headers=['Male Score','Male Total Votes','Female Score','Female Total Votes','Link stub']
    
    #find table with relavent data
    table=soup.find_all('table')
    table=table[1]
    
    #get male score
    
    Male=table.find('div',class_='bigcell').find_parent().find_parent().find_next_sibling().findNext().findNext().findNext().findNext().findNext()
    male_score=Male.text
    
    #get male total votes
    Male_total=Male.findNext().text
    Male_total_final=Male_total.replace("\n\n                    ","").replace("\n                \n","")
    male_total_votes=Male_total_final
    
    #get female score
    Female=table.find('div',class_='bigcell').find_parent().find_parent().find_next_sibling().find_next_sibling().findNext().findNext().findNext().findNext().findNext()
    female_score=Female.text
    
    #get female total votes
    Female_total=Female.findNext().text
    Female_total_final=Female_total.replace("\n\n                    ","").replace("\n                \n","")
    female_total_votes=Female_total_final
    
    #create dict and return
    demo_dict=dict(zip(headers,[male_score,male_total_votes,
                               female_score,female_total_votes,link]))
    return demo_dict
