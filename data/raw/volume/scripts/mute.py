# Description: This script converts the text file to json file

import json
inp_file = 'data/raw/volume/mute.txt'
out_file_1 = 'data/volume-control/mute.json'

with open(inp_file, 'r') as f:
    lines = f.readlines()

data_1 = {}

for line in lines:
    if line:
        key = line.strip().replace('\n', '')
        value = {
            "intent": "volume.decrease",
            "entities": {
                "volume": "0"
            }
        }

        value = dict(value)
        data_1[key] = value


with open(out_file_1, 'w') as f:
    f.write(json.dumps(data_1, indent=4))
