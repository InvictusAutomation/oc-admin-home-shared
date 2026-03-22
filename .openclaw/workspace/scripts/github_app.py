#!/usr/bin/env python3
"""GitHub App Authentication"""
import jwt, time, base64, json, requests, sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

APP_ID = "3051540"
INSTALLATION_ID = "115228932"
PRIVATE_KEY_PATH = "/home/admin/.ssh/github-app.pem"
ORG = "InvictusAutomation"

def get_token():
    with open(PRIVATE_KEY_PATH, 'r') as f: private_key = f.read()
    now = int(time.time())
    def b64url(d): return base64.urlsafe_b64encode(d).rstrip(b'=').decode()
    header_enc = b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    payload_enc = b64url(json.dumps({"iss": int(APP_ID), "iat": now, "exp": now + 600}).encode())
    pk = serialization.load_pem_private_key(private_key.encode(), None, default_backend())
    sig = pk.sign(f"{header_enc}.{payload_enc}".encode(), padding.PKCS1v15(), hashes.SHA256())
    jwt_token = f"{header_enc}.{payload_enc}.{b64url(sig)}"
    resp = requests.post(f"https://api.github.com/app/installations/{INSTALLATION_ID}/access_tokens", headers={"Authorization": f"Bearer {jwt_token}", "Accept": "application/vnd.github+json"})
    return resp.json()["token"]

def create_repo(name, desc=""):
    resp = requests.post(f"https://api.github.com/orgs/{ORG}/repos", headers={"Authorization": f"token {get_token()}", "Accept": "application/vnd.github+json"}, json={"name": name, "description": desc, "private": True, "auto_init": True})
    print(f"Status: {resp.status_code}")
    print(resp.text)

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    if sys.argv[1] == "create": create_repo(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
