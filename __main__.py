from zabbixdata import *
from geckoboard import *
from otherdata import *
import configs, pieces
from time import sleep

while True:
    try:
        gb = Geckoboard()
        for piece in pieces.pieces:
            kind = piece['kind']
            if kind == 'Item':
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
            if kind == "Other":
                now = OtherData().now()
                gb.text(now)
                gb.push(piece)
    except Exception, e:
        print str(e)
    finally:
        sleep(configs.runinterval)
