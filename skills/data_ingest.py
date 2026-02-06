"""
Skill: data_ingest
Description: Ingests mock data and returns structured JSON.
I/O:
    Input: None
    Output: dict with sample records
"""

def run():
    data = [
        {"id": 1, "content": "Sample text 1"},
        {"id": 2, "content": "Sample text 2"}
    ]
    return {"records": data}

if __name__ == "__main__":
    print(run())
