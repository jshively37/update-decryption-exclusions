import os
import requests
import yaml

from dotenv import load_dotenv

BASE_AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"
EXCLUSION_URL = (
    "https://api.sase.paloaltonetworks.com/sse/config/v1/decryption-exclusions"
)

INPUT_FILE = "exclusions.yaml"

HEADERS = {
    "Accept": "application/json",
}

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}

load_dotenv()
TSG_ID = os.environ.get("TSG_ID")
CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")


def create_token():
    auth_url = f"{BASE_AUTH_URL}?grant_type=client_credentials&scope:tsg_id:{TSG_ID}"

    token = requests.request(
        method="POST",
        url=auth_url,
        headers=AUTH_HEADERS,
        auth=(CLIENT_ID, SECRET_ID),
    ).json()
    HEADERS.update({"Authorization": f'Bearer {token["access_token"]}'})


def update_decrpytion_exclusion(domain, description):
    payload = {"name": domain, "description": description}

    params = {"tsg_id": TSG_ID, "folder": "Shared"}

    response = requests.post(
        EXCLUSION_URL, headers=HEADERS, params=params, json=payload
    )


if __name__ == "__main__":
    create_token()
    with open(INPUT_FILE, "r") as f:
        data = yaml.safe_load(f)
    items = data.get("exclusions", [])
    for item in items:
        domain = item.get("domain")
        reason = item.get("reason", "Automation Added")
        if domain:
            print(f"Adding {domain}")
            update_decrpytion_exclusion(domain, reason)
