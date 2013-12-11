import datetime

class OtherData:
    def now(self):
        values = {}
        values['type'] = 2  # Informative banner
        now = datetime.datetime.now()
        retval = datetime.time(now.hour, now.minute, now.second)
        values['text'] = '<h1><strong>'+str(retval)+'</strong></h1>'
        #print values
        return values