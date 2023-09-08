const router = require('express').Router();
const controller = require('./controller.js')

router
    .get('/startmail', controller.startMailCronJob)
    .get('/startsms', controller.startSmsCronJob)
    .get('/stopmail', controller.stopMailCronJob)
    .get('/stopsms', controller.stopSmsCronJob)
       

module.exports = router;