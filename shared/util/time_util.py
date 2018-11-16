import re

class TimeUtil:
    
    """ Time Utility
    """
    
    def toSeconds(val):
        
        """ Convert value of unit time to seconds.

        Args:
        val(mixed): Value to be converted into seconds. Can be in decimal hours (##.#), for timespan format (##:##:##).

        Returns:
        integer
        """
        
        secs                   = 0
        inputPattern           = None
        availableInputPatterns = {
            "decimal"  : "^[0-9]+(\.[0-9]+)?$",                  # Decimal format representing hours.
            "timespan" : "^[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}$"    # Timespan format
        }
        
        for key, pattern in availableInputPatterns.items():
            if re.search(pattern, val, re.M|re.I) is not None:
                inputPattern = key
        
        if inputPattern is None:
            raise ValueError("Value is not in the correct format.")
        
        if inputPattern == "decimal":
            val          = val.replace(",", "")
            decimalParts = val.split(".")
            secs         = int(decimalParts[0]) * 60 * 60
        
            if len(decimalParts) > 1:
                secs += float("." + decimalParts[1]) * 60 * 60
        
        elif inputPattern == "timespan":
            timespanParts = val.split(":")
            secs = int(timespanParts[0])*60*60 + int(timespanParts[1])*60 + int(timespanParts[2])
            
        return secs

    def fromSeconds(secs, unit, precision = 1):

        """ Convert value in seconds to some other unit of time.

        Args:
        secs(integer): Seconds
        unit(string): A unit of time - ie. hrs, mins, etc.

        Returns:
        mixed
        """

        if unit.lower() in [ "hrs", "hours" ]:
            return round(secs / 60 / 60, precision)

        else:
            raise NotImplementedError("Conversion logic for specified unit is not implemented!")
