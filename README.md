# Setup

## Install dependencies
````
python3 -m venv /path/to/new/virtual/environment
source venv/bin/activate
pip install -r requirements.txt
````

## Train model
````
python nlp_setup.py
python nlp_train.py
````

## Start service
````
export FLASK_APP=server.py
flask run
````

# Usage

````
GET http://127.0.0.1:5000/analyze/<video_id>
````