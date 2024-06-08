import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
def initialize_db():
    # Path to your service account key JSON file
    cred = credentials.Certificate("Users/dbutt/myweather/data/myweather-f2d76-firebase-adminsdk-vszkx-edd5d23e26.json")
    
    # Initialize the Firebase app with the service account
    firebase_admin.initialize_app(cred)
    
    # Get a Firestore client
    global db
    db = firestore.client()

# Function to save user preferences to Firestore
def save_user_preferences(location):
    doc_ref = db.collection('user_preferences').document('preferences')
    doc_ref.set({
        'location': location
    })
