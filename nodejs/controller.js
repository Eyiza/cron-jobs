require('dotenv').config();
const cron = require('node-cron');
const nodemailer = require('nodemailer');

let job;

let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAILUSER,
      pass: process.env.EMAILPASS
    }
})

let recipients = ['cronjob@mailinator.com']
let mailOptions = {
    from: 'process.env.EMAILUSER',
    to: recipients,
    subject: 'Node Cron',
    text: `Hello, this is a test email from Node Cron.`
};

// Function to start a cron job that runs every 5 seconds
function startCronJob(req, res) {
    console.log('Cron job started');
    res.send('Cron job started\n')
    job = cron.schedule('*/5 * * * * *', async () => {
    try {   
        transporter.sendMail(mailOptions, (err, info) => {
            if (err) {
              console.error('Error sending email:', err.message);
            } else {
              console.log('Email sent successfully');
            }
        });
    } catch (err) {
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
}


module.exports = {
    start: startCronJob,
    stop: stopCronJob
};