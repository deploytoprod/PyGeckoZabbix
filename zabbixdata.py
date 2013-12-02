'''
This class is responsible for going on Zabbix and get some data
'''

from pyzabbix import ZabbixAPI
from datetime import datetime
import time
import configs


class ZabbixData:
    def __init__(self):
        self.zapi = ZabbixAPI(configs.zabbixapiurl)
        self.zapi.login(configs.zabbixapilogin, configs.zabbixapipasswd)
        self.time_till = time.mktime(datetime.now().timetuple())
        self.time_from = self.time_till - 60 * 60 * 4  # 2 hours

    def gethistory(self, item):
        kind = item['kind']

        if kind == 'Line':
            id = item['zid']
            history = self.zapi.history.get(itemids=id,
                                            time_from=0,
                                            time_till=self.time_till,
                                            output='extend',
                                            sortfield='clock',
                                            sortorder='DESC',
                                            limit='25',
                                            )

            history = history[::-1]  # I'm reversing the list because in order to get the last measures I have to
                                     # query ordering by clock desc, so the list comes with the first value as the latest
                                     # to generate the line in correct order, I must reverse the values...

        if kind == 'Monitoring':
            history = {}
            httpcodezid = item['httpcodezid']
            httptimezid = item['httptimezid']
            httplasterrorzid = item['httplasterrorzid']

            httpcoderesponse = self.zapi.history.get(itemids=httpcodezid,
                                            time_from=0,
                                            time_till=self.time_till,
                                            output='extend',
                                            history=3,
                                            sortfield='clock',
                                            sortorder='DESC',
                                            limit='1',
                                            )
            history['httpcode'] = httpcoderesponse[0]['value']

            httptimeresponse = self.zapi.history.get(itemids=httptimezid,
                                            time_from=0,
                                            time_till=self.time_till,
                                            output='extend',
                                            history=0,
                                            sortfield='clock',
                                            sortorder='DESC',
                                            limit='1',
                                            )
            history['httptimeresponse'] = httptimeresponse[0]['value']

            httplasterrorresponse = self.zapi.history.get(itemids=httplasterrorzid,
                                            time_from=0,  # I want them all...
                                            time_till=self.time_till,
                                            output='extend',
                                            history=1,
                                            sortfield='clock',
                                            sortorder='DESC',
                                            limit='1',
                                            )
            history['httplasterrorresponse'] = httplasterrorresponse[0]['clock']

        #print history
        return history

    def getunacktriggers(self, item):
        triggers = self.zapi.trigger.get(only_true=1,
                                               skipDependent=1,
                                               monitored=1,
                                               active=1,
                                               output='extend',
                                               expandDescription=1,
                                               expandData='host',
                                               withLastEventUnacknowledged=1,
                                               sortfield='priority',
                                               sortorder='DESC'
                                               )
        #print triggers
        return triggers