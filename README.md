# TextTwilio
This project discovers how to send text messages using twilio. Twilio is a very popular communication platform for adding voice, video, and messageing to your applications. For example, you can quickly make and receive video calls, send text messages. And this perticularly useful for  confirming reservations, sending appointment reminders or promotions the possibilities are endless. 

They provide an API that is prefectly documented and very easy to use. So, we can directly communicate with this API by sending an http requests using the request module. But they also provide a library that we can install using pip or pipenv. This library is essentially a wrapper around the API. So this gives us objects and these objects encapsulate all the http communication. So we no longer have to work at a low level of sending http requests to twilio api. We work at a higher level and a more abstract and simplified fashion.

There are objects, these object has methods, we call them, and they internally take care of sending the right http requests to Twilio API. So the first thing we need to do is create a Twilio account.

## 1. Create twilio account and sign in:
    a. Go to Twilio signup page: https://www.twilio.com/
    b. Fill out the form and signup
    c. Note: You may go through a email loop with Twilio team to activate the account
    d. Then you sign in and create an account 
    e. Thne you are on twilio console: https://console.twilio.com/

## 2. Add phone number:
    a. Click on Phone Numbers item on left menu 
    b. On the page, the first step is get a twilio phone number
    c. So click on the Get a Phone Number button 
    d. Then it gets you back with a phone number and this number w are going to use to send a text message
    e. So let's go ahead and the next step is to send text message.

## 3. Send SMS:
    a. Write the text message in the input box and click on the send button
    b. And on the right hand side you can see the codes in different language and the response
    c. Next step is start building an app

## 4. Start building an app:
    a. Here in the twilio you can build application that could send sms to varified phones numbers
    b. You can get sample codes in different languages

## 5. Tutorial:
    a. You can find tutorial here to flow to build and host the app

## 6. Scale and upgrade twilio app:
    b. Here need to upgrade the account with twilio and scale the app with many functions

## 7. Build own app:
    a. Create a new project and open in vscode:
        i. Go to terminal and create a derectory in users.
            Terminal command: mkdir TextTwilio
        ii. Then go to the directory: cd TextTwilio
        iii. Open in vscode: code .

## 8. Install packages and create virtual environment:
    a. Install twilio: Go back to the vscode Terminal command: pipenv install twilio
    b. That creates virtual environment and at the same time it installs twilio
    c. Then select virtual environment in vscode
       Note: to check the vertual environment path the terminal command is: pipenv --venv

## 9. Py file creation for the project:
    a. Create a py file like, text.py in the root directory

## 10. Write codes for the project:
    a. First import client class from twilio rest api
       Code:
```python
            from twilio.rest import Client
```
       This Client class represents a client in twilio rest api.

    b. Now create a client object.
       Code:
```python
            Client()
```
       Here we need to pass my account sid, which is short for security indentifier as wel as an authentication token. We can find both these in twilio console page.

    c. Copy the SID and token from Twilio and store in variables on the py file.
       Codes:
```python
            account_sid = "284ur8249ufh9u24h82u4r0u90"
            auth_token = "92887239872830932-498-2"

            # Then create a client obejct
            client = Client(account_sid, auth_token)
```
    d. This client object has few interesting attributes. Here we use one of them messages
       Codes:
```python
            client.messages
```
        This message attribute has a method called .create()

    e. In this create method we need to pass 3 pieces of information:
       1. Phone number where to send sms
       2. Phone number from where to send sms, which is our twilio phone number
       3. The text body

       Codes:
```python
              client.messages.create(
                to = "phone_number"
                from_ = "twilio_phone_number"
                body = "A test message"
              )
```
    f. Then create a call object and store the result:
       Codes:
```python
              call = client.messages.create(
                to = "phone_number"
                from_ = "twilio_phone_number"
                body = "A test message"
              )
```
       This call object has attributes like date_created, date_sent, date_updated and so on. So this is the basic codes base for sending sms through twilio. 

       Final codes:
```python
                    from twilio.rest inport Client

                    account_sid = "314523452"
                    auth_token = "868060y0980y0070"

                    client = Client(account_sid, auth_token)

                    phone_number = "actual_phone_number"
                    twilio_phone_number = "actual_twilio_phone_number"

                    call = client.messages.create(
                      to = "phone_number"
                      from_ = "twilio_phone_number"
                      body = "The text messages content"
                    )

                    sms = call.date_created
                    print(f"The message has been sent on {sms}")
```
## 11. Secure the sensitive info:
    Now in the real project we must not hard coded the confidential information like account SID, authentication
    token, phone number etc. So we can either create a configaration file and keep those sensitive info there
    and put the confiq file in gitignore so this is not been shared to other or we can use environment variables
    which is keep the info in .bash_profile and the import them in the codes through os module. 

      i. Configaration file:
          a. Create a confiq file: Create a file named confiq.py in the source directory
          b. and store the sensitive information there in different variables
          Codes:
```python
                phone_number = "8547087518"
                twilio_phone_number = "39475270"
                account_sid = "314523452"
                auth_token = "868060y0980y0070"
```       
          c. Source codes: remove the sensitive info from the source code py file after creating the confiq file
          d. then import the config file in the py file as module and call the info by attribute
          Codes:
```python
                from twilio.rest inport Client
                import confiq

                client = Client(confiq.account_sid, confiq.auth_token)

                call = client.messages.create(
                  to = confiq.phone_number,
                  from_ = confiq.twilio_phone_number,
                  body = "The text messages content"
                )

                sms = call.date_sent
                print("The message has been sent on ", sms)
```
      ii. Environment variables:
          a. Store the sensitive information in .bash_profile in different variables:
              i. Go to terminal
              ii. Go to users: cd
              iii. Open bash_profile in nano: nano .bash_profile
              iv. Create variables and store the infomation in string
              v. Save the changes and exit
              vi. Then source the bash file to make the changes executable: source .bash_profile
              vii. Exit from the terminal and go back to vscode source codes.
              Codes:
```python
                        phone_number = "8547087518"
                        twilio_phone_number = "39475270"
                        account_sid = "314523452"
                        auth_token = "868060y0980y0070"
```
          b. Import the info from the bash profile in source code:
              i. import os module
              ii. os module has methods like .environ.get() it takes parameter as srt
              iii. So pass the variables on bash_profile in get method in string
              Codes:
```python
                        from twilio.rest inport Client
                        import confiq
                        import os

                        account_sid = os.environ.get("account_sid")
                        auth_token = os.environ.get("auth_token")
                        phone_number = os.environ.get("phone_number")
                        twilio_phone_number = os.environ.get("twilio_phone_number")

                        client = Client(account_sid, auth_token)

                        call = client.messages.create(
                          to = "phone_number"
                          from_ = "twilio_phone_number"
                          body = "The text messages content"
                        )

                        sms = call.date_sent
                        print("The message has been sent on ", sms)
```
## 12. Finally active the virtual environment and run the program and check your phone that should receive the text.