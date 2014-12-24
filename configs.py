geckoboardapikey = 'put your geckoboard api key here'
zabbixapiurl = 'your zabbix url'
zabbixapilogin = 'your zabbix login'
zabbixapipasswd = 'your zabbix passwd'

notriggersmessage = 'Good job, infra! Nothing is triggered on Zabbix :-)'

runinterval = 600

####################
#
#  Sample config
#
pieces = [
#           { 'type': 'Zabbix Item',
#             'kind': 'Item',
#             'name': 'Sample Name',
#             'zid': 12345,
#             'widgit_key': '123456-12345678-1234-1234-1234-123456789012',
#             'mintrigger': 1,
#             'maxtrigger': 50,
#             'percenttrigger': 40,
#             'colortrigger': '012345',
#             'unit': '%',
#           },

#           {
#             'type': 'Zabbix Item',
#             'kind': 'Monitoring',
#             'httpcodezid': 28985,
#             'httpexpectedcode': 200,
#             'httptimezid': 28984,
#             'httplasterrorzid': 28982,
#             'name': 'psafe.com',
#             'widgit_key': [ '123456-12345678-1234-1234-1234-123456789012',
#                             '123456-12345678-1234-1234-1234-123456789012' ],
#           },

#           {
#             'type': 'Zabbix Item',
#             'kind': 'Triggers',
#             'name': 'Unack issues',
#             'widget_key': '109909-6601885f-f14d-4a93-a3d0-3a2aab269348',
#             'filter': { 'priority': 1 },
#           },
         ]
