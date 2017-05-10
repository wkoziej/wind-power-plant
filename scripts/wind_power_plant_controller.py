#!/usr/bin/env python
import rospy

from wind_power_plant.srv import *
from std_msgs.msg import Float32
import numpy as np
from math import radians
from math import degrees

ERROR_LEVEL = 0.001


def directions_equals(dir1, dir2, error_level):
    return abs(dir1 - dir2) <= error_level

def wind_direction_changed(wind_direction_data):
    print " Wind direction    %s " % wind_direction_data.data
    gondola_direction_service_name = '/wind_power_plant/gondola_direction'
    turn_gondola_service_name = '/wind_power_plant/turn_gondola'   
    rospy.wait_for_service(gondola_direction_service_name)
    try:
        gondola_direction_srv = rospy.ServiceProxy(gondola_direction_service_name, GondolaDirection)
        gondola_direction = (gondola_direction_srv()).yawInRadians
        wind_direction = wind_direction_data.data


        if not directions_equals (gondola_direction, wind_direction, ERROR_LEVEL):

            wind_deg = ( degrees(wind_direction) + 360) %  360;
            gondola_deg = (degrees(gondola_direction) + 360) % 360;
            gondola_oposite_deg = (degrees(gondola_direction) + 180) % 360;
            
            turn_str = "right"
            change_dir_sign = -1

            if (wind_deg - gondola_oposite_deg + 360) % 360 < 180:
                turn_str = "left"
                change_dir_sign = 1

            rospy.wait_for_service(turn_gondola_service_name)
            # This take a while
            turn_gondola_srv = rospy.ServiceProxy(turn_gondola_service_name, TurnGondola)
            print " Gondola\t RAD %s,\t DEG = %s " % (gondola_direction, gondola_deg)
            print " Wind\t\t RAD %s,\t DEG = %s " % (wind_direction, wind_deg)
#            print " %s - L (GOP %s) - R %s " % (gondola_oposite_deg - wind_deg, gondola_oposite_deg, wind_deg - gondola_oposite_deg)
            print " Turn gondola %s" % (turn_str)
            
            turn_gondola_srv(change_dir_sign * 1.1)
            
    except:
        print "Service call failed %s" % (sys.exc_info()[0])
        raise

        
def wind_power_plant_controller():
    rospy.init_node('wind_power_plant_controller', anonymous=True)
    rospy.Subscriber("/wind/direction", Float32, wind_direction_changed, queue_size=1)
    rospy.spin()


if __name__ == '__main__':
    wind_power_plant_controller()
