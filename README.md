# UnChi
Geronimo
Cowabungga


  - - -

## 2023_02_13
  * first
    * turtlebot3
    * Enviroment VMware 17 Ubuntu 20.04
  * second
    * ROS2 DDS explain
  * third
```
    touch settings.json
    sudo apt install terminator
    ros2/
    source~/.bashrc
    cd robot_ws
    ls
    mkdirsrc
    cb
    colcunbuild
    github https://github.com/ChungUnChi/UnChi.git
    git config --global user.email "jhg78985200@gmail.com"
    git config --global user.name "ChungUnChi"
    cw
```


## 2023_02_14
  * first 
      * my package 
          * make node, and exceute
      * mpub

```

        import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class M_pub(Node):
  def __init__(self):
    super().__init__('mpub')
    self.pub = self.create_publisher(String, 'message', 10)
    self.create_timer(1, self.pubmessage)
    self.count = 0

  def pubmessage(self):
    msg = String()
    msg.data = f'hello, world : {self.count}'
    self.pub.publish(msg)
    self.get_logger().info(f'Seding message: [{msg.data}]')
    self.count += 1

def main():
  rclpy.init()
  node = M_pub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

      * msub

```

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class M_sub(Node):
  def __init__(self):
    super().__init__('msub')
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_subscription(String, 'message', self.messagesub, self.qos)

  def messagesub(self, msg):
    self.get_logger().info(f'Incoming messae : [{msg.data}]')

def main():
  rclpy.init()
  node = M_sub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()


```


      * mtpub

```

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Mt_pub(Node):
  def __init__(self):
    super().__init__('mpub')
    self.pub = self.create_publisher(String, 'message', 10)
    self.tpub = self.create_publisher(String, 'time', 10)
    self.create_timer(1, self.pubmessage)
    self.create_timer(0.1, self.pubtime)
    self.count = 0
    self.time = 0

  def pubmessage(self):
    msg = String()
    msg.data = f'hello, world : {self.count}'
    self.pub.publish(msg)
    self.get_logger().info(f'Seding message: [{msg.data}]')
    self.count += 1

  def pubtime(self):
    tmsg = String()
    tmsg.data = f'publish time : {self.time}'
    self.tpub.publish(tmsg)
    self.time += 0.1

def main():
  rclpy.init()
  node = Mt_pub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

```


      * tsub

```

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class T_sub(Node):
  def __init__(self):
    super().__init__('tsub')
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_subscription(String, 'time', self.messagesub, self.qos)

  def messagesub(self, msg):
    self.get_logger().info(f'Incoming time : [{msg.data}]')

def main():
  rclpy.init()
  node = T_sub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()


```


      * move_turtle


```

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class M_turtle(Node):
  def __init__(self):
    super().__init__('move_turtle')
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', self.qos)
    self.create_timer(0.1, self.pubmessage)
    self.vel = 0.0

  def pubmessage(self):
    msg = Twist()
    msg.linear.x = self.vel
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 2.5
    self.pub.publish(msg)
    self.get_logger().info(f'Seding message: [{msg}]')
    self.vel += 0.04
    if self.vel > 3.0:
      self.vel = 0.0

def main():
  rclpy.init()
  node = M_turtle()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

```

