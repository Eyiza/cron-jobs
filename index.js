const express = require('express');
const router = require('./routes.js');

const app = express();

app.use('/', router); // Use the router

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
