# SwissRoll_Generate
This is the project to generate some Swiss Roll datasets. </br>

When I wanted to search for some swiss-roll data sets with labels for machine learning on the Internet, I found that there were relatively few resources in this area, and it was difficult to find the appropriate source code to generate the corresponding data sets. Thus, I write the MatLab code to generate some kinds of swiss-roll. I hope this can help you.</br>   

# Swiss Rolls dataset
> The Swiss Rolls dataset is, itself, not very interesting. It is simply a standard "hello world" 3 dimensional data set which is universally known among academics working on various topics of dimensionality reduction techniques and algorithms.</br>
The following is the classic swiss roll data set (OriginClassicData.m). 
<div align=center><img width="500" height="300" src="https://github.com/TT159/SwissRoll_Generate/blob/86cc2cecdcb6f08ebb3f06e487e7a45e80e998b9/img_datasets/OriginSwiss.png"/></div> 

In my project, I focus on both 2 and 4 classes labeled data sets. I generate two different kinds of swiss roll data set. The one is derived from the classical swiss roll data set in which the data is generated uniformly (ClassicSwissRoll.m). 
<div align=center><img width="500" height="300" src="https://github.com/TT159/SwissRoll_Generate/blob/80e17dc7eb4ca82f419efd797f68fb2a6c34295d/img_datasets/ClassicData.jpg"/></div>  

The another one is the broken swiss roll. I constructed the broken swiss data sets in python code (BrokenSwissRoll.py) and plot it with MatLab (pythondata_plot.m).
<div align=center><img width="500" height="300" src="https://github.com/TT159/SwissRoll_Generate/blob/80e17dc7eb4ca82f419efd797f68fb2a6c34295d/img_datasets/BrokenData.jpg"/></div>  

