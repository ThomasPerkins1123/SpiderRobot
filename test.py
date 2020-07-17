from parts import Joint
import time


joint1 = Joint(18, [1200, 1800])
joint1.goMax()
time.sleep(1)
joint1.goMin()
