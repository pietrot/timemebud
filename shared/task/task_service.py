import time
from datetime import datetime

from shared.task.task import *
from shared.util.time_util import *

class TaskService:
    
    """ Task Service
    """

    def track(self, taskDescr):

        print("(CTRL-C at any time to stop the timer and record your task)\n")
        
        # Record start time
        startTime = datetime.utcnow()

        try:
            while True:
                # Calc elapsed time
                diff = datetime.utcnow() - startTime

                # Print formated time on same line - 0:00:00.000000 to 0:00:00
                print("\r", str(diff).split(".")[0], sep='', end='')
                time.sleep(1) # Arg in seconds

        except KeyboardInterrupt:
            # Record end time
            endTime = datetime.utcnow()
            diff    = endTime - startTime
            
            choice = input("\nRecord task? [y]/n: ").strip()
            
            if choice.lower() in ("y", "yes", ""):
                task            = Task()
                task.start_time = datetime.strftime(startTime, "%Y-%m-%d %H:%M:%S.%f")
                task.time_spent = TimeUtil.fromSeconds(diff.total_seconds(), "hrs", 4)
                task.descr      = taskDescr.strip("\"")
                return task

        return None
