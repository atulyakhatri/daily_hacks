# Importing modules
import time
from plyer import notification


if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Take a brake",
            message = "Drink water!",
    	    app_icon = r"C:\Users\user\clock_1019.ico",
            app_name = "Timer",
            toast = True,
 	    )
        time.sleep(40*60) #In seconds
