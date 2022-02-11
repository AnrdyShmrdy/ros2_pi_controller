from setuptools import setup

package_name = 'ros2_pi_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andyp',
    maintainer_email='andy.ponce@outlook.com',
    description='ROS2 Package to control Raspberry Pi peripherals',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'minimal_publisher = ros2_pi_controller.minimal_publisher:main',
        	'minimal_subscriber = ros2_pi_controller.minimal_subscriber:main',
        	'gpio_publisher = ros2_pi_controller.gpio_publisher:main',
        	'gpio_subscriber = ros2_pi_controller.gpio_subscriber:main',
        ],
    },
)
