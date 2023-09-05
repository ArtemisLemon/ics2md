import icalendar

def YamlHead(data):
    out = "---\nlayout : post\n"
    for key,value in data.items():
        out +=  "{} : {}\n".format(key,value)
    out+="---\n"
    return out

def write_md(data):
    pass #not ready
    filename = data['filename'] + ".md"
    with open(filename, 'w') as file:
        file.write(YamlHead(data['yamlhead']))
        if data["body"]:
            file.write(data["body"])


def load_ics(path):
    out = []
    file = open(path, 'rb')
    ical = icalendar.Calendar.from_ical(file.read())
    for component in ical.walk():
        if component.name == "VEVENT":
            out.append(component)
            print(component.get("summary"))
            print(component.get("description"))
            # print(component.get("organizer"))
            print(component.get("location"))
            print(component.decoded("dtstart"))
            print(component.decoded("dtend"))
            print("-----------------")
    file.close()
    return out

def extractfilename(decoded_datetime,title):
    out = ""
    year = decoded_datetime.year
    month = "{:02d}".format(decoded_datetime.month)
    day = "{:02d}".format(decoded_datetime.day)
    out += "{}-{}-{}".format(year,month,day)
    for word in title.split():
        out += "-{}".format(word)
    
    print(out)
    return out
    


def extractdata(event):
    out = {}
    out["filename"] = extractfilename(event.decoded("dtstart"), event.get("summary"))
    out["yamlhead"] = {"title":event.get("summary")}
    out["body"] = event.get("description")
    return out


events = load_ics("NaomodWeeklySeminars")
for event in events:
    write_md(extractdata(event))