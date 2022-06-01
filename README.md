
# Summary Transactions Email for Customers - Stori

This system is based in Flask and Python 3.10

The main goal of the system is to Send an Email to the Customer 
with the details of their month transactions.

The system needs an input of a CSV File where there should be transactions in the following way:

```
Id,Date,Transaction
0,7/15,+60.5
1,7/28,-10.3
2,8/2,-20.46
3,8/13,+10
```

There is also an example of this file called `data.csv` in the root path of this repository.

## Setup

Download the repository and once you are in the folder, copy the .env.dist file to create a .env file

```bash
cp .env.dist .env
```

In that file there are the configurations needed for the mail to be sent, for default is configured to use a Gmail Address as a Email Server, you will need to put your password of the email in order to work

After that you can just execute: 

```bash
docker compose up
```

This will automatically build the Python image configured in the DockerFile, install the needed packages and run inthe

For local purposes the image is mapping the `7007` port of your localhost in order to run the system

You will have access into `http://127.0.0.1:7007`

And example of the Email Sent will be like the following:

![Email Example](/static/images/email-example.png "Email Example")

You can edit the HTML for the email in case you want to add some customization, directly in the `templates/email.html` file.
Just need to remember that this HTML is not meant to be executed in the browser, but is meant to be sent into an email account.
So you will need to put attention to not add customization that doesn't work in most email clients.

## Database

The project includes a Docker Image of MySQL where the transactions is gonna be stored, when the `docker compose up` is executed the instance of mysql server will be up as well.
To access locally to the DB you can add to your `/etc/hosts` file the following line:

```
127.0.0.1       db
```

With this you can configure your client to acess to the DB with the following configurations:

```
host: db
db: stori
user: stori-user
password: story-secret
port: 13306  // Notice that the port is different than the default to not have conflicts with a local mysql server
```

Each time that you update the page all registries are gonna be deleted and will be recreated in base to the `data.csv`
The data will be stored as it shows:

![Database Example](/static/images/database-example.png "Database Example")