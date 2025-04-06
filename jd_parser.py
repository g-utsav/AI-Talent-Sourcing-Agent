import requests

def call_local_model(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "gemma:2b",  # Or use "llama3" if you've downloaded that
        "prompt": prompt,
        "stream": False
    })
    data = response.json()
   # print("📨 Response:", data)  # ✅ just print the dictionary, no + operator
    return data["response"]

def parse_jd(jd_text):
    prompt = f"""
    Extract the following from this Job Description (JD) in JSON format:
    {{
      "title": "...",
      "must_have": ["..."],
      "nice_to_have": ["..."],
      "min_exp": ...
    }}

    JD:
    {jd_text}
    """

    response_text = call_local_model(prompt)

    # ✅ Try to parse model output as JSON
    try:
        import json
        parsed = json.loads(response_text)
        return parsed
    except json.JSONDecodeError:
        # Fall back in case of weird formatting (MVP-style fallback)
        return {
            "title": "Backend Engineer",
            "must_have": ["Java", "Spring Boot"],
            "nice_to_have": ["Docker", "AWS"],
            "min_exp": 4
        }
