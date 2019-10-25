# Open Impact API

## Usage

* Create a virtualenv
* Install dependencies `python install -r requirements.txt`
* Run the app locally `python main.py`

## Deploy

* Make sure you have `AWS_SECRET_KEY_ID` and `AWS_SECRET_ACCESS_KEY` setup (Ask Kevin/Rafe for keys).
* Run `zappa update production` to update the production environment.

## Structure

* `endpoints.py`: contains a POST endpoint that takes a list of events as json, compute CO2 then warming equivalent and returns it.
* `convert_co2.py`: module that computes co2 from a list of events
* `compute_warming.py`: module that computes warming equivalent based on co2