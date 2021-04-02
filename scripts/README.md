# Code for Partial Cognate Detection and Phylogenetic Reconstruction

This instruction helps reproducing the steps of the partial cognate detection and phylogenetic reconstruction mentioned in the post "Computer-Assisted Comparison of Gelong and Hlai using Cross-Linguistic Data Formats".

In order to run the provided [script](https://github.com/digling/chingelong/blob/main/scripts/partial_cognate_detection.py), you need to follow several steps:
- Please clone this repository first:

	```$ git clone https://github.com/digling/chingelong.git```

- It is suggested to create a fresh virtual environment.
- Several software is required to run this code (e.g. cldfbench, lingpy). You can install all requirements with this command: 

	```$ pip install -e ./```

- Now you can run the script:

	```$ python scripts/partial_cognate_detection.py```

Running this script will produce a tsv file called *alignments.tsv* containing all cognate sets and alignments.

In a next step you can calculate the distance matrix:

```$ python scripts/phylogenetic_reconstruction.py```
  
With the help of the SplitsTree software you can compute and further manipulate the phylogenetic tree by uploading the distance matrix there.
