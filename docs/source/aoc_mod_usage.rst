**aoc-mod** script
=====================================

The **aoc-mod** command-line script can be used for automatically setting up a challenge project folder 
structure and pulling an Advent of Code day's challenge input and instructions. It can also be used 
for submitting answers to Advent of Code.

.. program-output:: aoc-mod --help

----------------

==========================
Setup a solution directory
==========================

.. program-output:: aoc-mod setup --help

The first main option of the **aoc-mod** script is the creation of a solution directory that takes the 
form "challenges/<year>/day<day_num>". By default, three files will be created in each new directory:

* ``input_day<day_num>.txt`` - the puzzle input
* ``instructions_day<day_num>.md`` - the puzzle instructions
* ``day<day_num>.py`` - a template code file that will be default provided in the project or custom

-----------------------
Setting a template file
-----------------------

The ``template path`` is a path to a file that will be copied into each new solution directory and can
be created by a user for their own challenges. An example Python file is included in the default Advent of 
Code module and can be created by not setting this option. 

The file can take on any format that is necessary and be of any programming language. However, AOC Mod 
supports two strings that are found and replaced when the template file is generated:

* ``{YEAR}`` - replaced with the puzzle year
* ``{DAY}`` - replaced with the puzzle day

These are used in the template file docstring to make it unique for each solution puzzle directory but are
not required for user-created templates. 

--------------------------------
Setting an output root directory
--------------------------------

The ``output root directory`` argument is the directory that will be prepended to the ``challenges`` 
solution output directory. If the directory doesn't exist, it will be created relative to the current
directory.

----------------

=====================
Submit puzzle answers
=====================

.. program-output:: aoc-mod submit --help

Most likely, this will be the most useful feature to users of AOC Mod. This option will take in a solution
from the user and, if the SESSION_ID is set, will submit (post) that answer to the Advent of Code website.

The response will be received from Advent of Code's website and displayed to the user in the terminal.

----------------

**NOTE:** See the `SESSION_ID section`_ for more information about which operations are supported with
and without a session id.

.. _SESSION_ID section: index.html#getting-and-using-the-session-id
