import requests
import URL
import data 

def post_new_order(body):
    return requests.post(URL.URL_SERVICE + URL.CREATE_ORDER,
                         json=body)
response = post_new_order(data.order_body)

def get_order(track_number):   
    return requests.get(URL.URL_SERVICE + URL.GET_ORDER_BY_TRACK,
                        params={"t": track_number})



