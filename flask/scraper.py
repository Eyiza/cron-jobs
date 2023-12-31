import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://www.google.com/about/careers/applications/jobs/results/?q=Software%20Engineer%20internn_US"
    response = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = soup.find_all('li', class_ = 'lLd3Je')

    scraped_jobs = [] 
    count = 0 

    for job in jobs:
        if count == 10:
            break

        title = job.find('h3', class_ = 'QJPWVe').text.strip()
        location = job.find('span', class_ = 'r0wTof').text.strip()
        url = job.find('a')['href']
        job_url = f'https://www.google.com/about/careers/applications/{url}'
        count += 1

        scraped_jobs.append({
            'title': title,
            'location': location,
            'url': job_url
        })

    return scraped_jobs
    

def scrape_news():
    url = "https://variety.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h3', id = 'title-of-a-story')

    scraped_news = [] 
    count = 0 

    for news in articles:
        if count == 10:
            break

        headline = news.text.strip()
        url = news.find('a')['href']
        count += 1

        scraped_news.append({
            'headline': headline,
            'url': url
        })


    return scraped_news
