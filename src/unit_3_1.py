#! /usr/bin/env python

# Import Needed Packages
import rospy
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest


# Init ROS Node
rospy.init_node('service_execute_trajectory_client')

# Wait For Service And Connect To Client
rospy.wait_for_service('/execute_trajectory')
execute_trajectory_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj)

# Instantiate ExecTraj Object
execute_trajectory_request_object = ExecTrajRequest()

# Instantiate ROSPack Object, Define Trajectory Filepath
rospack = rospkg.RosPack()
trajectory_file_path = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

# Define Request File
execute_trajectory_request_object.file = trajectory_file_path
result = execute_trajectory_service_client(execute_trajectory_request_object)

print result