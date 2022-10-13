from win10toast import ToastNotifier
import time
import requests
import json

toaster = ToastNotifier()

def dictionary_content():
    api_url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(api_url)
    content = response.content.decode('utf-8')
    dict_content = json.loads(content)
    return dict_content

def show_toaster():
    content = dictionary_content()

    toaster.show_toast(content['type'],
                        content['activity'],
                        duration=5)
    while toaster.notification_active():
        time.sleep()

while True:
   show_toaster()()
   time.sleep(5)
