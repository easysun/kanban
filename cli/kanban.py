import sys
import json

status = ['todo', 'wip', 'done']

if len(sys.argv) > 2:
    item = {}
    items = []
    with open('list.json', 'r') as input:
        items = json.load(input)
    if sys.argv[2] == 'new':
        item = {sys.argv[3]: "todo"}
        items.append(item)
        with open('list.json', 'w') as output:
            output.write(json.dumps(items))
    elif sys.argv[2] in status:
        show_list = []
        for item in items:
            for k, v in item.items():
                if v == sys.argv[2]:
                    show_list.append({k: v})
        print(show_list)
