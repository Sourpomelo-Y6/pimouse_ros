#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

class BuzzerTest(unittest.TestCase):
	def test_node_exist(self):
		nodes = rosnode.get_node_names()
		self.assertIn('/buzzer', nodes, "node does not exist")

	def test_put_value(self):
		pub = rospy.Publisher('/buzzer', UInt16)
		for i in range(10):
			pub.publish(1234)
			time.sleep(0.1)
		
		with open("/dev/rtbuzzer0","r") as f:
			data = f.readline()
			self.assertEqual(data,"1234/n","value does not writen to rtbuzzer0")

def write_freq(hz=0):
        bfile = "/dev/rtbuzzer0"
        try:
                with open(bfile,"w") as f:
                        f.write(str(hz) + "\n")
        except IOError:
                rospy.logerr("can't write to " + bfile)

def recv_buzzer(data):
        write_freq(data.data)

if __name__ == '__main__':
        rospy.init_node('buzzer')
        rospy.Subscriber("buzzer", UInt16, recv_buzzer)
        rospy.spin()

