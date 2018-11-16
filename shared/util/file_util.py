import os

class FileUtil:
    
    """ File Utility
    """
    
    def getFiles(dirpath, depth = 1, ext = None, hideExt = False, exclude = []):
        
        """ Get list of files found in the specified directory.

        Args:
        dirpath (string): The directory path.
        depth (integer): Optional - The depth of the dirtree required for the search.
        ext (string): Optional - Filter file extensions.
        hideExt (boolean): Optional - Hide file extention?
        exclude (array): Exclude these files
        
        Returns:
        array: List of files.
        """

        filenames = []

        for filename in os.listdir(dirpath):

            if filename in exclude:
                continue;

            validFilename = None

            if ext is not None:
                if filename.endswith("."+ext.lstrip('.')):
                    validFilename = filename

            else:
                validFilename = filename
            
            if validFilename:
                if not hideExt:
                    filenames.append(validFilename)
                
                else:
                    filenames.append([ validFilename.split('.')[0] ])
        
        return filenames

    def writeline(filepath, line):
        
        """ Write line in file.

        Args:
        filepath (string): The file path.
        line (string): Line to write.

        Returns:
        void
        """

        f = open(filepath, "a+")
        f.write(line + "\n")
        f.close()
    
    def readlines(filepath):
        
        """ Read file lines.

        Args:
        filepath (string): The file path.

        Returns:
        array: List of lines in file.

        """

        f = open(filepath, "r")
        return f.readlines()
