import requests
import json

web_hook_url = ""

image_url = "http://cdn.cloudinary.com/demo/image/upload/w_400/hungry_cat.jpg"
slack_msg = {"username": "ankit",
             "text": "When it is time for lunch, please remember not to delay and go ahead to have lunch. Other wise you will miss the salad, Dessert",
             "attachments": [
                 {
                     "color": "good",
                     "image_url": "http://funkyimg.com/i/2P2CM.png"
                 }
             ]
             }
requests.post(web_hook_url, data=json.dumps(slack_msg), headers={'Content-Type': 'application/json'})
