from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        Node(package='ugv_v2x', executable='leitsystem_interface_node', name='leitsystem_interface', parameters=[{'ttl_green': False, 'ttl_yellow': False}]),
        Node(package='ugv_v2x', executable='ampel_state_fuser_node', name='ampel_fuser'),
        Node(package='ugv_safety', executable='emergency_brake_node', name='emergency_brake'),
        Node(package='ugv_safety', executable='collision_monitor_node', name='collision_monitor', parameters=[{'min_distance': 0.6}]),
        Node(package='ugv_planning', executable='local_planner_node', name='local_planner'),
        Node(package='ugv_control', executable='speed_limiter_node', name='speed_limiter', parameters=[{'max_v_green': 1.5, 'max_v_yellow': 0.5}]),
        Node(package='ugv_control', executable='vehicle_interface_node', name='vehicle_interface'),
    ])
