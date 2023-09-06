from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler # Initialize APScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
from config import Config 
import mailservice 


app = Flask(__name__)
app.config.from_object(Config) 

scheduler = BackgroundScheduler()
scheduler.start()

# Initialize the mail service
mailservice.init_app(app)


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

@app.route('/send_email', methods=['GET'])
def send_email_route():
    recipient = 'precious.michael2002@gmail.com' # Get recipient email from the request data
    subject = "Hello from Your App"
    template = "<p>This is the email content.</p>"
    
    # Call the send_email function to send the email
    mailservice.send_email(recipient, subject, template)
    
    return jsonify({'status': 'Email sent successfully'})

if __name__ == '__main__':
    app.run(debug=True)
