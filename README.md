# ROS_RIA_002_ServiceRequests

Brief Notes Taken Over Proceeding Sections:

```
ROS Services vs ROS Topics vs ROS Actions:

Imagine having a BB-8 with a laser sensor, facial recognition, and
navigation. The laser will use a **topic** to publish all of the laser 
readings at 20Hz. We use a topic because we need to have that information 
available all the time, for other ROS systems.

The facial recognition system will provide a **service**. Our ROS program 
will call that service and wait until it provides the person's name.

The navigation system will provide an **action**. Your program will call 
the action to move the robot, and /while/ it is performing that task, your 
program will perform other tasks. (That action will, also, give Feedback 
-- such as distance left to desired coordinates, along the process.

Services are Synchronous. When you call a service, your program cannot 
continue until it receives a result from the service. Actions are 
Asynchronous (like launching a new thread). When you call an action, your 
program can perform other tasks while the action is being performed.

** Note: Use services when your program cannot continue until it receives 
   the result from the service.

   Service message files have extension '.srv'; wherein topic messages
   files have extension '.msg'.

   Service msg files are defined inside a srv directory; wherein topic
   msg files are defined inside a msg directory.

   Service messages have two parts: 

   Request
   ---
   Response

   Request: How you call service -- variables passed to service server
   Response: How service will respond 



Whenever a service message is compiles, three message objects are
created. The service message itself, the request, and the response.

Ex:
Let's say we have a service message named MyServiceMessage. It compiles 
the following:

  MyServiceMessage: The message itself, used for creating a connection 
      to the service server.

  MyServiceMessageRequest: Object used for creating a request to send to 
      the server.

  MyServiceMessageResponce: Object used for sending response from the   
      server back to the client whenever service ends.



List Running ROS Services
-------------------------
* rosservice list



Get More Info On Specific Service
rosservice info /name_of_service
---------------------------------
* rosservice info /trajectory_by_name

Node: Node that provides (has created) service

Type: Type of message used by service --with same structure as topics;
package_where_service_msg_defined or name_of_file_where_msg_defined.

Args: Arguments service takes when called.



Explore Structure Of Service Message
rossrv show name_of_package/name_of_service_msg
-----------------------------------------------
* rossrv show trajectory_by_name_srv/TrajByName



Call Service (Manually) From Console
rosservice call /service_name TAB-TAB
------------------------------------
* rosservice call /trajectory_by_name TAB-TAB
Gives: rosservice call /trajectory_by_name "traj_name: '' "
* rosservice call /trajectory_by_name "traj_name: 'get_food'"
(Available trajectories: init_pos, get_food, release_food)

Note: TAB-TAB means that you have to quickly press the TAB key twice. 
This will autocomplete the structure of the Service message to be sent 
for you. Then, you only have to fill in the values.



List '.srv' Files Associated With Server
roscd server_name; ls srv
----------------------------------------
roscd trajectory_by_name_srv; ls srv
```
