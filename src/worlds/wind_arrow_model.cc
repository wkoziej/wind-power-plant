#include <boost/bind.hpp>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <stdio.h>

#include "ros/ros.h"
//#include <ros/callback_queue.h>
//#include <ros/subscribe_options.h>
#include <std_msgs/Float32.h>


namespace gazebo
{
  class ModelPush : public ModelPlugin
  {
    public: void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
      // Store the pointer to the model
      this->model = _parent;
      // Listen to the update event. This event is broadcast every
      // simulation iteration.
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          boost::bind(&ModelPush::OnUpdate, this, _1));

      // Initialize ros, if it has not already bee initialized.
      if (!ros::isInitialized())
	{
	  int argc = 0;
	  char **argv = NULL;
	  ros::init(argc, argv, "gazebo_client",
		    ros::init_options::NoSigintHandler);
	}

      ros::NodeHandle nh;
      this->windDirectionPublisher = nh.advertise<std_msgs::Float32>("/wind/direction", 5);
 
    }

    // Called by the world update start event
    public: void OnUpdate(const common::UpdateInfo & /*_info*/)
    {
      math::Pose pose =  this->model->GetRelativePose();

      double change = math::Rand::GetDblNormal();
      double dir = math::Rand::GetDblNormal(0, 0.6) > 0.5 ? -1 : 1;
      double scale = 0.005;
      math::Quaternion rot(0.0, 0.0, change * dir * scale);

      pose.Set (pose.pos, pose.rot * rot);
      this->model->SetRelativePose(pose);

      std_msgs::Float32 direction;
      direction.data = pose.rot.GetYaw();
      this->windDirectionPublisher.publish(direction);      
    }

    // Pointer to the model
    private: physics::ModelPtr model;

    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;

    ros::Publisher windDirectionPublisher;
  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(ModelPush)
}
