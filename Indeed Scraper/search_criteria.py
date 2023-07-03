# Type how many pages you want to search for each job + location pairing.
pages = 5
# Type the minimum and maximum delay in seconds between refreshing pages. Lower = faster, but higher chance of captcha blocking and being a nuisance. 
min_delay = 2 
max_delay = 2 
# Type file path for where the Excel file should be stored.
file_path = "D:/Professional Work/job_scores.xlsx"

# List out job titles that you want to search (Ex. Software Developer)
job_titles = [
    "Software Developer",

    ]

# List out locations you want to search (Ex. New York City, NY) Note: Remote can be very tricky and yield not great results. 
locations = [
    "New York City, NY",

    ]

# List out phrases that are beneficial in terms of experience (Ex. 0-3 years of experience)
good_experience = [
    "0-3 years",

    ]

# List out phrases that are detrimental in terms of experience (Ex. 10+ years)
bad_experience = [
    "10+ years",
  
    ]

# List out phrases that match your education level (Ex. software engineering)
good_education = [
    "software engineering",
 
    ]

# List out phrases that don't match your education level (Ex. Doctorate)
bad_education = [
    "doctorate",
   
    ]

# List out phrases that match your skillset (Ex. Python)
good_skills = [
    "Python",
    
    ]

# List out phrases that don't match your skillset (Ex. JavaScript) Note: A lot harder to fill out than other categories, but just keep an eye on what skills jobs want that you don't/won't have.
bad_skills = [
    "JavaScript",

    ]

