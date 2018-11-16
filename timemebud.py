#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getopt, sys

from app.app import *

__version__   = "0.1.0"

def main():
    
    """ Main entry point for the application.
    """ 

    app = App()
    
    try:
        if len(sys.argv) > 1:
            # [1:] is equivalent to "1 to end"
            app.onecmd(" ".join(sys.argv[1:]))

        else:
            app.cmdloop()

    except KeyboardInterrupt:
        print("\nHave a wonderful day!\n")
        quit()

if __name__ == "__main__":
    main()

