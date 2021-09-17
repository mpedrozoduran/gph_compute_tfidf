# gph_compute_tfidf
TF-IDF Computation API

#Exercise

**1.** Build an API using Python that takes a URL and returns the terms with the highest TF-IDF on the page. To compute IDF use the articles in this dataset: https://www.kaggle.com/snapcrack/all-the-news. The url parameters are: url and limit Example call:

`/tfidf?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTf-idf&limit=10`
<br>
* To run the project using a docker image, open a terminal window and paste the following commands:
<br>
`docker pull mpedrozoduran/gph_compute_tfidf:1.0.0` 
<br>
`docker run -it -p 5000:5000 mpedrozoduran/gph_compute_tfidf:1.0.0`
* Or to compile the project:
`virtualenv -p python3 venv`
`pip install -r requirements.txt`
<br>
* Then open a browser window and paste the following URL: 
`http://localhost:5000/api/docs` 
<br>
Here you will find a swagger interface to test the project.
<br>

* The basics for TF-IDF computation were taken from: <br>
- [https://www.kaggle.com/snapcrack/all-the-news](https://www.kaggle.com/snapcrack/all-the-news) 
- [https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a](https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a)
<br>

**2.** No need to actually implement this, just explain how you would do it. How would you design a system that, in addition to computing TF-IDF counts for the provided URL upon request, updates the IDF statistics whenever TF-IDF for a previously unseen URL is requested? How would you deploy this on AWS or GCP?

The following image shows the propposed Application Architecture and a Stack Diagram that describes the interaction between the
technologies to use.

![Diagram](https://i.ibb.co/Dpzpr5n/architecture.png "Architecture Diagram")
