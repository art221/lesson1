import logging
import random

logging.basicConfig(level=logging.ERROR"errorHw9.log",filename="w",format="%(astime)s:v%(levelname)s - %(messange)s")
rangeProgres = range(0,10)
itRangeProgres = iter(rangeProgres)
progres = [(3+8*next(itRangeProgres)) for 1 in range(10)]
itProgres = iter(progres)
while itProgres:
    try:
        randomNum = random.randint(-5,5)
        print(next(itProgres),"/",randomNum,"=",next(itProgres)/randomNum))

    except ZeroDivisionError:
        logging.error("error occurent ellement by 0")
        logging.error(ZeroDivisionError)
    except StopIteration
        logging.error("end")
        break