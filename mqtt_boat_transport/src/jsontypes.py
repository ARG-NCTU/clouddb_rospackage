#!/usr/bin/env python3
#Created with python 2.7 compatibility

import json

class Type(object):
    def __init__(self):
        self.data = None

    def setData(self):
        pass

    @classmethod
    def fromString(cls, jsonstr):
        #todo
        #looking for a way to determine payloadtype from string
        #self.data = JSONDecode()
        pass

    def toString(self):
        return json.JSONEncoder().encode(self.data)
        
class VehStateType(Type):
    def __init__(self):
        super(VehStateType, self).__init__()

    def setData(self, timestamp, mid, vid, globalx, globaly, powerlevel, tempcpu, tempenv):
        # type: (str, int, int, float, float, int, float, float) -> None
        #todo: typechecking
        # tempenv = str(tempenv)
        self.data = {
            "timestamp": timestamp,
            "mid": mid,
            "vid": vid,
            "globalx": globalx,
            "globaly": globaly,
            "powerlevel": powerlevel,
            "tempcpu": tempcpu,
            "tempenv": tempenv
        }

class VehStateAnchor(Type):
    def __init__(self):
        super(VehStateAnchor, self).__init__()

    def setData(self, vsid, aid, commtypeid, mrange, rssi):
        # type: (int, int, int, float, float) -> None
        #todo: typechecking
        self.data = {
            "vsid": vsid,
            "aid": aid,
            "commtypeid": commtypeid,
            "range": mrange,
            "rssi": rssi
        }

class RVehStateEncounter(Type):
    def __init__(self):
        super(RVehStateEncounter, self).__init__()

    def setData(self, vsid, vsid2, commtypeid, mrange, rssi):
        # type: (int, int, int, float, float) -> None
        #todo: typechecking
        self.data = {
            "vsid": vsid,
            "vsid2": vsid2,
            "commtypeid": commtypeid,
            "range": mrange,
            "rssi": rssi
        }
