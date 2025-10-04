import os, json
from datetime import datetime
PATH = os.path.expanduser('~/.tiny_ai_app_history.json')

def add_entry(kind, prompt, response):
    try:
        data = load_all()
    except:
        data = []
    data.append({
        'time': datetime.utcnow().isoformat(),
        'kind': kind,
        'prompt': prompt,
        'response': response
    })
    with open(PATH, 'w') as f:
        json.dump(data, f, indent=2)

def load_all():
    if not os.path.exists(PATH):
        return []
    with open(PATH,'r') as f:
        return json.load(f)
