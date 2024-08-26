
import os

from dotenv import load_dotenv

load_dotenv()

# google credentials:
DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)
