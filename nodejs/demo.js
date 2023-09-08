// Scheduling a simple task with node cron.
const cron = require('node-cron');
const express = require("express");

const app = express();

// cron.schedule('* * * * *', () => {
//     console.log('Cron Job is running every minute!');
// });

cron.schedule('*/2 * * * * *', () => {
    console.log("---------------------");
    console.log("Cron Job is running every 2 seconds");
});

app.listen(3000);
