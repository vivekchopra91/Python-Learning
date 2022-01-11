import time
from plyer import notification

if __name__ == "__main__":
    while True:

        notification.notify(
            title = "Please Drink Water Now!",
            message = "Drinking enough water offers health benefits, however, drinking too much water, such as 3-4 liters of water, in a short period leads to water intoxication. For proper metabolism, a normal human body requires about two liters of water.",
            app_icon = "./icon.ico",
            timeout = 2
        )
        time.sleep(6)