# Albumy


ML-Powered Features
This fork includes two machine learning features using open-source models from HuggingFace:
1. Auto-Generated Alt Text

Automatically generates descriptive captions for uploaded images using BLIP (Salesforce)
Improves accessibility with meaningful alt text for screen readers
Example: "a dog sitting in grass" or "a parking lot with buildings"

2. Keyword-Based Image Search

Detects objects in images using CLIP (OpenAI) for zero-shot classification
Enables searching photos by content without manual tagging
Search for: "dog", "person", "food", "nature", "building", etc.

Pretrained Models Used:

BLIP for image captioning
CLIP for object detection

No API keys required - models run locally on your machine.

## Installation

Note: This version of Albumy requires Python 3.9 due to compatibility with older dependencies. 
Python 3.10+ will not work without an update package rabbit hole. 

clone:
```
$ git clone https://github.com/rgotzmann/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ brew install python@3.9
$ python3.9 -m venv env 
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
Note: This installs all dependencies including ML models (transformers, torch). 
First install may take a few minutes.

or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
Initialize database, generate fake data then run:
```
$ flask initdb
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

Using the ML Features

Auto-Generated Alt Text
When uploading an image:

Blip automatically generates a descriptive caption 
If you don't provide a description, the alt text becomes the description
Alt text is always generated for accessibility (and is visible in HTML <alt> attribute)

Keyword-Based Search
To search for images by content:

Use the search box in the navigation bar
Type keywords like: dog, cat, person, food, nature, building, beach, sunset
CLIP's zero-shot classification searches through detected objects
Results include all photos containing the detected objects, even if not manually tagged

Note: The first image upload will download ML models (~1GB) - this only happens once.

Technical Details
ML Implementation

  Model Storage: ~/.cache/huggingface/hub/ (automatic caching)
  Alt Text Field: Photo.alt_text (VARCHAR 500)
  Search Keywords: Photo.img_search (TEXT, comma-separated objects)
  Search Engine: Whooshee indexes both alt_text and img_search fields
  Processing Time: ~2-5 seconds per image (first time slower due to model loading)

Files Modified for ML Features

  albumy/models.py - Added alt_text and img_search fields to Photo model
  albumy/ml.py - ML script for image analysis
  albumy/blueprints/main.py - Integration in upload route
  albumy/utils.py - Updated PIL.Image.ANTIALIAS → LANCZOS for Pillow 10+ compatibility

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
