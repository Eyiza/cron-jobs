from flask import Flask, jsonify, current_app
from apscheduler.schedulers.background import BackgroundScheduler # Initialize APScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from config import Config 
import mailservice 
import jobs

app = Flask(__name__)
app.config.from_object(Config) 

scheduler = BackgroundScheduler()
scheduler.start()

# Initialize the mail service
mailservice.init_app(app)


@app.route('/start_job', methods=['GET'])
def start_job():
    # scheduler.add_job(my_scheduled_job, 'cron', second=1)  # Runs at specific time
    scheduler.add_job(jobs.my_scheduled_job, 'interval', seconds=1)  # Schedule job_function to be called every minute
    return jsonify({'status': 'Job added successfully'})


@app.route('/job_listings', methods=['GET'])
def send_joblistings():
    with app.app_context():
        # Schedule the job to run at 9 AM every Monday
        trigger = CronTrigger(day_of_week='fri', hour=8, minute=41)
        scheduler.add_job(jobs.job_listings, trigger=trigger) 
        # jobs.job_listings()
        return jsonify({'status': 'Job added successfully'})


@app.route('/stop_jobs', methods=['GET'])
def stop_job():
    scheduler.remove_all_jobs()  # Stop all jobs
    return jsonify({'status': 'All jobs stopped'})


if __name__ == '__main__':
    app.run(debug=True)
