### Write Unit Tests
You will test your code in two steps.

The first step involves linting—running a program, called a linter, to analyze code for potential errors. **flake8** is commonly used to check if your code conforms to the standard Python coding style. Linting makes sure your code is easy to read for the rest of the Python community.

To run your linter, execute the following:
bash`
    $ flake8 --statistics
    ./calculator.py:3:1: E302 expected 2 blank lines, found 1
    ./calculator.py:6:1: E302 expected 2 blank lines, found 1
    2     E302 expected 2 blank lines, found 1
`

The second step is unit testing. A unit test is designed to check a single function, or unit, of code. Python comes with a standard unit testing library, but other libraries exist and are very popular. This example uses **pytest**.

A standard practice that goes hand in hand with testing is calculating code coverage. Code coverage is the percentage of source code that is **“covered”** by your tests. **pytest** has an extension, *pytest-cov*, that helps you understand your code coverage.

The following command runs your test:

`$ pytest -v --cov`

pytest is excellent at test discovery. Because you have a file with the prefix test, pytest knows it will contain unit tests for it to run. The same principles apply to the class and method names inside the file.

The -v flag gives you a nicer output, telling you which tests passed and which failed. In our case, both tests passed. The --cov flag makes sure pytest-cov runs and gives you a code coverage report for calculator.py.