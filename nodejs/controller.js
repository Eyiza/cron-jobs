const cron = require('node-cron');
const {mailService} = require('./services/mail.service');
const {smsService} = require('./services/sms.service');
const {weatherService} = require('./services/weather.service');

let mailJob;
let smsJob;


// Function to start a cron job that runs every 5 seconds
exports.startMailCronJob = async(req, res) => {
    console.log('Mail Cron job started');
    res.send('Mail Cron job started\n')
    mailJob = cron.schedule('*/5 * * * * *', async () => {
    try {   
        recipients = ['cronjob@mailinator.com']
        await mailService(recipients);
        
    } catch (err) {
        console.error(err.message);
        }
    })
};


exports.startSmsCronJob = async(req, res) => {
    console.log('SMS Cron job started');
    res.send('SMS Cron job started\n')
    // job that runs every weekday at 9:45am
    smsJob = cron.schedule('45 9 * * 1-5', async () => {
    try {   
        recipients = ['+2348036525904']
        message = await weatherService('Lagos');
        await smsService(recipients, message);
    }
    catch (err) {
        console.error('Error sending SMS:', err.message);
      }
    })
};


// Function to stop the mail cron job
exports.stopMailCronJob = (req, res) => {
  if (mailJob) {
      mailJob.stop();
      console.log('Mail Cron job stopped');
      res.send('Mail Cron job stopped\n');
  } else {
      console.log('Mail Cron job is not running');
      res.send('Mail Cron job is not running\n');
  }
}

// Function to stop the SMS cron job
exports.stopSmsCronJob = (req, res) => {
  if (smsJob) {
      smsJob.stop();
      console.log('SMS Cron job stopped');
      res.send('SMS Cron job stopped\n');
  } else {
      console.log('SMS Cron job is not running');
      res.send('SMS Cron job is not running\n');
  }
}

// Function to stop all cron jobs
exports.stopAllCronJobs = (req, res) => {
  if (mailJob) {
      mailJob.stop();
      console.log('Mail Cron job stopped');
      // res.write('Mail Cron job stopped\n');
  }
  if (smsJob) {
      smsJob.stop();
      console.log('SMS Cron job stopped');
      // res.write('SMS Cron job stopped\n');
  } 
  res.send('All Cron jobs stopped\n');
}
