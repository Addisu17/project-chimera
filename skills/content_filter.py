"""
Skill: content_filter
Description: Filters content based on simple rules.
I/O:
    Input: dict of records
    Output: dict with filtered records
"""

def run(data):
    filtered = [r for r in data.get("records", []) if "1" in r.get("content", "")]
    return {"filtered_records": filtered}

if __name__ == "__main__":
    sample_data = {"records":[{"content":"Sample text 1"},{"content":"Sample text 2"}]}
    print(run(sample_data))
