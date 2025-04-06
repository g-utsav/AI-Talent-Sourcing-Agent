# db.py
import json
import os
from datetime import datetime

if not os.path.exists("data"):
    os.mkdir("data")

def store_jd(jd_data):
    # Sanitize filename: replace ':' and '.' with valid characters
    timestamp = datetime.utcnow().isoformat().replace(":", "-").replace(".", "_")
    jd_id = f"jd_{timestamp}"
    with open(f"data/{jd_id}.json", "w") as f:
        json.dump(jd_data, f, indent=2)
    return jd_id

def store_candidate(jd_id, candidate):
    path = f"data/{jd_id}_candidates.json"
    candidates = []
    if os.path.exists(path):
        with open(path, 'r') as f:
            candidates = json.load(f)
    candidates.append(candidate)
    with open(path, 'w') as f:
        json.dump(candidates, f, indent=2)
