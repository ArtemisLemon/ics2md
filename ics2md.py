import icalendar

def YamlHead(title):
    out = "---\nlayout : post\n title : {}\n---".format(title)

def write_md(data):
    pass
    filename = data['filename'] + ".md"
    with open(filename, 'w') as file:
        file.write(YamlHead(data['yamlhead']))


def load_ics():
    file = open("NaomodWeeklySeminars", 'rb')
    ical = icalendar.Calendar.from_ical(file.read())
    out = []
    for component in ical.walk():
        if component.name == "VEVENT":
            out.append(component)
            print(component.get("name"))
            print(component.get("description"))
            print(component.get("organizer"))
            print(component.get("location"))
            print(component.decoded("dtstart"))
            print(component.decoded("dtend"))
            print("-----------------")
    file.close()

load_ics()