const cron = require('node-cron');
const {mailService} = require('./services/mail.service');
const {smsService} = require('./services/sms.service');
const {weatherService} = require('./services/weather.service');

let job;

// Function to start a cron job that runs every 5 seconds
// function startCronJob(req, res) {
//     console.log('Cron job started');
//     res.send('Cron job started\n')
//     job = cron.schedule('*/5 * * * * *', async () => {
//     try {   
//         recipients = ['cronjob@mailinator.com']
//         mailService(recipients);
        
//     } catch (err) {
//         console.error(err.message);
//         }
//     })
// };


async function startCronJob(req, res) {
    console.log('Cron job started');
    res.send('Cron job started\n')
    job = cron.schedule('*/5 * * * * *', async () => {
    try {   
        recipients = ['+2348036525904']
        message = await weatherService('Lagos');
        smsService(recipients, message);
    }
    catch (err) {
        console.error(err.message);
        }
    })
};

// Function to stop the cron job
function stopCronJob(req, res) {
  if (job) {
    job.stop();
    console.log('Cron job stopped');
    res.send('Cron job stopped\n');
  }
};


module.exports = {
    start: startCronJob,
    stop: stopCronJob
};