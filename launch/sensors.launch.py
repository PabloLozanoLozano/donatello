# from launch import LaunchDescription
# from launch_ros.actions import Node
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import ThisLaunchFileDir
# import os

# from ament_index_python.packages import get_package_share_directory

# def generate_launch_description():
#     # Path al launch del LiDAR
#     rplidar_launch = os.path.join(
#         get_package_share_directory('donatello'),
#         'launch',
#         'rplidar.launch.py'
#     )

#     # Path al launch de la Realsense
#     realsense_launch = os.path.join(
#         get_package_share_directory('realsense2_camera'),
#         'launch',
#         'rs_launch.py'
#     )

#     return LaunchDescription([
#         # Incluir el launch del LiDAR
#         IncludeLaunchDescription(
#             PythonLaunchDescriptionSource(rplidar_launch),
#         ),
        
#         # Incluir el launch de la cámara Realsense con los argumentos que quieres
#         IncludeLaunchDescription(
#             PythonLaunchDescriptionSource(realsense_launch),
#             launch_arguments={
#                 'depth_module.depth_profile': '1280x720x30',
#                 'pointcloud.enable': 'true',
#                 'enable_imu': 'true',
#                 'unite_imu_method': 'linear_interpolation'
#             }.items()
#         ),
#     ])


from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path al launch del LiDAR
    rplidar_launch = os.path.join(
        get_package_share_directory('donatello'),
        'launch',
        'rplidar.launch.py'
    )

    # Path al launch de la Realsense
    realsense_launch = os.path.join(
        get_package_share_directory('realsense2_camera'),
        'launch',
        'rs_launch.py'
    )

    return LaunchDescription([
        # Incluir el launch del LiDAR
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(rplidar_launch),
        ),
        
        # Incluir el launch de la cámara Realsense
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(realsense_launch),
            launch_arguments={
                'depth_module.depth_profile': '1280x720x30',
                'pointcloud.enable': 'true',
                'enable_imu': 'true',
                'unite_imu_method': 'linear_interpolation'
            }.items()
        ),

        # Static transform entre base_link y laser_frame
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='laser_static_tf_pub',
            arguments=['0.2', '0', '0.175', '0', '0', '0', 'base_link', 'laser_frame'],
        ),

        # Static transform entre base_link y camera_link_optical
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='camera_static_tf_pub',
            arguments=['0.405', '0', '0.08', '-1.5708', '0', '-1.5708', 'base_link', 'camera_link_optical'],
        ),

    ])
