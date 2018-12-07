import requests
import json

web_hook_url= "path"

slack_msg = {"text": "hello from python" "text": "pageralert duity"}
requests.post(web_hook_url,data=json.dumps(slack_msg))
