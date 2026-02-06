"""
Skill: analytics
Description: Processes JSON data and returns summary statistics.
I/O:
    Input: dict of records
    Output: dict with summary
"""

def run(data):
    count = len(data.get("records", []))
    return {"total_records": count}

if __name__ == "__main__":
    sample_data = {"records": [{"id":1}, {"id":2}]}
    print(run(sample_data))
