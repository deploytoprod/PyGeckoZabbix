from zabbixdata import *
from geckoboard import *
import configs


gb = Geckoboard()

for piece in configs.pieces:
    kind = piece['kind']
    if kind == 'Line':
        history = ZabbixData().gethistory(piece)
        gb.line(history,piece)
        gb.push(piece)
    if kind == 'Monitoring':
        webmondata = ZabbixData().gethistory(piece)
        gb.monitoring(webmondata,piece)
        gb.push(piece)
    if kind == "Triggers":
        triggers = ZabbixData().getunacktriggers(piece)
        gb.triggerlist(triggers,piece)
        gb.push(piece)