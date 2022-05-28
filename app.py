from flask import Flask, render_template
import os
from src.functions import *

app = Flask(__name__)

@app.route("/")
def main():
    return parseCSV()        

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7007))
    app.run(debug=True, host='0.0.0.0', port=port)