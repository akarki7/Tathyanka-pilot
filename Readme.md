# Tathyanka Pilot NLQ


### Architecture Notes
------------------
* Backend is written in Python
* For UI we have used Streamlit
* For NLP models we have used HuggingFace
* For web scraping we have used Beautiful Soup

### Requirements
--------------------------
* `python`
* `pipenv`

### How to run
* run `pipenv shell` to activate/create your virtual env
* run `pipenv install` to install requirements 
* run `pipenv install -r requirements.txt` to install streamlit 

#### For web scraper
* `cd webscraper` and run `python -m nrb_scraper` 
  * The downloaded file will be saved here with the name given in the website itself eg (2079-05 (Mid Sept, 2022).xls)
  * This will also produce the output file named `final_data.csv` with the extracted data

#### For streamlit UI
* From the root directory run `streamlit run app.py`



### Features implemented
--------------------------
#### Backend

* Web scraper which downloads the monthly statistics file from NRB website and extracts data from sheet C4

#### Frontend

* UI page with a search form

### Folder and File Descriptions: (only the important folders/files are listed)
--------------------------
    
### Notes for the contributors
------------------------------
* To add any new feature please fork the repo and create a Pull Request with main
* If you find any bug please create a issue in the Github repo. For other security issue you can contact at `karkiaabishkar@gmail.com`.

