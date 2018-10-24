# Machine Learning 1 Exercises

## Instructions
### Installation
Clone this repo onto your machine with the following command in your terminal:  
```
git clone https://gitlab.tubit.tu-berlin.de/dettmar/ML1.git
```  
or if you use ssl:  
```
git clone git@gitlab.tubit.tu-berlin.de:dettmar/ML1.git
```  

Note: the repo will be cloned into the folder `ML1/`, i.e. make sure it doesn't exist.

### Project file structure
In order to keep our project file structure relatively clean; once you're ready to upload your `.ipynb` file, copy paste it (not the whole folder) into the right exercise folder (`exercise01/`, `exercise02/`, etc), rename it as follows:
```sheet01_<theo or prog>_<your first name>.ipynb```

This way it'll be relatively easy to overview each others contributions without overwriting each others files.

### Branching
With the above file structure, branches won't be necessary. Let's keep it all in `master`. Remember to set the upstream with the first push as such:  
```
git push -u origin master
```

### Git Cheat sheet
1) Add all the files you've modified/added:  
```git add .```

2) Commit your changes with a message:  
```git commit -am "<describe your changes here>"```

3) Push your changes to gitlab:  
```git push```

### Jupyter notebook
It seems as if Gitlab can render `.ipynb` files somewhat accurately, however images and some other data seems to be omitted. To see the "real" results, it's best to run the file locally.
