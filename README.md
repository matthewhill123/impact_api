# Open Impact API

## Setup

* Create a virtualenv with Python 3.7: `virtualenv venv -p python3.7`
* Install dependencies `python install -r requirements.txt`

## Contribute

* There are two protected branches `dev`, `master`
    * `dev`: latest stable version of code
    * `master`: automatically gets deployed to production
* Create a new branch from dev: `git checkout -b <new_branch_name>` 
* When you're done, open a pull request to `dev`
* To release on production, create a merge request from `dev` to `master`

## Usage

* Run the app locally `python main.py`

## Deploy

* Make sure you have `AWS_SECRET_KEY_ID` and `AWS_SECRET_ACCESS_KEY` setup (Ask Kevin/Rafe for keys).
* Run `zappa update production` to update the production environment.

## Structure

* `endpoints.py`: contains a POST endpoint that takes a list of events as json, compute CO2 then warming equivalent and returns it.
* `convert_co2.py`: module that computes co2 from a list of events
* `compute_warming.py`: module that computes warming equivalent based on co2