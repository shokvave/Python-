from credentials import mobile_number
import requests
import schedule
import time


def send_message():
    resp = requests.post('http://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hey good morning sugar',
        'key': 'textbelt'

    })
    print(resp.json())

# schedule.every().day.at('7:15').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
    