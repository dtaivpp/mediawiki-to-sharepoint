# settings.py
from dotenv import load_dotenv
load_dotenv()

import os
Sharepoint_User = os.getenv("SHAREPOINT_USER")
Sharepoint_Pass = os.getenv("SHAREPOINT_PASS")
Sharepoint_Url  = os.getenv("SHAREPOINT_URL")