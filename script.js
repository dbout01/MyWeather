function fetchWeather() {
    const location = document.getElementById('locationInput').value;
    const apiKey = '93c5c74f2ef46cb3722057f1f93d5144';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&APPID=${apiKey}&units=metric`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Weather data not found');
            }
            return response.json();
        })
        .then(data => displayWeather(data))
        .catch(error => console.error('Error:', error));
}

function displayWeather(data) {
    const weather = document.getElementById('weatherResult');
    weather.innerHTML = `<h2>Weather in ${data.name}</h2>
                         <p>Temperature: ${data.main.temp} °C</p>
                         <p>Weather: ${data.weather[0].main}</p>
                         <p>Humidity: ${data.main.humidity}%</p>
                         <p>Wind speed: ${data.wind.speed} m/s</p>`;
}
