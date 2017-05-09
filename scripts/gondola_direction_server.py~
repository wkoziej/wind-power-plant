#!/usr/bin/env python

from wind_power_plant.srv import *
from gazebo_msgs.srv import * 

import rospy

def handle_gondola_direction(req):
    print "Getting direction [%s]" % (req)
    service = '/gazebo/get_link_state' 
    rospy.wait_for_service(service)
    try:
        get_link_state = rospy.ServiceProxy(service, GetLinkState)
        resp = get_link_state('gondola', '')
        print " Resp status %s and message %s " % (resp.success, resp.status_message)
        r = GondolaDirectionResponse()
        r.yawInRadians = resp.link_state.pose.orientation.z 
        return r
    
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        
    return GondolaDirectionResponse()

def gondola_direction_server():
    rospy.init_node('gondola_direction_server')
    s = rospy.Service('/wind_power_plant/gondola_direction', GondolaDirection, handle_gondola_direction)
    print "Ready for geting gondola direction"
    rospy.spin()

if __name__ == "__main__":
    gondola_direction_server()
