from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # TF LiDAR 1
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['-0.24', '0', '0.0', '0', '0', '0', 'base_link', 'laser1'],
        ),

        # # TF LiDAR 2
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=['0.2', '0.18', '0.0', '0', '0', '0', 'base_link', 'laser2'],
        # ),

        # LIDAR 1
        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node_1',
            namespace='lidar1',
            parameters=[{
                'channel_type': 'serial',
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 460800,
                'frame_id': 'laser1',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Standard',
            }],
            output='screen',
        ),

        # # LIDAR 2
        # Node(
        #     package='sllidar_ros2',
        #     executable='sllidar_node',
        #     name='sllidar_node_2',
        #     namespace='lidar2',
        #     parameters=[{
        #         'channel_type': 'serial',
        #         'serial_port': '/dev/ttyUSB1',
        #         'serial_baudrate': 460800,
        #         'frame_id': 'laser2',
        #         'inverted': False,
        #         'angle_compensate': True,
        #         'scan_mode': 'Standard',
        #     }],
        #     output='screen',
        # )
    ])
