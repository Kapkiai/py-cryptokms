.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/kapiai/pycrypto/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Py-Crypto could always use more documentation, whether as part of the
official Py-Crypto docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/kapkiai/pycrypto/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `pycryto` for local development.

1. Fork the `pycryto` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:kapkiai/pycrypto.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv pycrypto
    $ cd pycrypto/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. You may want to leverage the provided Docker configuration for testing and development

 - Install the latest version of Docker
 - Use the provided Docker Compose configuration in ./resources/docker/latest and run the tests::

    $ cd resources/docker/latest
    $ docker-compose up -d
    $ cd ../../../
    $ tox
    $ cd resources/docker/latest
    $ docker-compose stop


6. When you're done making changes, check that your changes pass the tests, including testing other Python versions, with tox::

    $ tox

7. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7 and 3.6, and for PyPy. Check
   https://travis-ci.org/kapkiai/pycrypto/pull_requests
   and make sure that the tests pass for all supported Python versions.
4. Pull requests should be created against the 'next' branch for new features, or 'master' for critical patches to current functionality.
