def formatunit(value, unit):
    if unit == 'bps':
        return bit_to_humanreadable(value, unit)
    elif unit == 'int':
        return int_to_smallformat(value, unit)
    elif unit == '%':
        return percent(value)

def percent(num):
    return str(round(num))+'%'

def bit_to_humanreadable(num, type):
    for x in ['bits', 'Kb', 'Mb', 'Gb', 'Tb']:
        if num < 1024.0:
            return "%3.2f %sps" % (num, x)
        num /= 1024.0


def int_to_smallformat(num, type):
    for x in ['', 'K', 'M', 'G', 'T']:
        if num < 1000.0:
            return "%3.1f %s" % (num, x)
        num /= 1000.0

def priority_to_humanreadable(priority):
    notclassified='#ffffff'
    information='#63CF5F'
    warning='#C0D100'
    average='#FF9900'
    high='#D17C28'
    disaster='#FF0000'
    label = {}

    priority = int(priority)

    if priority == 0:
        label['txt'] = 'Not Classified'
        label['color'] = notclassified
    if priority == 1:
        label['txt'] = 'Information'
        label['color'] = information
    if priority == 2:
        label['txt'] = 'Warning'
        label['color'] = warning
    if priority == 3:
        label['txt'] = 'Average'
        label['color'] = average
    if priority == 4:
        label['txt'] = 'High'
        label['color'] = high
    if priority == 5:
        label['txt'] = 'Disaster'
        label['color'] = disaster

    return label

def calculate_age(unixtimestamp):
    import datetime
    import time

    now = time.mktime(datetime.datetime.now().timetuple())
    seconds = int(now) - int(unixtimestamp)

    agesec = datetime.timedelta(seconds=seconds)
    return agesec

def sec_to_ms(sec):
    return sec*1000
