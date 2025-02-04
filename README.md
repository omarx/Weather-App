# Weather App Python Logger

This is a simple Python application that retrieves and logs daily weather data into a database based on user input for a city. It uses an external weather API to fetch weather details such as temperature, wind speed, and humidity.

## Features
- Fetches latitude and longitude coordinates for a given city.
- Retrieves weather data including temperature, humidity, wind speed, and feels-like temperature.
- Stores the weather data into a PostgreSQL database.
- Provides user feedback on the success or failure of logging weather data.

## Requirements

### Dependencies
Ensure you have the following installed before running the application:
- Python 3.x
- PostgreSQL
- Required Python libraries:
  - `requests`
  - `dotenv`
  - `psycopg2`

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/weather-logger.git
   cd weather-logger
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add your API key and URLs:
   ```
   API_KEY=your_api_key_here
   DATA_URL=https://api.openweathermap.org/data/2.5/weather?
   COORD_URL=https://api.openweathermap.org/geo/1.0/direct?q=
   ```

5. Set up the database:
   Ensure you have a PostgreSQL database running with a table named `forecast`:
   ```sql
   CREATE TABLE forecast (
       id SERIAL PRIMARY KEY,
       latitude VARCHAR(50),
       longitude VARCHAR(50),
       temperature VARCHAR(50),
       feels_like VARCHAR(50),
       humidity VARCHAR(50),
       city VARCHAR(100),
       wind_speed VARCHAR(50),
       date DATE
   );
   ```

## Usage
To run the application, use:
```sh
python app.py
```

Enter a city name when prompted, and the weather data will be fetched and logged into the database.

## Error Handling
- If an API request fails, an error message will be displayed.
- If database insertion fails, an error will be printed.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## Contact
For any questions, please reach out to omarpeart100@gmail.com.

