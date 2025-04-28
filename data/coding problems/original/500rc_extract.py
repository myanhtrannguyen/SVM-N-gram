import json

original = 'data\original\code_problems.jsonl'

with open(original, 'r', encoding='utf_8') as f:
    rc = [json.loads(line) for line in f.readlines()]

last_500_rc = rc[-500:]

with open('data\original\code_problems_500rc.jsonl', 'w', encoding='utf_8') as f:
    for line in last_500_rc:
        f.write(json.dumps(line) + '\n')
