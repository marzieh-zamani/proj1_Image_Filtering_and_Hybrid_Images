# ENSE 885AY project 1: [Image Filtering and Hybrid Images]


# Project Review
- Project subject: Image Filtering and Hybrid Images

- Project objectives: Writing an image filtering function and using it to create hybrid images.


# Main files to check
- Project report: I have briefly introduced the objectives of the project, reviewed the image processing methods, explained the main functions, described experiments and discussed the results.

- Notebook: High level code where inputs are given, main functions are called, results are displayed and saved.

- Student code: Image processing functions are defined.


# Setup by Dr. Kin-Choong Yow
- Install <a href="https://conda.io/miniconda.html">Miniconda</a>. It doesn't matter whether you use 2.7 or 3.6 because we will create our own environment anyways.
- Create a conda environment, using the appropriate command. On Windows, open the installed "Conda prompt" to run this command. On MacOS and Linux, you can just use a terminal window to run the command. Modify the command based on your OS ('linux', 'mac', or 'win'): `conda env create -f environment_<OS>.yml`
- This should create an environment named `ense885ay`. Activate it using the following Windows command: `activate ense885ay` or the following MacOS / Linux command: `source activate ense885ay`.
- Run the notebook using: `jupyter notebook ./code_dir/proj1.ipynb`
- Generate the submission once you're finished using `python zip_submission.py`


# Credits and References
This project has been developed based on the project template and high-level code provided by Dr. Kin-Choong Yow, my instructor for the course “ENSE 885AY: Application of Deep Learning in Computer Vision”.

This course is based on Georgia Tech’s CS 6476 Computer Vision course instructed by James Hays.

- Dr. Kin-Choong Yow page: 
http://uregina.ca/~kyy349/

- “CS 6476 Computer Vision” page:
https://www.cc.gatech.edu/~hays/compvision/

- Project source page at “CS 6476 Computer Vision”:
https://www.cc.gatech.edu/~hays/compvision/proj1/

- James Hays pages:
https://www.cc.gatech.edu/~hays/
https://github.com/James-Hays?tab=repositories


# My contribution
The following files contain the code written by me:

- code/student_code.py >> my_imfilter() function
- code/student_code.py >> create_hybrid_image() function
- proj1_5RegularImages.ipynb >> Tuned Cut-off Frequency
- proj1_CutoffEffect.ipynb >> Effect of Cut-off Frequency on Hybrid Images

______________
Marzieh Zamani