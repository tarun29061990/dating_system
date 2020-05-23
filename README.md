# README #

### What is this repository for? ###

This is a dating system application.

### How do I get set up? ###

This project uses python3. You need to have 
python3.6 virtual environment installed on your machine.
To install python3.6 virtual environment follow this link:
 
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 

After installing the virtual environment, go to the project folder and type: 

    source <virtual_env_directory> activate
    
Run the application by typing:
    
    python src/main.py


### How to run tests
Test cases are located in tests folder.
In order to run the test cases simply type:

    python tests/runner.py
    
    
### Optimisations

For optimisation we can consider putting all the data to elastic search/ some graph Database. Querying will be fast and later we can run some machine learning algorithms for better recommendation.

### Project Structure and Logic

The whole code lies in the src folder.
1. main.py - This is the main starting file of the application. It register users, create a user graph and sort the edges based on parameters.

2. user.py - This is a user class which handles user registration.

3. constants.py - This is a constants class which handles all the constants.

### Who do I talk to? ###

* Tarun Chaudhary (http://curioustechie.in)
