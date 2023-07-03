# Job-Board-Scraper
 Python command-line application to scrape job board postings for user customized criteria, then rank postings with a final export to Excel.

# About the files
Two main files, search_criteria.py and Indeed_Scraper.py
search_criteria allows you to specify many aspects of the job search and how you should be ranking jobs. This can range from the job title, location, education, experience, and skills. The latter 3 have two lists each, one for good phrases (which will add +1 to a job's score) and bad phrases (which will subtract -1 from a job's score). You can also configure how many pages should be scraped for each combination of job + location. Jobs are sorted by relevancy (would have preferred date, but had issues there) so more pages isn't awful.

# How to run
Configure search_criteria with the number of pages, job titles, and locations you want to search. Add in all of the phrases that you want to look for. Keep in mind that phrases can repeat if you list out two variants, such as "Excel" and "MS Excel". I prefer to default to the shortest, most likely format that a phrase may appear as (so just "Excel" in this case). Set your file location (needs to be a .xlsx file, will create it if it doesn't already exist). Set the min and max delay between refreshes (this determines how fast you will search through pages).
Once criteria are entered, run Indeed_Scraper.py. It can take a lengthy time if you are searching for a ton of jobs, but isn't that intensive. 

# Tips and help
For min and max delay, I have gotten 2 seconds to work (meaning a delay of anywhere from 2 to 2.99 seconds). 
For locations, "Remote" seems to be clunky. Many job postings won't actually be Remote, so you may end up with some jobs that are extremely off from where you are looking.
If you want to search for something that isn't really an experience, education, or skill, you can still throw it in any of those categories. For example, if you really want a job that offers hybrid, you can throw that in any category and it will add to that score. 
The application DOES NOT SAVE until it is fully done, so if you run it for 30 minutes and decide to cancel, you'll get nothing.

# Going forward
Ideally I want to get this scraper to sort by date, as that is most often the most useful listings. Also, it would be ideal to save progress while the application is running, but having it constantly update an Excel sheet seems a bit more tedious than doing it all at once. Ultimately this is just a short project to delve into HTML scraping and learning Python, so I don't expect to expand much.
