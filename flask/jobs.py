import mailservice 
import scraper
from flask import render_template_string


def my_scheduled_job():
    print("Cron job executed!")

def job_listings(app):
    with app.app_context():
        scraped_jobs = scraper.scrape_jobs()

        # Load the email template
        with open('template.html', 'r') as template_file:
            email_template = template_file.read()

        template = render_template_string(email_template, jobs=scraped_jobs)
        
        recipient = 'jobs@mailinator.com'
        subject = "Job Listings"
        sender = "Google Careers Scraping"
        
        mailservice.send_email(recipient, subject, template, sender)
        print ('Email sent successfully')
