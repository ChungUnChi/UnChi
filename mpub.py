import rclpy
from rclpy.node import Node
from std_msgs.msg import String


import Nodeclass M_pub(Node)
        def __init__(self):
                super().__init__('mpub')




def main():
        rcply.init()
        node = M_pub()
        pub = node.create_publisher(String, 'messagepub', 10)
        msg = String()
        msg.data = 'hello, world'
        while True:
                pub.publish(msg)
        node.destroy_node()



def main():
        pass

if __name__ == '__main__':
    main()
 

