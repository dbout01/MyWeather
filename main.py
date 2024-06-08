from .database import initialize_db, save_user_preferences, get_user_preferences
from .weather_api import fetch_weather_data

def main():
    # Initialize the database
    initialize_db()

    # Example usage: save user preferences
    user_id = "user123"  # Unique for each user
    user_location = "Paris"
    save_user_preferences(user_id, user_location)

    # Retrieve user preferences
    preferences = get_user_preferences(user_id)
    if preferences:
        location = preferences['location']
        # Fetch weather data based on user preferences
        weather_data = fetch_weather_data(location)
        if 'error' in weather_data:
            print(weather_data['error'])
        else:
            print(weather_data)
    else:
        print("No preferences found for this user.")

if __name__ == "__main__":
    main()
