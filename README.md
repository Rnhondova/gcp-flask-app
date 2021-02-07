![CI](https://github.com/Rnhondova/gcp-flask-app/workflows/CI/badge.svg)

# Sample flask app deployed using GCP app engine
- Continuous integration (CI) implemented using github actions
- Continuous deployment (CD) implemented using GCP

Application is located [here](https://flask-app-gcp.ue.r.appspot.com).

## Application routes
- /next_business_day/from_date : This is function that will supply next business day from supplied date, taking into account US bank holidays with date supplied in the mm-dd-yyyy format (e.g. /02-25-2021).
- /name/supply_name: e.g. /name/Ronald
