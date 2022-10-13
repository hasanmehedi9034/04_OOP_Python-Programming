from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
toaster.show_toast("Hello Programmers!!!",
                   "Python is really awesome, I am here for 10 seconds!",
                   icon_path="Downloads-Black-Folder.ico",
                   duration=2)

toaster.show_toast("Good morning Dear",
                   "How are you today?",
                   icon_path=None,
                   duration=5,
                   threaded=True)

# Wait for threaded notification to finish
while toaster.notification_active(): 
    time.sleep()