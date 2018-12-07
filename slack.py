import requests
import json

web_hook_url= "https://hooks.slack.com/services/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"

slack_msg = {"text": "hello from python" "text": "pageralert duity"}
requests.post(web_hook_url,data=json.dumps(slack_msg))
