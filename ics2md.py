import icalendar

def YamlHead(data):
    pass

def write_md(data):
    pass
    filename = data['filename'] + ".md"
    with open(filename, 'w') as file:
        file.write(YamlHead(data['yamlhead']))


def load_ics(icsurl):
    pass