'''
This class is responsible for pushing data to Geckoboard
'''

import json
import requests
from helpers import *
import configs

class Geckoboard:
    def __init__(self):
        self.widgetdata = {}
        self.widgetdata['api_key'] = configs.geckoboardapikey
        self.headers = {'content-type': 'application/json'}

    def line(self, zhist, widgetdefinitions):
        mintrigger = widgetdefinitions['mintrigger']
        maxtrigger = widgetdefinitions['maxtrigger']
        colortrigger = widgetdefinitions['colortrigger']
        unit = widgetdefinitions['unit']

        points = []
        data = {}
        settings = {}
        settings['colour'] = '78ab49'  # Default color line: light green

        for i in zhist:
            points.append(i['value'])
            #print("{0}: {1}".format(datetime.
            #                        fromtimestamp(int(point['clock'])).
            #                        strftime("%x %X"), point['value']))

        print widgetdefinitions['name']
        print (min(points))
        print (max(points))
        if unit == 'bps':
            points = map(int,points)
        if unit == '%':
            points = map(float,points)
        print points

        try:
            widgetdefinitions['percenttrigger']
        except KeyError:
            if (max(points) > maxtrigger) or (min(points) < mintrigger) or (min(points) == max(points)):
                settings['colour'] = colortrigger
        else:
            if unit != '%':
                percentdiff  = 100.0 - (float((min(points))/float(max(points))) * 100)

            else:
                percentdiff = max(points) - min(points)

            if float(widgetdefinitions['percenttrigger'] <= percentdiff) or (float(min(points)) == float(max(points))):
                settings['colour'] = colortrigger

            print percentdiff
            print colortrigger

        settings['axisy'] = [formatunit(float(min(points)),unit),
                             formatunit(float(max(points)),unit)]

        data['item'] = points
        data['settings'] = settings
        self.widgetdata['data'] = data
        print self.widgetdata

    def monitoring(self, zhist, widgetdefinitions):
        data = {}
        httpcode = zhist['httpcode']
        httptimeresponsems = sec_to_ms(float(zhist['httptimeresponse']))
        httplasterrorresponse = calculate_age(zhist['httplasterrorresponse'])

        try:
            widgetdefinitions['httpexpectedcode']
        except KeyError:
            if int(httpcode) == 200:
                data['status'] = 'Up'
            else:
                data['status'] = 'Down'
        else:
            if int(httpcode) == widgetdefinitions['httpexpectedcode']:
                data['status'] = 'Up'
            else:
                data['status'] = 'Down'

        data['downTime'] = str(httplasterrorresponse)
        data['responseTime'] = str(httptimeresponsems)

        self.widgetdata['data'] = data
        #print self.widgetdata


    def triggerlist(self, ztriggers, widgetdefinitions):
        data = []
        if len(ztriggers):
            for trigger in ztriggers:
                title = {}
                label = {}
                listitem = {}

                title['text'] = trigger['host'] + ' - ' + trigger['description']
                title['highlight'] = 'True'

                severity = priority_to_humanreadable(trigger['priority'])
                label['name'] = severity['txt']
                label['color'] = severity['color']
                description = "Age: " + str(calculate_age(trigger['lastchange']))

                #print title
                #print label
                #print description

                listitem['label'] = label
                listitem['title'] = title
                listitem['description'] = description

                data.append(listitem)
        else:
            title = {}
            data = []
            listitem = {}

            title['text'] = 'Good job, infra! Nothing is triggered on Zabbix :-)'
            title['highlight'] = 'True'
            listitem['title'] = title

            data.append(listitem)

        self.widgetdata['data'] = data
        #print self.widgetdata

    def push(self, widgetdefinitions):
        wk = widgetdefinitions['widget_key']
        response = requests.post('https://push.geckoboard.com/v1/send/' + wk,
                                 data=json.dumps(self.widgetdata),
                                 headers=self.headers)
        print response.text