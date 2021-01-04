from flask import Flask
from main import comments_analysis

app = Flask(__name__)

@app.route('/analyze/<string:id>')
@app.route('/analyze/<string:id>/<string:page_token>')
def analyze(id, page_token=None):
    result = None
    
    try:
      result = comments_analysis(id, page_token)
    except Exception as e:
      print(e)
    
    return result