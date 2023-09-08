require('dotenv').config();
const nodemailer = require('nodemailer');

let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAILUSER,
      pass: process.env.EMAILPASS
    }
})

function mailService(recipients) {
    let mailOptions = {
        from: 'process.env.EMAILUSER',
        to: recipients,
        subject: 'Node Cron',
        text: `Hello, this is a test email from Node Cron.`
    };
    transporter.sendMail(mailOptions, (err, info) => {
      if (err) {
        console.error('Error sending email:', err.message);
      } else {
        console.log('Email sent successfully');
      }
    });
}

module.exports = {mailService};