# Cron Jobs

This project consists of a set of scripts that can be used to automate the process of creating and deleting cron jobs. There are two folders `flask` and `nodejs`, each containing different cron jobs implemented using different packages for managing the cron job schedules with specific functionalities.


## Built with
* [Flask](https://flask.palletsprojects.com)
   * [APScheduler](https://apscheduler.readthedocs.io/en/stable/) - A light but powerful in-process task scheduler that lets you schedule functions (or any other python callables) to be executed at times of your choosing.
   * [Flask Mail](https://pythonhosted.org/Flask-Mail/) - A package for Flask that makes it easy to send emails.
* [NodeJS](https://nodejs.org/) and [Express](https://expressjs.com/) 
    * [node-cron](https://www.npmjs.com/package/node-cron) - A package for Node.js that allows you to schedule cron jobs.
    * [nodemailer](https://nodemailer.com/about/) - A module for Node.js applications to allow email sending.
    * [Twilio](https://www.twilio.com/docs/libraries/node) - A module for Node.js applications to allow SMS sending.
    * [OpenWeatherMap](https://openweathermap.org/api) - An API for getting weather updates.

## Getting Started
Download the project code locally
[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. 


## Prerequisites
* [Python 3](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
* [NodeJS](https://nodejs.org/en/download/)
* [npm](https://www.npmjs.com/get-npm)
* [git](https://git-scm.com/downloads)
* [curl](https://curl.haxx.se/download.html)
* [jq](https://stedolan.github.io/jq/download/)
* [Twilio](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account)
* [OpenWeatherMap](https://openweathermap.org/api)


## Flask Cron Jobs
The `flask` folder contains Flask-based cron jobs responsible for web scraping and sending emails. The `APScheduler` package is used to schedule these cron jobs, `BeautifulSoup` for web scraping and `Flask-Mail` for sending emails .The cron jobs are:
1. [Demo](./flask/jobs.py) - This is a simple cron job that runs at regular intervals, specifically every second. It can be used as a template for creating other cron jobs.
2. [Google Career Scraper Cron Job](./flask/jobs.py) - This cron job scrapes Google Careers 9am every Monday and sends an email to a given recipient. 
3. [Variety News Scraper Cron Job](./flask/jobs.py) - This cron job scrapes Variety news every day and sends an email to a given recipient. 


## NodeJS Cron Jobs
The `nodejs` folder contains three cron jobs. The `node-cron` package is used to schedule these cron jobs. The cron jobs are:
1. [`demo.js`](./nodejs/demo.js) - This is a simple cron job that runs at regular intervals, specifically every 2 seconds. It can be used as a template for creating other cron jobs.
2. [Email Cron Job](./nodejs/controller.js) - This cron job sends an email every 5 seconds, demonstrating how to use node-cron to send emails periodically. It uses the `nodemailer` package to send emails.
3. [Weather SMS Cron Job](./nodejs/controller.js) - This cron job sends an SMS of the weather update using Twilio every weekday at 9:45 AM. It uses the Twilio API to send SMS messages.


## Installation
### Flask
Navigate to the [`flask`](./flask) folder.
1. Create a virtual environment for the project
    ```bash
    virtualenv venv
    ```
2. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application
    ```bash
    python app.py
    ```
5. Open the application in your browser 
    ```bash
    http://localhost:5000
    ```
6. To stop the application, press `Ctrl + C`


### NodeJS
Navigate to the [`nodejs`](./nodejs) folder.
1. Install the dependencies
    ```bash
    npm install
    ```
2. Run the application
    ```bash
    npm start
    ```
3. Open the application in your browser
    ```bash
    http://localhost:3000
    ```
4. To stop the application, press `Ctrl + C`

## Configuration
### Flask
Before running the application, you need to configure the following environment variables:
1. `MAIL_USERNAME` - The email address of the sender
2. `MAIL_PASSWORD` - The password of the sender's email address

Create a `.env` file at the `flask` level and add the variables to it (otherwise hard code their strings in [`config.py`](./flask/config.py) file).
```
MAIL_USERNAME=your_email_address
MAIL_PASSWORD=your_email_password
``` 
Other variables that can be updated include:
1. `MAIL_RECIPIENT` - The email address of the recipient


### NodeJS
Before running the application, you need to configure the following environment variables:
1. `EMAILUSER` - The email address of the sender
2. `EMAILPASS` - The password of the sender's email address
3. `TWILIO_ACCOUNT_SID` - The Twilio account SID
4. `TWILIO_AUTH_TOKEN` - The Twilio auth token
5. `TWILIO_PHONE_NUMBER` - The Twilio phone number
6. `WEATHER_API_KEY` - The OpenWeatherMap API key

Create a `.env` file at the `nodejs` level and add the variables to it (otherwise hard code their strings in their respective files).<br>
Other variables that can be updated include:
1. `MAIL_RECIPIENT` - The email address of the recipient
2. `RECIPIENT_PHONE_NUMBER` - The recipient's phone number


## API Endpoints
### Flask
1. `/` - The home page
2. `/demo_job` - The endpoint that starts the demo cron job
3. `/job_listings` - The endpoint that starts the Google Careers cron job
4. `/news` - The endpoint that starts the Variety News cron job
5. `/stop_job/<job_id>` - The endpoint that stops the cron job with the given job ID
6. `/stop_jobs` - The endpoint that stops all the cron jobs


### NodeJS
1. `/startmail` - The endpoint that starts the email cron job
2. `/startsms` - The endpoint that starts the weather cron job
3. `/stopmail` - The endpoint that stops the email cron job
4. `/stopsms` - The endpoint that stops the weather cron job
5. `/stopall` - The endpoint that stops all the cron jobs

**Note** - Curl commands can be used to start and stop the cron jobs. For example, to start the flask demo cron job, run the following command:
```bash
curl http://localhost:5000/demo_job
```
To stop the demo cron job, run the following command:
```bash
curl http://localhost:5000/stop_job/demo_job
``` 


## Author
Precious Michael - [preciousmichael](https://eyiza.github.io/precious-michael/)
