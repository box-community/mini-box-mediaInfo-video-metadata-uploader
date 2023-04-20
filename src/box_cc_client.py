from boxsdk import Client, CCGAuth

import config

def get_cc_client():
    auth = CCGAuth(
    client_id=config.client_id,
    client_secret=config.client_secret,
    enterprise_id=config.enterprise_id
    )
    client = Client(auth)

    return client