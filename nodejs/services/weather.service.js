require('dotenv').config();
const axios = require('axios');
const WEATHER_API_KEY = process.env.WEATHER_API_KEY;


async function weatherService(city) {
    try {
        const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${WEATHER_API_KEY}`);
        const { name, main: { temp, humidity } } = response.data;
        const message = `The weather in ${name} is ${temp} degrees with ${humidity}% humidity.`;
        return message;
    } catch (err) {
        console.error(err.message);
        return err.message;
    }
}


module.exports = { weatherService };
