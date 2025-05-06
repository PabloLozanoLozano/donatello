from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'slam_params_file',
            default_value='./src/donatello/config/mapper_params_online_async.yaml',
            description='Archivo de parámetros para SLAM Toolbox'
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Usar tiempo simulado'
        ),
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[LaunchConfiguration('slam_params_file'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
        )
    ])
