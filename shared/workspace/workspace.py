import os

class Workspace:
    
    """ Workspace Model
    """

    config = None
    name   = None
    path   = None

    def __init__(self, config):
        
        """ Default constructor.
        """
        
        self.config = config

    def set(self, workspace):
        
        """ Set workspace.

        Args:
        workspace (string): The workspace name.

        Returns:
        void
        """

        self.name = workspace
        self.path = self.config["WORKSPACE"]["path"].rstrip("/") + "/{}".format(workspace)

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def getTaskLogPath(self):
        
        """ Get task log filepath.

        Returns:
        string
        """

        return self.path + "/task.log"


    def getTodoLogPath(self):
        
        """ Get todo log filepath.

        Returns:
        string
        """
        
        return self.path + "/todo.log"
