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

CircleCI maintains pre-built Docker images for several programming languages. In the above configuration file, you have specified a Linux image that has Python already installed. That image will create a container in which everything else happens.

Let’s look at each line of the configuration file in turn:

- **version**: Every config.yml starts with the CircleCI version number, used to issue warnings about breaking changes.

- **jobs**: Jobs represent a single execution of the build and are defined by a collection of steps. If you have only one job, it must be called build.

- **build**: As mentioned before, build is the name of your job. You can have multiple jobs, in which case they need to have unique names.

- **docker**: The steps of a job occur in an environment called an executor. The common executor in CircleCI is a Docker container. It is a cloud-hosted execution environment but other options exist, like a macOS environment.

- **image**: A Docker image is a file used to create a running Docker container. We are using an image that has Python 3.7 preinstalled.

- **working_directory**: Your repository has to be checked out somewhere on the build server. The working directory represents the file path where the repository will be stored.

- **steps**: This key marks the start of a list of steps to be performed by the build server.

- **checkout**: The first step the server needs to do is check the source code out to the working directory. This is performed by a special step called checkout.

- **run**: Executing command-line programs or commands is done inside the command key. The actual shell commands will be nested within.

- **name**: The CircleCI user interface shows you every build step in the form of an expandable section. The title of the section is taken from the value associated with the name key.

- **command**: This key represents the command to run via the shell. The | symbol specifices that what follows is a literal set of commands, one per line, exactly like you’d see in a shell/bash script.