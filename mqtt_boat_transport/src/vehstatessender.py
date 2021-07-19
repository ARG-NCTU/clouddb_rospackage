#!/usr/bin/env python3
import sys
import getpass
USER = getpass.getuser()
path = "/home/" + USER + "/duckiepond-nctu/catkin_ws/src/mqtt_bridge/src"
print(path)
sys.path.append(path)
from mqtt_publisher import MQTTpublisher
from jsontypes import *
from robotx_bionic_msgs.msg import Temperature
from std_msgs.msg import Int64, Float32
import time
import rospy

ros_topic_name = '/gps'

class VehStateSender(MQTTpublisher):
    def __init__(self):
        super(VehStateSender, self).__init__()
        d = rospy.Duration(float(rospy.get_param('~period', 3)))
        mqtt_ip = rospy.get_param('~mqtt_ip', '104.199.238.34')
        mqtt_port = int(rospy.get_param('~mqtt_port', 1883))
        self.mqtt_topic = rospy.get_param('~mqtt_topic', 'VehState')
        self.sub_temp = rospy.Subscriber("/temperature_node/temp", Temperature, self.cb_tempcpu) 
        self.sub_current = rospy.Subscriber("/current_8A_node_1/power", Int64, self.cb_current)     
        self.sub_tempenv = rospy.Subscriber("/environment_temperature", Float32, self.cb_tempenv)  
        self.tempcpu = float()
        self.current_time = None
        self.current = int()
        self.tempenv = float()

    def create_payload(self):
        data = VehStateType()
        now = time.localtime()
        self.current_time = time.strftime("%Y-%m-%dT%H:%M:%S", now)
        data.setData(timestamp=self.current_time, mid=2, vid=2,globalx=0.0,globaly=0.0,powerlevel=self.current,tempcpu=self.tempcpu,tempenv=self.tempenv)
        return data.toString()

    def cb_tempcpu(self, msg):
        self.tempcpu = msg.temperature_cpu
    
    def cb_current(self, msg):
        self.current = msg.data
    
    def cb_tempenv(self, msg):
        self.tempenv = msg.data



if __name__ == "__main__":
    veh_pub = VehStateSender()
    rospy.on_shutdown(veh_pub.on_shutdown)
    
    while not rospy.is_shutdown():
        veh_pub.loop()
