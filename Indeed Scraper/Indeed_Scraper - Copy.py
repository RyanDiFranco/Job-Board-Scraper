#import search_criteria
#import time
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
#from bs4 import BeautifulSoup #webscrape
#from collections import defaultdict #default dictionary: store a list with each key
#import pandas as pd  #DF
#import re   #regular expressions
#import datetime     #format date/time

#options = Options()
#options.add_experimental_option("detach", True)

#job_titles = search_criteria.job_titles
#locations = search_criteria.locations
#good_phrases = search_criteria.good_phrases
#page_refresh_delay = 0.5

#good_count = 0

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#indeed_posts = []
#for job in job_titles:
#    #Go through each job title
#    for location in locations:
#        #Go through each location

#        for page in range(search_criteria.pages):

#            url = "https://indeed.com/jobs?q=" + job + "&l=" + location + "&sort=date" + "&start=" + str(page * 10)
#            driver.get(url)
#            html = driver.page_source

#            #print(html) #Entire HTML post

#            # Scrapping the web
#            soup = BeautifulSoup(html, "lxml")

#            # Outer most entry point of HTML:
#            outer_most_point = soup.find("div", attrs={"id":"mosaic-provider-jobcards"})

#            time.sleep(page_refresh_delay) #Delay to hopefully not piss off indeed?
#            job_title_count = 0
#            link_count = 0
#            for post in outer_most_point.find("ul"):

#                job_title_element = post.find("h2", class_="jobTitle")
#                if job_title_element != None:
#                    job_title = job_title_element.text.strip()

#                    job_title_count += 1

#                company_element = post.find("span", class_="companyName") 
#                if company_element != None:
#                    company = company_element.text.strip()
                
#                job_link_element = post.find("a")
#                if job_link_element != None:
#                    job_link = "indeed.com/" + post.find("a",{"class":"jcs-JobTitle"})["href"]
#                    link_count += 1

#                job_date_element = post.find("span", attrs={"class": "date"})
#                if job_date_element != None:
#                    job_date = job_date_element.text

#                #job_description_element = post.find("div", class_="job-snippet") #Short form snippet about the job
#                #if job_description_element != None:
#                #    job_description = job_description_element.text.strip()
#                #    print(job_description)


                

           
