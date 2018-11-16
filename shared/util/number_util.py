import locale

class NumberUtil:
    
    """ Number Utility
    """
    
    def toCurrency(n):
        
        """ Convert given number into currency format.
        
        Args:
        n (float): Number to convert.

        Returns:
        string
        """

        if not isinstance(n, float):
            n = float(n)
        
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return locale.currency(n, grouping = True)
