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


@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'Application is running'})


@app.route('/demo_job', methods=['GET'])
def start_job():
    job_id = 'demo_job'
    # scheduler.add_job(my_scheduled_job, 'cron', second=1)  # Runs at specific time
    scheduler.add_job(jobs.my_scheduled_job, 'interval', seconds=1, id=job_id)  # Schedule job_function to be called every minute
    return jsonify({'status': 'Job added successfully'})


@app.route('/job_listings', methods=['GET'])
def send_joblistings():
    job_id = 'job_listings'
    trigger = CronTrigger(day_of_week='mon', hour=9) # Schedule the job to run at 9 AM every Monday
    scheduler.add_job(jobs.job_listings, args=(app,), trigger=trigger, id=job_id) 
    return jsonify({'status': 'Job added successfully'})


@app.route('/stop_job/<job_id>', methods=['GET'])
def stop_job(job_id):
    try:
        scheduler.remove_job(job_id)  # Stop the specific job using its job_id
        return jsonify({'status': f'Job {job_id} stopped successfully'})
    except Exception as e:
        return jsonify({
            'error': f'Error stopping job',
            'message': f'{str(e)}'
            })


@app.route('/stop_jobs', methods=['GET'])
def stop_all_jobs():
    scheduler.remove_all_jobs()  # Stop all jobs
    return jsonify({'status': 'All jobs stopped'})


if __name__ == '__main__':
    app.run(debug=True)
