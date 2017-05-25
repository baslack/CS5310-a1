# CS5310-a1
Benjamin A. Slack
05.25.2017
benjamin.a.slack@wmich.edu

Grader:
Job consists of two executable python scripts, a1.py & test_sorts.py, as well as a small python package with the bulk
of the implementation. All scripts have been coded using Python 2.7.13. Python shebang lines have been added to the
executable scripts, so that on Linux or OSX they should run using the correct version of python. However, on windows
the user will need to execute with the appropriate python interpreter. Assuming that python is installed on your path,
you should be able to run the scripts as follows:

<prompt>/python a1.py ...
<prompt>/python test_sorts.py

a1.py supports a few command line options. By default it will run tests of all the qsort and select configurations
required by the assignment, using values of n in the list [10, 20, 40, 80, 160, 320, 640, 1280, 2560], taking averages
over 1000 iterations with a maximum integer value of 10000 in the list. Note, this can take not insignificant amount of
time to run. Therefore the following command line flags can be added.

-n <int> <int> <int> ..., execute all tests for the given integer values of n
-m <int>, set the maximum value for elements of the list
-i <int>, set the number of iterations for averaging the time measurements
-f <string>, set the filename of the output file

Results of the execution will be output to stdout as well as the output file.

NOTE!: The output file will be truncated should it already exist.