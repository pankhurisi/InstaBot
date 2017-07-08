from paralleldots.config import set_api_key, get_api_key
import requests
import json


def get_parallel_dots_keyword(text, api_key_generated):
    print text
    print type(text)
    set_api_key("fhT5stjJBkAIpe5ftBQJQBFMnamtgazeW5ZDlLYVTMc")
    if not api_key_generated == None:
        if type(text) != str:
            print "Input should be string"
        elif text == "":
            print "Input cannot be empty"

        parallel_dots_url = "https://paralleldots.com/keywords"
        user_info = requests.post(parallel_dots_url, data={"api_key_generated": api_key_generated, "q": text})
        if user_info.status_code != 200:
            print ""
        user_info = {"keywords": json.loads(user_info.content)}
        print user_info['keywords']
    else:
        print "The api key does not exist "
