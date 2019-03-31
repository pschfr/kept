#!/usr/bin/env python3

# import modules
from dotenv import load_dotenv
import os
import gkeepapi

# initiate and authenticate
load_dotenv()
keep = gkeepapi.Keep()
success = keep.login(os.getenv('GOOGLE_USERNAME'), os.getenv('GOOGLE_PASSWORD'))

# sync to be up to date
keep.sync()
