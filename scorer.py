# scorer.py
def rank_candidates(jd_data, candidates):
    for c in candidates:
        score = 0
        for skill in jd_data['must_have']:
            if skill.lower() in c['profile_url'].lower():
                score += 1
        c['score'] = score
    return sorted(candidates, key=lambda x: x['score'], reverse=True)
