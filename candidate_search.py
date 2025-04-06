# candidate_search.py
import requests

def search_github_candidates(jd_data):
    query = f"location:{jd_data['location']} " + " ".join(jd_data['must_have'])
    url = f"https://api.github.com/search/users?q={query}&per_page=10"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    users = response.json().get("items", [])

    candidates = []
    for user in users:
        print(user)
        candidates.append({
            "username": user["login"],
            "profile_url": user["html_url"],
            "email": f"{user['login']}@users.noreply.github.com"  # Placeholder
        })
    return candidates
