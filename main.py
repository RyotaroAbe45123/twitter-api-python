import os

from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session


def initial_settings() -> dict:
    load_dotenv()
    env_dict = {
        "API_KEY": os.getenv("API_KEY", None),
        "API_KEY_SECRET": os.getenv("API_KEY_SECRET", None),
        "ACCESS_TOKEN": os.getenv("ACCESS_TOKEN", None),
        "ACCESS_TOKEN_SECRET": os.getenv("ACCESS_TOKEN_SECRET", None),
        "BEARER_TOKEN": os.getenv("BEARER_TOKEN", None),
        "CLIENT_ID": os.getenv("CLIENT_ID", None),
        "CLIENT_SECRET": os.getenv("CLIENT_SECRET", None),
    }
    assert not [v for v in env_dict.values() if v is None], "Invalid Env File"
    return env_dict

def main():
    settings = initial_settings()

    api = OAuth1Session(
        settings["API_KEY"], settings["API_KEY_SECRET"], settings["ACCESS_TOKEN"], settings["ACCESS_TOKEN_SECRET"]
    )

    endpoint = "https://api.twitter.com/2/tweets"

    payload = {
        "text": "hello from twitter api v2"
    }

    res = api.post(
        endpoint,
        json=payload
    )

    print(res.status_code)
    print(res.json())


if __name__ == "__main__":
    main()