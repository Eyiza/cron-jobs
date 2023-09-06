from flask import Flask, jsonify

app = Flask(__name__)

# Initialize APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def my_scheduled_job():
    print("Cron job executed!")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/start_job', methods=['GET'])
def start_job():
    # scheduler.add_job(my_scheduled_job, 'cron', second=1)  # Runs at specific time
    scheduler.add_job(my_scheduled_job, 'interval', minutes=1)  # Schedule job_function to be called every minute
    return jsonify({'status': 'Job started successfully'})

@app.route('/stop_job', methods=['GET'])
def stop_job():
    scheduler.remove_all_jobs()  # Stop all jobs
    return jsonify({'status': 'All jobs stopped'})

if __name__ == '__main__':
    app.run(debug=True)
