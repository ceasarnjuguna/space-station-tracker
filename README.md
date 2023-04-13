**International Space Station Tracker**
This Python script tracks the International Space Station (ISS) and sends an email notification when it is near the user's current location and it is currently dark outside. The script uses the requests library to make API requests to retrieve the ISS position and the user's sunrise/sunset times, and the smtplib library to send email notifications.

**Usage**
To run the script, simply run the iss_tracker.py file in your Python environment:

python iss_tracker.py

The script will run continuously and check the user's location and the ISS position every 60 seconds. If the ISS is within +5 or -5 degrees of the user's position and it is currently dark outside, the script will send an email notification to the specified email address.

**Files**
This project consists of the following file:

iss_tracker.py: Contains the code for the ISS tracker script.

**Requirements**
This project requires the following Python libraries:

requests
datetime
smtplib

You can install these libraries using pip:

pip install requests datetime smtplib

**Configuration**
Before running the script, you need to configure the following variables in the iss_tracker.py file:

MY_LAT: Your latitude
MY_LONG: Your longitude
my_email: Your email address
password: Your email password
to_addrs: The email address to send notifications to

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
This project was inspired by a challenge from the 100 Days of Code course on Udemy