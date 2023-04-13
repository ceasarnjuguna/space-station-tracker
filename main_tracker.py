import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -1.2746752  # Your latitude
MY_LONG = 36.847616  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def location():
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 or MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

status = True


def iss_tracker():
    global status
    if location() and hour >= sunset or hour <= sunrise:
        my_email = ""
        password = ""

        with smtplib.SMTP("smtp.gmail.com") as connection:  # url of the smpt server we are using
            # securing connection to the email server
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="",
                                msg="Subject:ISS\n\n Look Up😜")
        status = False


while status:
    iss_tracker()
    time.sleep(60)
