# Instawork-Interview 
> This project contains 5 APIs 
> which can be used to CREATE, READ, UPDATE, DELETE Team Members
> The URL will be `/team/` , GET, POST, PUT & DELETE are the exposed methods.
> To get Team Mmeber by ID, the URL will be `/team/?member_id=<int>`

### Tech
* Python
* Django
* Django_Rest_Framework
* MySQL

### MySQL Settings
Make sure you have MySQL server up and running
```
    create database instawork_interview;
```
MySQL 8.0+ uses `caching_sha2_password` as the default plugin which is not supported by Django MySQL client.
Run the following query to change your plugin from `chaching_sha2_password` to `mysql_native_password`
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<your_password>';
```


### Installation
1) Make sure you have Python-3.6 installed
2) Python3 needs `mysql-connector-c` to be installed by `brew` if you are on **mac**
3) Open your MySQL server and run this command:
4) Clone the repo
5) Create a venv `python3 -m venv venv; source venv/bin/activate`
6) Install the requirements `pip3 install -r requirements.txt`
7) Edit the `config.py` file with your `user`, `password`, `mysql_host`, `port` to make this code connect to the right database;
8) Run `python3 manage.py migrate` to create the required tables.
9) Finally, run the server with `python3 manage.py runserver`

### Exposed End Points
`curl -X GET http://localhost:8000/team/`
```
URL: /team/
Method: GET 
Response: {
    members: [
        {
            firstName,
            lastName,
            role,
            email,
            phone,
        }
    ]
}
```
&NewLine;
`curl -X GET http://localhost:8000/team/?member_id=1`
```
URL: /team/?member_id=<int>
Method: GET 
Response: {
    firstName,
    lastName,
    role,
    email,
    phone,
}
```
&NewLine;
`curl -X POST http://localhost:8000/team/ -d '{"firstName": "Isha", "lastName": "Gupta", "mobile": "+91-9585364407", "role": "Admin", "email": "ishagpt8@gmail.com"}'`
```
URL: /team/
Method: POST 
Request Body: {
    firstName,
    lastName,
    role,
    email,
    phone,
}
Response: {
    firstName,
    lastName,
    role,
    email,
    phone,
}
```
&NewLine;
 `curl -X PUT http://localhost:8000/team/1/ -d '{"mobile": "+91-1234567890", "email": "ishagupta97@gmail.com"}'`
```
URL: /team/<member_id>/
Method: PUT
All the fields are optional in request body.
Request Body: {
    [firstName],
    [lastName],
    [role],
    [email],
    [phone],
}
Response: {
    firstName,
    lastName,
    role,
    email,
    phone,
}
```
&NewLine;
`curl -X DELETE http://localhost:8000/team/1/`
```
URL: /team/<member_id>/
Method: DELETE
Response: {
    "message": "Member ID <member_id> is deleted."
}
```

