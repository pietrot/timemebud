import getopt
import configparser
import cmd
import shlex
import os, os.path
from subprocess import call
from datetime import datetime, timedelta

from shared.task.task import *
from shared.util.time_util import *
from shared.util.string_util import *
from shared.util.number_util import *

try:
    import readline

except ImportError:
    readline = None

EDITOR            = os.environ.get("EDITOR", "vi")
HISTORY_FILE      = os.path.expanduser("~/.timemebud_history")
HISTORY_FILE_SIZE = 1000

from shared.workspace.workspace import *
from shared.task.task_service import *
from shared.util.file_util import *
from tabulate import tabulate

class App(cmd.Cmd):
    
    """ App
    """
    
    intro     = None
    prompt    = None

    config    = None
    workspace = None

    def __init__(self):
        
        """ Default constructor.
        """

        super().__init__()

        # Read configuration file
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        
        # Set default workspace
        self.workspace = Workspace(self.config)
        self.workspace.set(self.config["WORKSPACE"]["default"])
        self.setIntro(self.workspace, True) 

    
    def do_log(self, argsStr):
        
        """ Log a task manually.

        Args:
        arg (string):

        Returns:
        void
        """

        args = shlex.split(argsStr)

        unixOptions = "t:d:h:"  
        gnuOptions  = ["task=", "date=", "hrs="] 
        
        try:  
            options, values = getopt.getopt(args, unixOptions, gnuOptions)
        
        except getopt.error as err:  
            # output error, and return
            print(str(err))
            return
        
        descr = None
        date  = None
        hrs   = None

        for opt, val in options:
            if opt in ('-t','-T','--task'):
                descr = val.strip()

            if opt in ('-d','-D','--date'):
                date = val

            if opt in ('-h','-H','--hrs'):
                hrs = val
        
        if descr is None and date is None and hrs is None:
            print("\n*Usage* `TIMEMEBUD> log -t \"Task description goes here...\" -d YYYY/MM/DD -h hrs`\n" )
            return
        
        startTime       = datetime.strptime(date, "%Y/%m/%d")
        timeSpent       = TimeUtil.fromSeconds(TimeUtil.toSeconds(hrs), "hrs", 4)

        task            = Task()
        task.start_time = datetime.strftime(startTime, "%Y-%m-%d %H:%M:%S.%f")
        task.time_spent = timeSpent
        task.descr      = descr
        
        FileUtil.writeline(self.workspace.getTaskLogPath(), task.toLog())        


    def do_track(self, arg):
        
        """ Track a task.
        """

        taskService = TaskService()
        task        = taskService.track(arg)

        if task is not None:
            FileUtil.writeline(self.workspace.getTaskLogPath(), task.toLog())
    
    def do_amend(self, arg):
        
        """ Amend workspace log.
        """

        call([ EDITOR, self.workspace.getTaskLogPath() ])

    def do_highfive(self, arg):

        """ Self praise.
        """

        print("\nF**k yea! Great stuff.\n");
     
    def do_quit(self, arg):
        
        """ Quit.
        """

        print("\nHave a wonderful day!\n")
        return True
    
    def do_exit(self, arg):
        
        """ Quit.
        """

        return self.do_quit(arg)
    
    def do_show(self, what):
        
        """ Show active workspace, available workspaces, or labels.

        Args:
        what (string):

        Return:
        void
        """
        
        what = what.strip().lower()
        
        if what == "workspace":
            print("\n*" + self.workspace.name + "*\n")

        elif what == "workspaces":
            print("\n" + tabulate(FileUtil.getFiles(self.config['WORKSPACE']['path'], 1, None, True, [ ".gitkeep" ]), \
                [ "Workspaces" ], tablefmt="presto") + "\n")
        
        elif what == "log":

            log            = FileUtil.readlines(self.workspace.getTaskLogPath())
            dataset        = [];
            summary        = [];
            totalTimeSpent = None
            totalCost      = None

            for row in log:
                row       = row.strip()
                cols      = row.split("\t")
                
                startTime = datetime.strptime(cols[0], "%Y-%m-%d %H:%M:%S.%f")
                timeSpent = float(cols[1])
                cost      = timeSpent * float(self.config["INVOICING"]["hourly_rate"])
                
                if totalTimeSpent is None:
                    totalTimeSpent = timeSpent

                else:
                    totalTimeSpent += timeSpent
                
                if totalCost is None:
                    totalCost = cost

                else:
                    totalCost += cost

                dataset.append([ datetime.strptime(cols[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%Y/%m/%d"), \
                    StringUtil.wordwrap(cols[2], 10), \
                    round(timeSpent, 1),  NumberUtil.toCurrency(cost)])
            
            summary = [ "--\nSummary", "--\n", "--\n" + str(round(totalTimeSpent, 1)), "--\n" + NumberUtil.toCurrency(totalCost) ]
            dataset.append(summary);

            print("\n" + tabulate(dataset, [ "Date", "Task", "Time Spent (In Hrs)", "Cost ($)" ], tablefmt="presto") + "\n")
        
        else:
            print("\nNone\n")
    
    def do_use(self, workspace):
        
        """ Use workspace.

        Args:
        workspace (string):

        Return:
        void
        """
        
        # Determine if the specified workspace is the current one: 
        if not (self.workspace.name == workspace):
            # If not, switch to the specified workspace.
            self.workspace = Workspace(self.config)
            self.workspace.set(workspace)
            print("\nNow using *{}*!\n".format(workspace))
            self.setIntro(self.workspace)

        else:
            # Otherwise, clear screen.
            self.setIntro(self.workspace)
            
    def setIntro(self, workspace, init = False):
        
        os.system('cls||clear')
        
        self.intro = """
  _______ _____ __  __ ______   __  __ ______   ____  _    _ _____  _
 |__   __|_   _|  \/  |  ____| |  \/  |  ____| |  _ \| |  | |  __ \| |
    | |    | | | \  / | |__    | \  / | |__    | |_) | |  | | |  | | |
    | |    | | | |\/| |  __|   | |\/| |  __|   |  _ <| |  | | |  | | |
    | |   _| |_| |  | | |____  | |  | | |____  | |_) | |__| | |__| |_|
    |_|  |_____|_|  |_|______| |_|  |_|______| |____/ \____/|_____/(_)

    Welcome to TIMEMEBUD CLI. Type help or ? to list commands.

    Current workspace: *{}*

    """.format(workspace.name)
        
        self.prompt = "TIMEMEBUD> "

        if init == False:
            print(self.intro)

    
    # Command lifecycle methods:

    def emptyline(self):
        pass

    def preloop(self):
        if readline and os.path.exists(HISTORY_FILE):
            readline.read_history_file(HISTORY_FILE)

    def postloop(self):
        if readline:
            readline.set_history_length(HISTORY_FILE_SIZE)
            readline.write_history_file(HISTORY_FILE)
