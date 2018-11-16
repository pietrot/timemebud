# TIMEMEBUD CLI

A simple time tracking CLI for all terminal junkies out there.


## Installation

TIMEMEBUD CLI requires _Python 3+_ in order to run properly. For Mac OS users, you can install Python using _homebrew_:

```
$ brew install python
$ python --version
$ pip --version
```

TIMEMEBUD does have a few dependencies. You can install these globally or locally using _pipenv_.

```
$ brew install pipenv
```

[Latest Pipenv Documentation](https://pipenv.readthedocs.io/en/latest)

To install dependencies:

```
$ cd /path/to/timemebud/folder
$ PIPENV_VENV_IN_PROJECT=true pipenv install
```

Finally, to run TIMEMEBUD:

```
$ cp config.ini.example config.ini
$ PIPENV_VENV_IN_PROJECT=true pipenv shell
```

----

## TODOs

- [ ] Create a setup script to install TIMEMEBUD via pip's registry.
- [ ] Filter log by date.
- [ ] Filter log by labels.
- [ ] Implement method for assigning label colors.
- [ ] Implement method for generating PDF invoices from task logs.

## Changelog

**Updates** - _v0.1.0_
* Implemented a simple CLI for tracking tasks.
* Implemented file-based logging strategy.
* Introduced _workspaces_ - allowing users to track tasks across organizations, projects, and so on.
