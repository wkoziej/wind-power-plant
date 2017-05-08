#!/usr/bin/env python

from wind_power_plant.srv import *
from gazebo_msgs.srv import * 
import rospy

def handle_turn_gondola(req):
    print "Turning [%s]" % (req.yawInRadians)
    service = '/gazebo/apply_joint_effort' 
    rospy.wait_for_service(service)
    try:
        start = rospy.Time(0)
        duration = rospy.Time(1)
        effort = req.yawInRadians;
        apply_joint_effort = rospy.ServiceProxy(service, ApplyJointEffort)
        resp = apply_joint_effort('gondola_hinge', effort, start, duration)
        print " Resp status %s and message %s " % (resp.success, resp.status_message)
        return TurnGondolaResponse()
    
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

    ##return TurnGondolaResponse()

def turn_gondola_server():
    rospy.init_node('turn_gondola_server')
    s = rospy.Service('/wind_power_plant/turn_gondola', TurnGondola, handle_turn_gondola)
    print "Ready to turn gondola"
    rospy.spin()

if __name__ == "__main__":
    turn_gondola_server()
