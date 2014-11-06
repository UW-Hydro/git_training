#!/usr/bin/env python
"""
hello_hydro.py

An example module used for teaching the UW Land Surface Hydrology Group how to
use Python, Git, and Github.
"""

import letters

def main():

    # Say hello to the world
    letters.hello_world()

    # Say hello to Joe
    letters.hello_name('Today is Thursday')

    # Add your own hello function to letters.py
    # Then call that function from here...

    # All done, say goodbye
    letters.goodbye_world()

    return


if __name__ == "__main__":
    main()
