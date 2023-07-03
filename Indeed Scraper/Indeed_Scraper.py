import search_criteria
import time
import sys
import random
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup #webscrape
from collections import defaultdict #default dictionary: store a list with each key
import pandas as pd  #DF
import openpyxl
import re   #regular expressions
import datetime     #format date/time

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")

start_time = time.time()

job_titles = search_criteria.job_titles
locations = search_criteria.locations
max_pages = search_criteria.pages
good_experience = list(set(search_criteria.good_experience))
bad_experience = list(set(search_criteria.bad_experience))
good_education = list(set(search_criteria.good_education))
bad_education = list(set(search_criteria.bad_education))
good_skills = list(set(search_criteria.good_skills))
bad_skills = list(set(search_criteria.bad_skills))

min_delay = search_criteria.min_delay
max_delay = search_criteria.max_delay
actual_max = max_delay + 1 # Adjusted max delay for calculating time estimates

file_path = search_criteria.file_path
wait_user_input = search_criteria.wait_user_input

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
job_urls = set()
job_dates_dict = {} #Dictionary to store dates corresponding to urls

max_job_pages = len(job_titles) * len(locations) * max_pages # Theoretical max number of pages for finding jobs
max_links = max_job_pages * 15 # Theoretical max number of jobs if every page is unique

max_stage_one_time = (max_links / 15) * (actual_max)
max_stage_two_time = max_links * (actual_max)
max_time = max_stage_one_time + max_stage_two_time
print("Max Stage One Estimated Time = " + str(max_stage_one_time) + " seconds.")
print("Max Total Estimated Time = " + str(max_time) + " seconds. Beginning job scraping")

progress_bar = tqdm(total = max_job_pages, unit = "iteration")

def calculate_score(good_phrases, bad_phrases, description):
    score = 0
    count = 0
    for phrase in good_phrases:
        if phrase.lower() in description.lower():
            score += 1
            count += 1
    for phrase in bad_phrases:
        if phrase.lower() in description.lower():
            score += -1
            count += 1
    return score, count

for job in job_titles:
    #Go through each job title
    for location in locations:
        #Go through each location
        for page in range(max_pages):

            url = "https://indeed.com/jobs?q=" + job + "&l=" + location + "&start=" + str(page * 10)
            # "&sort=date" + Removed this to hopefully fix issues.
            driver.get(url)
          
            time.sleep(random.randint(min_delay, max_delay) + (random.randint(0, 99) / 100)) # Picks between min and max, adds a random decimal
            progress_bar.update(1)

            html = driver.page_source

            # Scrapping the web
            soup = BeautifulSoup(html, "lxml")

            # Outer most entry point of HTML:
            outer_most_point = soup.find("div", attrs={"id":"mosaic-provider-jobcards"})

            for post in outer_most_point.find("ul"):
                job_link_element = post.find("a")
                #job_link_element = post.find("a",{"class":"jcs-JobTitle"})["href"]
                if job_link_element != None and "href" in job_link_element.attrs:
                    #job_link = "https://indeed.com/" + post.find("a",{"class":"jcs-JobTitle"})["href"]
                    job_link = "https://indeed.com/" + job_link_element["href"]
                    if job_link not in job_urls:
                        job_urls.add(job_link)

                        job_date_element = post.find("span", attrs={"class": "date"})
                        if job_date_element != None:
                            job_date = job_date_element.text
                        else:
                            job_date = "None"
                        job_dates_dict[job_link] = job_date

progress_bar.close()
job_urls = list(job_urls)
num_links = len(job_urls)
num_dates = len(job_dates_dict)
if num_links != num_dates:
    print("Mismatch on dates and links. Closing now.")
    sys.exit(1)
print("\nNumber of Links Gathered = " + str(num_links) + " of " + str(max_links) + " possible.")

# Code for iterating over job URLS
print("Scraping is beginning")
data_title = []
data_company = []
data_location = []
data_date = []
data_link = []
data_exp_score = []
data_exp_phrases = []
data_edu_score = []
data_edu_phrases = []
data_skill_score = []
data_skill_phrases = []
data_total_score = []
data_total_phrases = []

progress_bar = tqdm(total = num_links, unit = "iteration")

for link in job_urls:
    driver.get(link)
    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")

    job_title_element = soup.find("h1", class_="jobsearch-JobInfoHeader-title")
    if job_title_element != None:
        job_title = job_title_element.text.strip()
    else:
        job_title = "No title"

    company_element = soup.find("div", attrs={"data-company-name": "true"})
    if company_element != None:
        company = company_element.text.strip()
    else:
        company = "No company"
        
    location_element = soup.find("div", class_="css-6z8o9s eu4oa1w0")
    if location_element != None:
        location = location_element.text.strip()
    else:
        location = "No location"

    posting_date = job_dates_dict[link]

    job_description = ""
    description_element = soup.find('div', id='jobDescriptionText')
    if description_element != None:
        job_description = description_element.text.strip()

        job_exp_score, job_exp_phrases = calculate_score(good_experience, bad_experience, job_description)
        job_edu_score, job_edu_phrases = calculate_score(good_education, bad_education, job_description)
        job_skills_score, job_skills_phrases = calculate_score(good_skills, bad_skills, job_description)
    else:
        job_description = "Description invalid"
        job_exp_score = -99
        job_exp_phrases = -99
        job_edu_score = -99
        job_edu_phrases = -99
        job_skills_score = -99
        job_skills_phrases = -99

    total_score = job_exp_score + job_edu_score + job_skills_score
    total_phrases = job_exp_phrases + job_edu_phrases + job_skills_phrases

    data_title.append(job_title)
    data_company.append(company)
    data_location.append(location)
    data_date.append(posting_date)
    data_link.append(link)
    data_exp_score.append(job_exp_score)
    data_exp_phrases.append(job_exp_phrases)
    data_edu_score.append(job_edu_score)
    data_edu_phrases.append(job_edu_phrases)
    data_skill_score.append(job_skills_score)
    data_skill_phrases.append(job_skills_phrases)
    data_total_score.append(total_score)
    data_total_phrases.append(total_phrases)

    time.sleep(random.randint(min_delay, max_delay) + (random.randint(0, 99) / 100))
    progress_bar.update(1)

progress_bar.close()
time.sleep(0.1)
data = {
    "Title": data_title,
    "Company": data_company,
    "Location": data_location,
    "Date Posted": data_date,
    "Link": data_link,
    "Experience Score": data_exp_score,
    "Experience Phrases": data_exp_phrases,
    "Education Score": data_edu_score,
    "Education Phrases": data_edu_phrases,
    "Skills Score": data_skill_score,
    "Skills Phrases": data_skill_phrases,
    "Total Score": data_total_score,
    "Total Phrases": data_total_phrases
    }

df = pd.DataFrame(data)

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

# Convert the DataFrame to an Excel object
df.to_excel(writer, sheet_name='Job_Scores', index=False)

# Access the workbook and worksheet objects
workbook = writer.book
worksheet = writer.sheets['Job_Scores']

# Format the data as a table
worksheet.add_table(0, 0, df.shape[0], df.shape[1] - 1, {'name': 'Job_Scores', 'columns': [{'header': col} for col in df.columns]})

# Save the workbook
writer.close()

print("\nScraping finished")