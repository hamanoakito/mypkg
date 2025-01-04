import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    coordinate = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'calculate',
            )
    publish_check = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'check',
            output = 'screen'
            )
    return launch.LaunchDescription([coordinate, publish_check])