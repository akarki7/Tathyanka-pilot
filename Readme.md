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
  * https://www.python.org/downloads/ 
* `pipenv`
  * to install run `pip install pipenv`
* Add your own .env file according to the .env_sample provided

### How to run
* run `pipenv shell` to activate/create your virtual env
* run `pipenv install` to install requirements 
* run `pipenv install -r requirements.txt` to install streamlit 

#### For streamlit UI
* From the root directory run `streamlit run app.py`

#### For web scraper
* `cd webscraper` and run `python -m nrb_scraper` 
  * The downloaded file will be saved here with the name given in the website itself eg (2079-05 (Mid Sept, 2022).xls)
  * This will also produce the output file named `final_data.csv` with the extracted data

*  `python script_cleaner.py -d "207905 BHADRA"` to get the cleaned data of Sheet 8 (Assets and Liabilities)


### Link for google collab
https://colab.research.google.com/drive/1X1gpnKj8D0siPdLrVZLoXLUrVL78EuSn?usp=sharing

In this google collab I have written the script for training the ML model with WikiSQL dataset


### Features implemented
--------------------------
#### Backend

* Web scraper which downloads the monthly statistics file from NRB website and extracts data from sheet C4

#### Frontend

* UI page with a search form

### Folder and File Descriptions: (only the important folders/files are listed)
--------------------------
    ├── static
        ├── css
        ├── img
    ├── webscraper
        ├── nrb_scraper.py (main webscraper file for NRB)
    ├── app.py (main file that hosts streamlit UI and also contains logic of NLP)
    ├── utils.py (contains util functions that are used by app.py)
    ├── requirements.txt and Pipfile (contains all the dependencies)
    ├── Extra findings (contains extra information I saved for myself)
    
### Notes for the contributors
------------------------------
* To add any new feature please fork the repo and create a Pull Request with main
* If you find any bug please create a issue in the Github repo. For other security issue you can contact at `karkiaabishkar@gmail.com`.

