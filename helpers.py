def formatunit(value, unit):
    if unit == 'bps':
        return bit_to_humanreadable(value)
    elif unit == '%':
        return percent(value)

def percent(num):
    return str(round(num))+'%'

def bit_to_humanreadable(num):
    num /= 8  # I receive bit, and first I need to get rid of this, and transform in Byte
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.2f %s/s" % (num, x)
        num /= 1024.0

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