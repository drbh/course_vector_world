


## 1. Vectorizing and Comparing

In this folder we do all of the Machine Learning, and comparison. Reflecting on the repo - this code actually creates all of the value. The rest of the steps perform various transformations to make this data useful and manageable. 


#### Words as vectors

First we introduce the idea of converting words, sentences or other blobs of text into vectors. 

Vectors in our case are just a way to encode the information, in a way that we can use traditional math to interact with the text.

This means we can preserve a large amount of relational meaning while reducing open ended text to a manageable well understood space.

The picture below visualizes some of the main word to vector concept.

Since mapping words to vectors takes a huge amount of time and resources (hours of supercomputing and billions of inputs of real life raw text) we cannot effectly create a word to vector model ourselves.

However! Thanks to Google and many others leading the ML space - they provide a pre trained word to vector encoder we can use for our use case with some Python acrobatics. 

![](https://miro.medium.com/max/612/1*70iOJhTnYxj7Wc08TMbFaw.png)


#### Dot Product Similarity


Next we'll want to use these vectors for something useful, in our case we care about similarity of different classes. We can re- state this as, similarity of vectors. 

Since all of the vectors are fixed around the same point, we can use a simple but powerful distance measure - the dot product (inner product). This has two advantages, 1 we can easily compute this, using well tested and optimized functions, 2 it is accepted as a better distance metric then something like the cosine distance - which only takes into account the angle and not the magnitude of the vectors. 


below is a good representation of cosine similarity - with dot product we also use the length of the vector to weight similarity scores.
![](https://miro.medium.com/max/625/1*MgE-cLwdRUk-D2ErtfX4mA.png)

https://nlp.stanford.edu/IR-book/html/htmledition/dot-products-1.html

#### Similarity Matrix

Now we compute the inner product of all 14,066 vectors (all 512 in length) with itself. This returns us a huge 14,066 x 14,066 table (197,852,356 cell) table.

In our case our similarity matrix is also a correlation matrix since both inputs we used were identical.

This means that the values in the table correspond to the similarity of the two classes. 

![](http://logiciels.pierrecouprie.fr/telechargement/EANALYSIS/EAnalysisHelp/images/similarityMatrix-01.jpg)

![](https://sites.google.com/site/dchipsoft/high-level-analysis/analysis-of-variance-and-correlation-filtering/sample-correlation-matrix/image004.png?attredirects=0)


## 2. Reduction

Awesome! we can lookup values in this huge table, or we can do some pre processing to make this meaningful.

The very first step is removing all of the redundent values. Since `AxB == BxA` we know that we will have double of each score since we computed every class with every other class. For instance we will have `ENG 101 -> ENG 102 and ENG 102 -> ENG 101`. 

#### Get unique combos

All correlation tables have this issue and a simple and visual solution is to only use either the upper or lower diagonal half of the matrix. We must cut this diagonal along the `AxA` values. Where the `ENG 101 -> ENG 101` is computed. Looking on graph this is obvious since all of the values are 1's

We can actually use a very helpful math forumla to 1 compute the number of values and 2 reduce the matrix. This is called the Nth triangle and is simply `n * ( (n+1) / 2 )` in Python.

![](http://jwilson.coe.uga.edu/emt725/TriNos/DotSquare.jpg)

## 3. Expanding

Now we want to tie the existing data like the name of the course and the new reduced triangular matrix to a table. This included a few steps where we have to load large values into memory and concat values. Since Python was taking too long and was resouces hungry we write some parts of this expansion process in Rust. 

At the end of the day - we just want to make a table like
```
| source, | target, | score
-----------------------
| ENG 101,| ENG 102,| 0.89
```

And with Rust + Dask we can achieve this a reasonable time, on my MacBookPro. 

## 4. Extracting Useful Values

Great we now have a table with 98,933,211 rows and three columns. About 300 M cells. We know it has useful data but in this format we cant do much.

On a 1024 x 768 screen with 786,432 pixels, 98 M rows would mean about 126 relationships per pixel. 

We need to reduce the table to just the "useful" relationships. In this case we want to know the most similar. We dont care about the most dis-simiar (not at this point)

So what we really want to do is get a class, look at all the relationships, choose the top 10 (or n) most similar and forget the rest. 

This is exactly the formula, groupby a class, order by the score and limit the response to 10 values. A very SQL'ly sentence. 

Luckily Dask supports a very similar syntax and we can compute this expression. We now have a table of topn data! 

A list of the 10 most similar classes for every class - based on Google trained Machine Learning vector encoding and large scale similarity computation and reduction. Niceeee


## The future - step 5 

Lastly to make this useful to non programmers - we need a GUI. The next steps are to visualize the top relationships as a outward expanding graph. That way you get layer 1 and layer 2 relationships.

Stay tuned.  



#### Process Diagram

![diagram](https://raw.githubusercontent.com/drbh/course_vector_world/master/images/diagram.png)

# Notes
http://bl.ocks.org/d3noob/5141278