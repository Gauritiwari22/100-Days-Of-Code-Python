"Day 33"
"Undertsanding basics of APIs and Day33 learnings"

# APIs allow your Python program to communicate with external services over the internet. 
# Instead of storing all data locally, you request data from a server, a
# nd the server responds with structured information, usually in JSON format.
#  This enables real-time features like weather apps, trackers, or notifications.

# HTTP requests are the way clients talk to servers. 
# A GET request asks for data, while POST sends data. In this lesson, most interactions use GET requests to fetch information from public APIs.
#  Every request returns a response with a status code that indicates success or failure.

# The requests library simplifies sending HTTP requests in Python. It handles connections, responses, and data conversion. 
# After receiving a response, you typically convert it to JSON and treat it like a Python dictionary for easy access.

# JSON is a lightweight data format that looks like nested dictionaries and lists. 
# API responses are parsed into Python objects so you can extract required values using keys.

# Query parameters are extra inputs sent with the request URL to customize results, such as latitude and longitude for weather or sunrise times. 
# Passing parameters as a dictionary is safer and cleaner than manually modifying URLs.

# Error handling is important because network calls can fail. 
# Using built-in methods like raise_for_status() prevents silent bugs by immediately stopping execution when the server returns an error code.