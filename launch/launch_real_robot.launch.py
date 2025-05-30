import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    # Includes the robot_state_publisher launch file, and forces sim time to be disabled
    package_name='donatello' 

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    # Joystick launch
    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch', 'joystick.launch.py'
                )])
    )

    # Twist Mux
    twist_mux_params = os.path.join(get_package_share_directory(package_name), 'config', 'twist_mux.yaml' )
    twist_mux = Node(
            package="twist_mux",
            executable="twist_mux",
            parameters=[twist_mux_params],
    )
    # RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(
            get_package_share_directory(package_name),
            'rviz',
            'donatello1.rviz' 
        )],
        output='screen'
    )

    # Lanza el nodo que publica en /odom a partir de /motor_feedback_vel
    real_odom_node = Node(
        package='donatello_py',
        executable='real_odometry_publisher',
        name='real_odometry_publisher',
        output='screen'
    )


    # Launch them all
    return LaunchDescription([
        rsp,
        joystick,
        twist_mux,
        real_odom_node,
        rviz_node
    ])