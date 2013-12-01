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
        self.time_from = self.time_till - 60 * 60 * 2  # 2 hours

    def gethistory(self, item):
        kind =  item['kind']

        if kind == 'Line':
            id = item['zid']
            history = self.zapi.history.get(itemids=id,
                                            time_from=self.time_from,
                                            time_till=self.time_till,
                                            output='extend',
                                            limit='120',)
            if not len(history):
                history = self.zapi.history.get(itemids=id,
                                                time_from=self.time_from,
                                                time_till=self.time_till,
                                                output='extend',
                                                limit='120',
                                                history=0,)

        if kind == 'Monitoring':
            httptestid = item['httptestid']
            history = self.zapi.webcheck.get(httptestids=httptestid,
                                             output='extend',
                                             limit='6',
                                             selectSteps='extend',
                                             webstepid=0,)

        return history

    def getunacktriggers(self, item):
        unack_triggers = self.zapi.trigger.get(only_true=1,
                                               skipDependent=1,
                                               monitored=1,
                                               active=1,
                                               output='extend',
                                               expandDescription=1,
                                               expandData='host',
                                               withLastEventUnacknowledged=1,
                                               sortfield='priority',sortorder='DESC'
                                               )
        print unack_triggers
        return unack_triggers