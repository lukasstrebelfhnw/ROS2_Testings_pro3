from setuptools import setup

package_name = 'ugv_safety'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/bringup_example.launch.py'] if os.path.exists('launch/bringup_example.launch.py') else []),
        ('share/' + package_name + '/config', ['config/params.yaml'] if os.path.exists('config/params.yaml') else []),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lukas',
    maintainer_email='lukas@example.com',
    description=package_name + ' nodes',
    license='MIT',
    entry_points={
        'console_scripts': [
            "emergency_brake_node = ugv_safety.emergency_brake_node:main",
            "collision_monitor_node = ugv_safety.collision_monitor_node:main"
        ],
    },
)
