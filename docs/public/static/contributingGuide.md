---
title: Contributing
---

# Contributing to py-iot-utils

If you would like to become an active contributor to this project, please submit an [issue](https://github.com/dgonzo27/py-iot-utils/issues) with the _contributor_ template.

## Branching Strategy

In this strategy, there is only a single branch or _"source of truth"_ - the `master` branch. The idea behind this strategy is to minimize the amount of human interaction required to maintain branches and to minimize the overrall number of maintained branches in general.

- When developing a new feature or resolving a bug, checkout to a `features/*` or `bugs/*` branch using your approved GitHub issue number. For example, `features/git-issue-6`.

- When you are finished developing, you'll push your code and create a pull request to the `master` branch.

- Once the branch is approved and merged the branch will be deleted.

## Building and Testing

1. Clone the repository or pull the latest changes from `master`.

   ```sh
   git clone git@github.com:dgonzo27/py-iot-utils.git && cd py-iot-utils

   git pull origin master
   ```

2. Install and enable [pre-commit](https://pre-commit.com).

   ```sh
   pre-commit install
   ```

3. Checkout to a `features/*` or `bugs/*` branch.

   ```sh
   git checkout -b features/git-issue-27
   ```

4. Create and activate a virtual environment.

   ```sh
   python3 -m venv .venv

   source .venv/bin/activate
   ```

5. Install `dev-requirements.txt`.

   ```sh
   python3 -m pip install --upgrade pip

   python3 -m pip install -r requirements-dev.txt
   ```

6. Build a package.

   ```sh
   cd iot-storage-client

   python3 -m build

   cd ..
   ```

7. Test a package.

   ```sh
   cd iot-storage-client

   coverage run -m unittest discover tests

   coverage report -m

   cd ..
   ```

8. Deactivate virtual environment.

   ```sh
   deactivate
   ```

## Supporting the Official Documentation

This application is developed using [React](https://reactjs.org) and [Material UI](https://mui.com/material-ui/). It is packaged into a [Docker](https://www.docker.com) image that leverages a multi-stage build, running [NGINX](https://nginx.org) under the hood. This image is deployed to the [Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/) and is run as a containerized [App Service](https://docs.microsoft.com/en-us/azure/app-service/overview) all through the use of [Terraform](https://www.terraform.io) and [GitHub Actions](https://github.com/features/actions).

In order to support and develop against the official documentation app, there are a few pre-requisites.

1. Local development should be done from a UNIX-based machine - use Linux, MacOS or WSL2 if you're on a Windows machine.

2. NPM should **not** be installed globally on your machine. Instead, manage your version of NPM with [Node Version Manager](https://github.com/nvm-sh/nvm). This application is currently being developed with the LTS version of node - v16.16.0 at the time of writing (npm v8.11.0).

3. [Docker Desktop](https://www.docker.com/products/docker-desktop/) should be installed on your machine for building and validating images that are run in cloud environments. It is not sufficient to only develop and test using the `npm start` command. You will want to build and run your Docker images to ensure a successful deployment to the cloud.

## Code of Conduct

Before contributing to this repository, please review the [code of conduct](/codeOfConduct).
