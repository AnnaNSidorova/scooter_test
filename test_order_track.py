import sender_stand_request, data

def get_track_number(body):
    track_number = sender_stand_request.post_new_order(body)
    return track_number.json()["track"]


def test_order_info_by_track():
    track_number = get_track_number(data.order_body)
    get_response = sender_stand_request.get_order(track_number)
    assert get_response.status_code == 200