from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # Paths a los launch files
    sensors_launch = PathJoinSubstitution(
        [FindPackageShare('donatello'), 'launch', 'sensors.launch.py']
    )
    
    ekf_config = PathJoinSubstitution(
        [FindPackageShare('donatello'), 'config', 'ekf.yaml']
    )

    return LaunchDescription([
        # Lanzar los sensores (LiDAR + Realsense)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(sensors_launch),
        ),

        # Lanzar el EKF después de un  delay
        TimerAction(
            period=7.0,  # Esperar 7 segundos antes de lanzar el EKF
            actions=[
                Node(
                    package='robot_localization',
                    executable='ekf_node',
                    name='ekf_filter_node',
                    output='screen',
                    parameters=[ekf_config]
                )
            ]
        )
    ])
