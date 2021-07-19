#!/usr/bin/env python3
import sys
import getpass
USER = getpass.getuser()
path = "/home/" + USER + "/duckiepond-nctu/catkin_ws/src/mqtt_bridge/src"
print(path)
sys.path.append(path)
from mqtt_publisher import MQTTpublisher
from jsontypes import *
from std_msgs.msg import Int64, Float32
import time
import rospy


class VehStatsAnchorSender(MQTTpublisher):
    def __init__(self):
        super(VehStatsAnchorSender, self).__init__()
        d = rospy.Duration(float(rospy.get_param('~period', 3)))
        mqtt_ip = rospy.get_param('~mqtt_ip', '104.199.238.34')
        mqtt_port = int(rospy.get_param('~mqtt_port', 1883))
        self.mqtt_topic = rospy.get_param('~mqtt_topic', 'VehStatsAnchor')
        self.sub_range = rospy.Subscriber("/range", Float32, self.cb_range)
        self.sub_rssi = rospy.Subscriber("/rssi", Float32, self.cb_rssi)
        self.range = float()  
        self.rssi = float()
        

    def create_payload(self):
        data = VehStateAnchor()
        data.setData(vsid=2, aid=8, commtypeid=1, mrange=self.range, rssi=self.rssi)
        return data.toString()

    def cb_range(self, msg):
        self.range = msg.data
    
    def cb_rssi(self, msg):
        self.rssi = msg.data

if __name__ == "__main__":
    veh_anc_pub = VehStatsAnchorSender()
    rospy.on_shutdown(veh_anc_pub.on_shutdown)
    
    while not rospy.is_shutdown():
        veh_anc_pub.loop()
