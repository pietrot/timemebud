class StringUtil:
    
    """ String Utility
    """
    
    def wordwrap(text, n):
        
        """ Returns a string where \\n is inserted between every n words

        Args:
        text (string):
        n (integer): Wrap to nth number of words.

        Returns:
        string
        """

        text = text.strip();
        
        # Determine if text is empty:
        if text == "":
            # If so, return
            return text;
        
        # Otherwise, let's wrap it up!
        
        if not isinstance(n, int):
            n = int(n)
        
        words       = text.split()
        wrappedText = ''
        
        for i in range(0, len(words), n):
            wrappedText += ' '.join(words[i:i+n]) + "\n"

        return wrappedText
