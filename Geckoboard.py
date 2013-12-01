'''
This class is responsible for pushing data to Geckoboard
'''

import json
import requests
from Helpers import *
import Configs

class Geckoboard:
    def __init__(self):
        self.widgetdata = {}
        self.widgetdata['api_key'] = Configs.geckoboardapikey
        self.headers = {'content-type': 'application/json'}

    def line(self, zhist, widgetdefinitions):
        mintrigger = widgetdefinitions['mintrigger']
        maxtrigger = widgetdefinitions['maxtrigger']
        colortrigger = widgetdefinitions['colortrigger']
        unit = widgetdefinitions['unit']

        points = []
        data = {}
        settings = {}
        settings['colour'] = '00ff00'  # Default color line

        for i in zhist:
            points.append(i['value'])
            #print("{0}: {1}".format(datetime.
            #                        fromtimestamp(int(point['clock'])).
            #                        strftime("%x %X"), point['value']))

        if (float(max(points)) > maxtrigger) or (float(min(points)) < mintrigger):
            settings['colour'] = colortrigger

        settings['axisy'] = [formatunit(float(min(points)),unit),
                             formatunit(float(max(points)),unit)]

        data['item'] = points
        data['settings'] = settings
        self.widgetdata['data'] = data
        #print self.widgetdata

    #def monitoring(self, item):
    #    url = item['uri']
    #    strexpected = item['strexpected']


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