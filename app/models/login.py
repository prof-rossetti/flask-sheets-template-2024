
from app.db import BaseModel

class Login(BaseModel):

    SHEET_NAME = "logins"

    COLUMNS = ["email", "verified", "first_name", "last_name", "profile_photo_url"]
