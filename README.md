# cts-surveyor-pyclient
## Python client for facial detection, age / gender classification and people detection / counting

This client uses the CTS Surveyor server that can run locally and allow you to classify people by age and gender, as well as track people that are moving in front of the camera. You will need to download CTS surveyor from the following link to perform people detection and classification:

http://caerustech-solutions.com/demo/surveyor.zip

The current version can only run on Windows (for now)

Here is how to use the solution:

1. Unzip the surveyor.zip
2. Make sure you have Python 3.5 or later
3. pip install websocket-client
4. pip install requests
5. Clone this repo
6. Start surveyor.exe from where you unpackaged surveyor.zip
7. Run "python test_notifier.py" to receive notification events regarding detected people
8. Run "python test_client.py" to invoke API's (such as to enable/disable detection, as well as to retrieve statistics)
9. Enjoy detecting/classifiying faces and people!


Dependencies:

pip install websocket_client

pip install requests