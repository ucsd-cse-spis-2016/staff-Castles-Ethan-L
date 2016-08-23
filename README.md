# Castle-starter

Castle Game starter repo

# HOW TO PLAY

Using [Method 1, with starter code](http://ucsd-cse-spis-2016.github.io/topics/github_create_repo/#method1), create a new private repo with these instructions:

* Create the repo under the `ucsd-cse-spis-2016` github organization
* Give it the name `spis16-Castles-First-L` where `First` is your first name, and `L` is the first letter of 
    your last name.
* Use this repo (the one you are looking at now, i.e. [https://github.com/ucsd-cse-spis-2016/Castle-starter](https://github.com/ucsd-cse-spis-2016/Castle-starter) as the starter code to import)

Then, every day, edit your castles according to the instructions below.

# EDIT `castles.json` to set your castles

For each remaining day of SPIS, you can play the Castle game by updating the file `castles.json` in this repo
with your entries for that day's competition.

The file `castles.json` should contain the following when you first copy this repo. 

```json

{ "First_L" : 
  { 
    "0823" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0824" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0825" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0826" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0827" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0828" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0829" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0830" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0831" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0901" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
   }
}
```

To enter each days competition, you'll edit the numbers in the list for that day so that they represent your 10 castles.

The numbers should sum to 100, and should all be non-negative.



For example, if Alex Triton were playing, and Alex wanted to be ready for the competition that ends on 08/23 at midnight, 
Alex might put this into the `castles.json` file in `https://github.com/ucsd-cse-spis-2016/spis16-Castles-Alex-T`:

```json

{ "Alex_T" : 
  { 
    "0823" :  11, 11, 11, 11, 22, 5, 6, 21, 1, 1 ],
    "0824" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0825" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0826" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0827" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0828" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0829" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0830" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0831" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    "0901" : [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
   }
}
```

# CHECKING YOUR NUMBERS FOR VALIDITY

To check your numbers, you can `git clone` the repo you create, and run the script `check_castles.py`

That script will check whether the castles.json file is in the correct format.

That script is also a nice example of loading json data into Python.

To check your numbers, you can run the script `check_castles.py`, either in IDLE,
or by typing `python check_castles.py` at the Unix command line (bash shell prompt).

The script will check the following:

* that your JSON is formatted properly
* that you changed the name from "First_L" to something else
* that the dates are the expected ones
* that your list of castles for each date has exactly 10 castles
* that your lists contain only non-negative integers
* that your lists sum to 100 or less

If the values all pass the test, then you'll be entered into the competition.

