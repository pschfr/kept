#!/usr/bin/env python3

# import system modules
import os
import json

# import and initiate dotenv
from dotenv import load_dotenv
load_dotenv()

# import and initiate the Google Keep API
import gkeepapi
keep = gkeepapi.Keep()

# attempt to load note cache from file
cache_exists = os.path.isfile('keep_cache.json')

# if file exists,
if cache_exists:
	# read it...
	fh = open('keep_cache.json', 'r')
	# and parse the JSON.
	state = json.load(fh)
	# login to Google Keep, passing the cache to login
	success = keep.login(os.getenv('GOOGLE_USERNAME'), os.getenv('GOOGLE_PASSWORD'), state=state)

# otherwise,
else:
	# login to Google Keep first,
	success = keep.login(os.getenv('GOOGLE_USERNAME'), os.getenv('GOOGLE_PASSWORD'))
	# then dump the current state
	state = keep.dump()
	# and write it to a file.
	fh = open('keep_cache.json', 'w')
	json.dump(state, fh)

# Now fetch all notes and labels.
g_all_notes = keep.all()
g_notes = keep.find(archived=False, trashed=False)
g_labels = keep.labels()

# Simple loop over notes
for g_note in g_notes:
	print(g_note.title)

# sync to be up to date
keep.sync()
