from bs4 import BeautifulSoup
import requests

html_file=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_file,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date=job.find('span',class_='sim-posted').span.text
    if 'few' in published_date:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','').strip()
        skills_div=job.find('div',class_='more-skills-sections')
        skills=[span.text.strip() for span in skills_div.find_all('span')]
        more_info=job.header.h2.a['href']
        
        print(f"Company name: {company_name}")   
        print(f"Required skills: {skills} ") 
        print(f"More Info:{more_info}")

        print(" ")  
        
        # for job in jobs:
        #     print(job.text)