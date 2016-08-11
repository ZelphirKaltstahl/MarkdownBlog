%title: Coursera Clustering & Retrieval Course finished!
%author: Zelphir
%date: 2016-08-11

Yesterday I completed the next course in the ML specialisation of University of Washington. It is a course about clustering and retrieval. I got the grade 93.1%, which is quite good I guess. I only improved one quiz before finishing the course, which brought me one more point in that quiz. The result of the quiz is thus really close to a result without improving any scores of quizzes. Now I got the certificate for that course, which I will use in applications for master theses projects.

Some pros and cons for that course are:

# Pros

* The content is important knowledge for ML.
* The programming assignments `Jupyter` notebooks.
* They use `Python` in the course, a good language for ML, because of all the packages available for it.
* The explanations of the theory in the course videos are good.
* The explanations on how to solve the programming assignments without `GraphLab Create` and with `SFrame` instead are great.

# Cons

* They're still using `Python 2.7.x`. It is the year 2016 people!
* They should mention, that the slides are different from the videos. Once I got stuck for days, because something was only explained in the slides, but not in the videos and I assumed the slides where the same as the ones used in the video lectures. Until that one quiz, I never had a problem answering the questions only watching the videos.
* They forced me to use `GraphLab Create` and `Python 2.7.x` at one point in the fifth week of the course. This is because `GraphLab Create` is not ready for `Python 3`. It seems a modern tool, but I simply do not understand, why they did not implement it in `Python 3` in the first place. Or who came up with the idea of using outdated `Python 2` for that matter ... Sooner or later they will have to update their code and it will be a lot of work, simply because they did not start with `Python 3`.

# Conclusion

I learned a lot from the course and I hope it will help me in the future, with a master project in ML.

# Note

Once can usually use `SFrame` to solve the tasks `GraphLab Create` solves, because it is, what `GraphLab Create` uses itself. `SFrame` is written by the same company and is a part of the `GraphLab Create` project, which they open sourced. However, I started working on the Titanic Kaggle competition, to try and see how accurate I could make predictions, using my current ML knowledge and when I did so, I realized, that I could not find a `SFrame` version for `Python 3.4.x`  or `Python 3.5.x` anywhere anymore. Seems it got taken offline and all the links are not working. I do not know, whether this is intentional, in order to promote the use of `GraphLab Create`, or just coincidence, that it happened, when it did. So I needed to use `Pandas` instead. Fortunately, the Titanic dataset is not that large and easily fits into memory of my machine.