#!/usr/bin/env python3

import datetime
import time
import requests

from send_message import gmail_send_message

while True:

    content = ""

    res = requests.get("https://webapi.xanterra.net/v1/api/availability/hotels/glaciernationalparklodges?date=07%2F05%2F2024&limit=1&rate_code=INTERNET&is_group=false&nights=1")


    max_price_1 = res.json()["availability"]['07/05/2024']['GLMG']['max']
    min_price_1 = res.json()["availability"]['07/05/2024']['GLMG']['min']


    content = content + "max: %s" % (max_price_1) + "\n"

    content = content + "min: %s" % (min_price_1) + "\n"

    content = content + "https://secure.glaciernationalparklodges.com/booking/lodging-search?dateFrom=07-05-2024&adults=2&children=0&nights=1&destination=ALL"

    # print("max: %s" % (res.json()["availability"]['07/05/2024']['GLMG']['max']))
    # print("min: %s" % (res.json()["availability"]['07/05/2024']['GLMG']['min']))

    content = content + "\n\n\n"


    res = requests.get("https://webapi.xanterra.net/v1/api/availability/hotels/glaciernationalparklodges?date=07%2F06%2F2024&limit=1&rate_code=INTERNET&is_group=false&nights=1")


    max_price_2 = res.json()["availability"]['07/06/2024']['GLMG']['max']
    min_price_2 = res.json()["availability"]['07/06/2024']['GLMG']['min']


    content = content + "max: %s" % (max_price_2) + "\n"

    content = content + "min: %s" % (min_price_2) + "\n"

    content = content + "https://secure.glaciernationalparklodges.com/booking/lodging-search?dateFrom=07-06-2024&adults=2&children=0&nights=1&destination=ALL"


    # print("max: %s" % (res.json()["availability"]['07/06/2024']['GLMG']['max']))
    # print("min: %s" % (res.json()["availability"]['07/06/2024']['GLMG']['min']))

    if max_price_1 != 0 or max_price_2 != 0 or min_price_1 != 0 or min_price_2 != 0:
        gmail_send_message(content)

    print("[%s] Finish query, max: [%s], min: [%s], max: [%s], min: [%s]" % (datetime.datetime.now(), max_price_1, min_price_1, max_price_2, min_price_2))
    time.sleep(60 * 5)