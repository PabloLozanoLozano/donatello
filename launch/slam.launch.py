import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'donatello'

    bringup_launch = PathJoinSubstitution(
        [get_package_share_directory(package_name), 'launch', 'start_ekf.launch.py']
    )

    real_robot_launch = PathJoinSubstitution(
        [get_package_share_directory(package_name), 'launch', 'launch_real_robot.launch.py']
    )

    slam_params = PathJoinSubstitution(
        [get_package_share_directory(package_name), 'config', 'slam_params.yaml']
    )

    return LaunchDescription([
        # Lanza todo el bringup (sensores + ekf)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(bringup_launch),
        ),

        # Lanza odometría + robot_state_publisher + rviz
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(real_robot_launch),
        ),

        # Lanza slam_toolbox
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox_node',
            output='screen',
            parameters=[slam_params]
        )
    ])
