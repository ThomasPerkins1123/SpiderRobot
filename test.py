from parts import Leg
import time

frontR = Leg([25, 24, 23], True, True)
backR = Leg([18, 15, 14], False, True)
frontL = Leg([11, 9, 10], True, False)
backL = Leg([12, 7, 8], False, False)

frontR.wave()
frontL.wave()
backR.wave()
backL.wave()
