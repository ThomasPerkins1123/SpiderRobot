from parts import Spider
import time

Dave  = Spider()



Dave.frontLeft.hip.printStats()
Dave.frontRight.foot.goTo(0)
Dave.frontLeft.foot.goTo(0)
time.sleep(1)
Dave.frontRight.foot.goTo(90)
Dave.frontLeft.foot.goTo(90)
time.sleep(1)
Dave.frontRight.foot.goTo(180)
Dave.frontLeft.foot.goTo(180)
