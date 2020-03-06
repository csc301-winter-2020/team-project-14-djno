## Gmail for both google developer and apple developer account use
gmail: teamproject14djno@gmail.com <br>
password: Csc301Team14<br>



## authentication
[sign-in,sign-out](https://developers.google.com/identity/sign-in/web)<br>
[url set-up for using google sign-in](https://developers.google.com/identity/sign-in/web/server-side-flow)<br>
```json
{
    "web":
    {
        "client_id":"725608313090-l8vr2u5rc91jv9acqogiase3ioctkv02.apps.googleusercontent.com",
        "project_id":"djno-1582242497797",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"865katckHYM9Db2gcQ652k-T","javascript_origins":["http://localhost:5000"]
    }
}
```
## map
This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

## ChatID
const CLIENT_ID = 'VIeKTiBnrEeg0Ce5';

## run code on localhost
1. flask run <br>
2. map: http://localhost:5000/map/map.html <br> 
3. auth: http://localhost:5000/auth/login_signout.html

## depoly web heroku server and database on digital Ocean