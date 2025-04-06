# outreach.py
def generate_message(jd_data, candidate):
    return f"""
    Hi {candidate['username']},

    We came across your GitHub profile and were impressed by your work. We're currently hiring for a {jd_data['title']} role that matches your skills in {', '.join(jd_data['must_have'])}.

    If you're open to exploring new opportunities, we’d love to chat!

    Best,
    Talent Team
    """
