# Code for Partial Cognate Detection

This instruction helps reproducing the steps of the partial cognate detection mentioned in the post "Computer-Assisted Comparison of Gelong and Hlai using Cross-Linguistic Data Formats".

In order to run the provided [script](https://github.com/digling/chingelong/scripts/partial_cognate_detection.py), you need to follow several steps:
- Please clone this repository first:
	```$ git clone https://github.com/digling/chingelong.git```
- It is suggested to create a fresh virtual environment.
- Several software is required to run this code (e.g. cldfbench, lingpy). You can install all requirements with the command: 
	```$ pip install -e ./```
- Now you can run the script:
	```$ python scripts/partial_cognate_detection.py```

Running this script will produce the expected tsv file called *alignments.tsv*.