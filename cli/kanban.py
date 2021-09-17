import json
import sys
import uuid

from datetime import datetime

status = ['todo', 'wip', 'done']
commands = status + ['new', 'move']

if len(sys.argv) > 2:
    item = {}
    items = []
    with open('list.json', 'r') as input:
        items = json.load(input)

    if sys.argv[2] == 'new':
        item = {"id": uuid.uuid4().hex, "title": sys.argv[3], "status": "todo",
            "created_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        items.append(item)
        with open('list.json', 'w') as output:
            output.write(json.dumps(items))

    elif sys.argv[2] in status:
        show_list = []
        stack = []
        for item in items:
            if item['status'] == sys.argv[2]:
                show_list.append(item)
        show_list = sorted(show_list, key = lambda x: x['updated_time'])
        print(show_list)

    elif sys.argv[2] == 'move':
        for idx, item in enumerate(items):
            if idx == int(sys.argv[3]) - 1:
                item['status'] = sys.argv[5]
                item['updated_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('list.json', 'w') as output:
            output.write(json.dumps(items))

    elif sys.argv[2] not in commands:
        raise ValueError(f"\'{sys.argv[2]}\' is not supported, it supposed to be {commands}")
