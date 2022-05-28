from posixpath import split
from flask import Flask, render_template
import os
import math

import pandas as pd
import smtplib
import datetime
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def parseCSV():
    """
    Read the CSV file and return an HTML
    """  
    df = pd.read_csv(r'data.csv')
    calculate_amount_values(df)
    html = render_html()

    send_email(html, os.getenv('EMAIL_FROM'), os.getenv('EMAIL_TO'), os.getenv('EMAIL_SUBJECT'))
        
    return html


def parse_date(date):
    """
    Get the date in a format "Month/Day" like "7/18"
    transform it into a datetime of the current year
    and return the datetime without formatting.
    """ 
    dateSplited = date.split('/')
    
    realDate= datetime.datetime(datetime.datetime.now().year, int(dateSplited[0]), int(dateSplited[1]))
    return realDate

def calculate_amount_values(df):
    global transactions
    global creditAmounts
    global debitAmounts
    global transactionsAmount
    transactionsAmount = {}
    creditAmounts = []
    debitAmounts = []
    transactions = []
    
    for ind in df.index:
        if(df['Transaction'][ind] < 0):
            debitAmounts.append(df['Transaction'][ind])            
        else:
            creditAmounts.append(df['Transaction'][ind])            
        transactionsAmount[parse_date(df['Date'][ind]).strftime("%B")] = transactionsAmount.get(parse_date(df['Date'][ind]).strftime("%B"), 0) + 1            
        transactions.append([parse_date(df['Date'][ind]), str(df['Transaction'][ind])])
    return
    


def render_html():
    return render_template('/email.html', transactions=transactions, total_balance=calculate_total_balance(debitAmounts, creditAmounts)[0], transactionsAmount = transactionsAmount.items(), debitAverage = calculate_total_balance(debitAmounts, creditAmounts)[1], creditAverage = calculate_total_balance(debitAmounts, creditAmounts)[2])    

def calculate_total_balance(debitAmounts, creditAmounts):
    total = 0
    global debitAverage
    debitAverage = 0
    debitTotal = 0
    debitCount = 0

    global creditAverage
    creditAverage = 0
    creditTotal = 0
    creditCount = 0
    totalBalance = 0

    for debitAmount in debitAmounts:
        totalBalance += debitAmount
        debitTotal += debitAmount
        debitCount = debitCount + 1

    for creditAmount in creditAmounts:
        totalBalance += creditAmount
        creditTotal += creditAmount
        creditCount = creditCount + 1

    debitAverage = debitTotal / debitCount
    creditAverage = creditTotal / creditCount

    return [totalBalance, debitAverage, creditAverage]

def calculate_grouped_transactions_by_month():    
    for debitAmount in debitAmounts:
        var=0
    for creditAmount in creditAmounts:
        total += creditAmount

def send_email(html, toEmail, fromEmail, subject):
    message = MIMEMultipart('alternative')
    message['subject'] = subject
    message['To'] = toEmail
    message['From'] = fromEmail

    # Setting the image from the file
    with open('static/images/stori-logo.png', 'rb') as f:
    
        mime = MIMEBase('image', 'png', filename='stori-logo.png')    
        mime.add_header('Content-Disposition', 'attachment', filename='stori-logo.png')
        mime.add_header('X-Attachment-Id', '0')
        mime.add_header('Content-ID', '<0>')        
        mime.set_payload(f.read())        
        encoders.encode_base64(mime)
        message.attach(mime)

    
    server = smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT'))
    server.starttls()
    server.login(os.getenv('EMAIL_ORIGIN'), os.getenv('EMAIL_PASSWORD'))
    content = MIMEText(html, "html")
    message.attach(content)

    server.sendmail(fromEmail, toEmail, message.as_string())
    print('Mail Sent')