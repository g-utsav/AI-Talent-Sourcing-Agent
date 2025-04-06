# ai_talent_sourcer_agent/agent.py
from dotenv import load_dotenv
load_dotenv()

import argparse
from jd_parser import parse_jd
from candidate_search import search_github_candidates
from scorer import rank_candidates
from outreach import generate_message
from sender import send_email
from db import store_jd, store_candidate


def run_agent(jd_file, location, min_exp):
    print("🔍 Reading JD...")
    with open(jd_file, 'r') as f:
        jd_text = f.read()

    jd_data = parse_jd(jd_text)
    jd_data['location'] = location
    jd_data['min_exp'] = min_exp
    jd_id = store_jd(jd_data)

    print("👥 Searching GitHub candidates...")
    raw_candidates = search_github_candidates(jd_data)
    #print(raw_candidates)

    print("🧠 Scoring candidates...")
    ranked = rank_candidates(jd_data, raw_candidates)

    for candidate in ranked[:10]:
        print(f"📨 Generating outreach for {candidate['username']}")
        message = generate_message(jd_data, candidate)
        candidate['outreach_message'] = message
        #send_email(candidate['email'], message)
        store_candidate(jd_id, candidate)

    print("✅ Done! Top 10 candidates contacted.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AI Talent Sourcer Agent')
    parser.add_argument('--jd', required=True, help='Path to job description text file')
    parser.add_argument('--location', required=True, help='Candidate location filter')
    parser.add_argument('--min_exp', type=int, required=True, help='Minimum years of experience')
    args = parser.parse_args()

    run_agent(args.jd, args.location, args.min_exp)
