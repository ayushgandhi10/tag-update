import json



##### update input file
file = open('tags.json', 'r')
data = json.load(file)
file.close()


if 'Alert' in data['complaint']:
    data['complaint'] = data['complaint'].replace('Alert', '').strip()
    for section in data['sections']:
        new_tags = []
        for tag in section['tags']:
            if tag['name'] == 'SECURITY' or tag['value'] == 'SECURITY' or tag['name'] == 'DECON' or tag['value'] == 'DECON':
                continue
            else:
                if data['complaint'] == 'Trauma':
                    if tag['name'] == 'PD Onboard' or tag['value'] == 'PD Onboard':
                        continue
                new_tags.append(tag)
        section['tags'] = new_tags
elif 'Distress' in data['complaint']:
    data['complaint'] = 'Respiratory Distress'
    for section in data['sections']:
        new_tags = []
        for tag in section['tags']:
            if tag['name'] == 'SECURITY' or tag['value'] == 'SECURITY' or tag['name'] == 'DECON' or tag['value'] == 'DECON' or  tag['name'] == 'RT Needed' or tag['value'] == 'RT Needed':
                continue
            else:
                new_tags.append(tag)
        section['tags'] = new_tags
    
if data['complaint'] == 'Stroke':
    for section in data['sections']:
        new_tags = []
        if section['name'] == 'Onset':
            for tag in section['tags']:
                tag['name'] = 'Onset ' + tag['name']
                new_tags.append(tag)
            section['tags'] = new_tags
                


##### update output file
file = open('output.json', 'w')
json.dump(data, file, indent=2)  # indent=4 for pretty printing
file.close()