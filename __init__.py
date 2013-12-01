from ZabbixData import *
from Geckoboard import *
import Configs


gb = Geckoboard()

for piece in Configs.pieces:
    kind = piece['kind']
    if kind == 'Line':
        history = ZabbixData().gethistory(piece)
        gb.line(history,piece)
        gb.push(piece)
    #    continue
    #if kind == 'Monitoring':
    #    history = ZabbixData().gethistory(piece)
    #    gb.monitoring(history,piece)
    #    gb.push(piece)
    if kind == "Triggers":
        triggers = ZabbixData().getunacktriggers(piece)
        gb.triggerlist(triggers,piece)
        gb.push(piece)