# CI GitHub Actions Demo

This repository contains GitHub Actions workflows demonstrating various CI/CD patterns and configurations.

## GitHub Actions Workflows

### Task 1 - Basic CI with Container (`task1.yml`)
**Triggers:** Push to main branch, Manual dispatch

A simple CI workflow that demonstrates:
- Running in a Python 3.11 container
- Basic checkout and echo operations
- Container-based execution on Ubuntu

**Jobs:**
- `test`: Runs on ubuntu-latest with python:3.11 container
  - Checks out code
  - Displays "Hello, CI with GitHub Actions!" message

### Task 2 - Python Unit Testing (`task2.yml`)
**Triggers:** Push to main branch, Manual dispatch

A Python testing workflow that:
- Sets up Python 3.9 environment
- Runs unit tests using unittest framework
- Provides test completion feedback

**Jobs:**
- `test`: Runs on ubuntu-latest
  - Checks out code with actions/checkout@v4
  - Sets up Python 3.9
  - Discovers and runs tests from `tests/` directory
  - Outputs success message upon completion

### Task 3 - Scheduled Workflow (`task3.yml`)
**Triggers:** Daily at 00:00 UTC (cron), Manual dispatch

A scheduled workflow demonstrating:
- Cron-based automation
- Daily build execution
- Time-based CI operations

**Jobs:**
- `build`: Runs on ubuntu-latest
  - Checks out code
  - Executes scheduled task with success message

### Task 4 - Matrix Strategy Testing (`task4.yml`)
**Triggers:** Push to main branch, Manual dispatch

An advanced workflow using matrix strategy for cross-platform testing:
- Tests across multiple operating systems
- Tests multiple Python versions
- Includes custom matrix configurations

**Jobs:**
- `test`: Matrix strategy across:
  - **OS:** ubuntu-latest, windows-latest
  - **Python versions:** 3.8, 3.9, 3.10
  - **Special case:** ubuntu-22.04 with Python 3.7
  - Runs unit tests on all combinations
  - Reports Python version and OS in completion message

## Workflow Features Used

- **Triggers**: push, workflow_dispatch, schedule (cron)
- **Containers**: Python 3.11 container usage
- **Matrix Strategy**: Cross-platform and multi-version testing
- **Actions**: checkout@v3/v4, setup-python@v4
- **Test Framework**: Python unittest discovery pattern
