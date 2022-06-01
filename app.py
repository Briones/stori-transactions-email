from flask import Flask, render_template
import os
from src.functions import *

app = Flask(__name__)

@app.route("/")
def main():
    create_connection()
    create_transactions_table()
    truncate_transactions_table()
    html = parseCSV()    
    return html

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7007))
    app.run(debug=True, host='0.0.0.0', port=port)