import json


def get_request_type(payload):
    data = json.loads(payload)
    if data["entry"][0]["messaging"][0].get('postback'):
        return "postback"

    elif "messaging" in data["entry"][0]["messaging"][0]:
        return "message"

    try:
        if data["entry"][0]["messaging"][0]['message']['quick_reply'].get('payload'):
            return "postback"
    except KeyError:
        return "message"


def postback_events(payload):
    data = json.loads(payload)
    postbacks = data["entry"][0]["messaging"]

    for event in postbacks:
        sender_id = event["sender"]["id"]
        if data["entry"][0]["messaging"][0].get('postback'):
            postback_payload = event["postback"]["payload"]
        else:
            try:
                postback_payload = event["message"]["quick_reply"]["payload"]
            except KeyError:
                pass
        yield sender_id, postback_payload


def messaging_events(payload):
    data = json.loads(payload)

    messaging_events = data["entry"][0]["messaging"]

    for event in messaging_events:
        sender_id = event["sender"]["id"]

        # Not a message
        if "message" not in event:
            yield sender_id, None

        if "message" in event and "text" in event["message"] and "quick_reply" not in event["message"]:
            data = event["message"]["text"].encode('unicode_escape')
            yield sender_id, {'type': 'text', 'data': data, 'message_id': event['message']['mid']}

        elif "attachments" in event["message"]:
            if "location" == event['message']['attachments'][0]["type"]:
                coordinates = event['message']['attachments'][
                    0]['payload']['coordinates']
                latitude = coordinates['lat']
                longitude = coordinates['long']

                yield sender_id, {'type': 'location', 'data': [latitude, longitude],
                                  'message_id': event['message']['mid']}

            elif "audio" == event['message']['attachments'][0]["type"]:
                audio_url = event['message'][
                    'attachments'][0]['payload']['url']
                yield sender_id, {'type': 'audio', 'data': audio_url, 'message_id': event['message']['mid']}

            else:
                yield sender_id, {'type': 'text', 'data': "I don't understand this",
                                  'message_id': event['message']['mid']}

        elif "quick_reply" in event["message"]:
            data = event["message"]["quick_reply"]["payload"]
            yield sender_id, {'type': 'quick_reply', 'data': data, 'message_id': event['message']['mid']}

        else:
            yield sender_id, {'type': 'text', 'data': "I don't understand this", 'message_id': event['message']['mid']}
