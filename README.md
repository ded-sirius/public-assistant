#Public Assistant
**featuring Amazon Alexa**

A speech-controlled app for public kiosks that gives directions to nearby facilities and businesses.

To use the app, first follow the instructions under *Execution*, followed by those under *Creating the Alexa Skill*.

##Execution

* Create a copy of `config.example.py` as `config.py` and insert your Google API
* Execute main.py
* In a separate terminal, execute ngrok from the root directory using
```
bin/ngrok http 5000
```

##Creating the Alexa Skill
In the Amazon Developer's Console: 

* Under Skill Information, set the Invocation Name to "dead serious"
* Under Interaction Model, copy the contents of intents.json into Intent Schema
* Create a new custom slot type called LIST\_OF\_LOCATIONS and copy the contents of locations.txt into it
* Copy the contents of samples.txt into Sample Utterances
* Under Configuration, select HTTPS and copy the final output of ngrok into the text bar under the geographical regions. Example: 
```
https://22183bb0.ngrok.io
```
* Under SSL Certificate, select "My development endpoint is a sub-domain..."

##Test

Example input:

1.``
Alexa, start Dead Serious
``

2.``
How do I get from Sunset Park to a homeless shelter?
``
