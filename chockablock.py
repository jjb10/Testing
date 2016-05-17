import requests

import time
import json

timeout = time.time() + 20

print "hello"


def play(qty,price):
    header = {"X-Starfighter-Authorization": "be7e75b7f65de58977327c95a0c82e7fb47d6abe"}
    data = {
        "orderType": "limit",
        "qty": qty,
        "direction": "buy",
        "account": "BK15996873",
        "price": price
    }
    r = requests.post("https://api.stockfighter.io/ob/api/venues/WLNBEX/stocks/OLI/orders", data=json.dumps(data),
                      headers=header)
    print r.content
    response = r.json()
    total_filled = response['totalFilled']
    return total_filled



# set target price
qty = 10000
price = 5300

l=[];

while True:
    a = play(qty,price)
    l.append(a)
    x=sum(l)
    time.sleep(2)
    print x
    if x == 100000:
        break
    if a==0:
        price=price+5
    if a>0:
        price=price-30
    time.sleep(0)
    print price



