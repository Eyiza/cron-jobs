const router = require('express').Router();
const controller = require('./controller.js')

router
    .get('/start-cron', controller.start)
    .get('/stop-cron', controller.stop)    

module.exports = router;