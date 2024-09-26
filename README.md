# Description
This example of an ETL pipeline is designed to store data extracted from the front-end into PostgreSQL.

## Technique
* **Python**
* **Libraries**: BeautifulSoup, urllib, pandas, pyyaml
  ``` bash
  pip install -r requirements.txt
* **Database**: Postgresql
* **Database Management**: pgAdmin 4
## Workflow
* Extract category in the menu, an output is list of url (Subcategory)
* Using each input as parameter for page_parsing, which is parsing data of every products on fixed number page (customable)
* Store raw data into Postgresql
## Start 
* Initialize database
  ``` bash
  python database/init_db.py
* Start the `main_build.py` file
    ``` bash
  python main_build.py
## Next step
* clean raw data for useable
* create pipeline for scheduling run
* apply model, analysis

