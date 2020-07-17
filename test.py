from parts import joint
import time


joint1 = joint(18, [1200, 1800])
joint1.goMax()
time.sleep()
joint1.goMin()
