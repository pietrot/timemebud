class Task:
    
    """ Task Model
    """

    start_time = None
    descr      = None
    time_spent = None

    def toLog(self):
        
        """ Convert task model to a readable log string.
        
        Returns:
        string
        """
        
        str = "{0}\t{1}\t{2}".format(self.start_time, self.time_spent, self.descr)
        return str
