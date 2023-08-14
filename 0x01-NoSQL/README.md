# 0x01-NoSQL

This repository contains exercises and tasks for learning about NoSQL databases.

## Tasks

### 0. Install MongoDB
[Task 0](./0-install_mongodb)
- Install MongoDB on your machine and make sure it is running properly

### 1. Create a database
[Task 1](./1-create_database) 
- Using the Mongo shell, create a new database called `my_db`

### 2. Create a collection 
[Task 2](./2-create_collection)
- Using the Mongo shell, create a new collection called `movies` within the `my_db` database

### 3. Insert documents
[Task 3](./3-insert)
- Insert 3 new documents into the `movies` collection, with fields for `title` (string), `plot` (string), `year` (number), `rating` (number)

### 4. All documents
[Task 4](./4-all)
- Write a script that lists all documents in the `movies` collection 

### 5. All matches
[Task 5](./5-all)
- Write a script that lists all documents in `movies` with a rating >= 5

### 6. Count
[Task 6](./6-count)
- Write a script that displays the number of documents in the `movies` collection 

### 7. Delete
[Task 7](./7-delete) 
- Write a script that deletes the document with the title "Betty" from the `movies` collection

### 8. List all documents in Python
[Task 8](./8-all.py)
- Write a Python script that lists all documents in the `movies` collection 

### 9. Insert in Python
[Task 9](./9-insert_school.py)
- Write a Python script that inserts a new document into the `school` collection

### 10. Change school topics
[Task 10](./10-update_topics.py)
- Write a Python script that changes all topics of a school document based on the name

### 11. Where can I learn Python?
[Task 11](./11-schools_by_topic.py)
- Write a Python script that lists all documents with a specific topic in the `school` collection 

### 12. Log stats
[Task 12](./12-log_stats.py) 
- Write a Python script that provides some stats about Nginx logs stored in MongoDB

### 13. Regex filter
[Task 13](./13-count_by_range.py)
- Write a Python script that lists all documents with `ip` address starting in `[145, 155]` from the `nginx` collection

### 14. Top 10 of the most present IPs
[Task 14](./14-top_students.py)
- Write a Python script that prints the top 10 most present IPs in the `nginx` collection

### 15. Log stats - new version
[Task 15](./100-find)
- Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection

### 16. List all documents in Python
[Task 16](./101-students.py)
- Improve 14-top_students.py to sort students by number of occurrences


## Tasks To Complete

+ [x] 0. **List all databases**<br/>[0-list_databases](0-list_databases) contains a MongoDB script that lists all databases in MongoDB.

+ [x] 1. **Create a database**<br/>[1-use_or_create_database](1-use_or_create_database) contains a MongoDB script that creates or uses the database `my_db`.

+ [x] 2. **Insert document**<br/>[2-insert](2-insert) contains a MongoDB script that inserts a document in the collection `school`:
  + The document must have one attribute `name` with value “Holberton school”.
  + The database name will be passed as an option of `mongo` command.

+ [x] 3. **All documents**<br/>[3-all](3-all) contains a MongoDB script that lists all documents in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 4. **All matches**<br/>[4-match](4-match) contains a MongoDB script that lists all documents with `name="Holberton school"` in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 5. **Count**<br/>[5-count](5-count) contains a MongoDB script that displays the number of documents in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 6. **Update**<br/>[6-update](6-update) contains a MongoDB script that adds a new attribute to a document in the collection `school`:
  + The script should update only document with `name="Holberton school"` (all of them).
  + The update should add the attribute `address` with the value “972 Mission street”.
  + The database name will be passed as an option of `mongo` command.

+ [x] 7. **Delete by match**<br/>[7-delete](7-delete) contains a MongoDB script that deletes all documents with `name="Holberton school"` in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 8. **List all documents in Python**<br/>[8-all.py](8-all.py) contains a Python function that lists all documents in a collection:
  + Prototype: `def list_all(mongo_collection):`.
  + Return an empty list if no document in the collection.
  + mongo_collection will be the pymongo collection object.

+ [x] 9. **Insert a document in Python**<br/>[9-insert_school.py](9-insert_school.py) contains a Python function that inserts a new document in a collection based on `kwargs`:
  + Prototype: `def insert_school(mongo_collection, **kwargs):`.
  + `mongo_collection` will be the `pymongo` collection object.
  + Returns the new `_id`.

+ [x] 10. **Change school topics**<br/>[10-update_topics.py](10-update_topics.py) contains a Python function that changes all topics of a school document based on the name:
  + Prototype: `def update_topics(mongo_collection, name, topics):`.
  + `mongo_collection` will be the `pymongo` collection object.
  + `name` (string) will be the school name to update.
  + `topics` (list of strings) will be the list of topics approached in the school.

+ [x] 11. **Where can I learn Python?**<br/>[11-schools_by_topic.py](11-schools_by_topic.py) contains a Python function that returns the list of school having a specific topic:
  + Prototype: `def schools_by_topic(mongo_collection, topic):`.
  + `mongo_collection` will be the `pymongo` collection object.
  + `topic` (string) will be topic searched.

+ [x] 12. **Log stats**<br/>[12-log_stats.py](12-log_stats.py) contains a Python script that provides some stats about Nginx logs stored in MongoDB:
  + Database: `logs`.
  + Collection: `nginx`.
  + Display:
    + First line: `x logs` where `x` is the number of documents in this collection.
    + Second line: `Methods:`.
    + 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation at the start of each line).
    + One line with the number of documents with:
      + `method=GET`.
      + `path=/status`.
    + Example:
      ```log
      94778 logs
      Methods:
          method GET: 93842
          method POST: 229
          method PUT: 0
          method PATCH: 0
          method DELETE: 0
      47415 status check
      ```
  + You can use this dump as data sample: [dump.zip](dump.zip).

+ [x] 13. **Regex filter**<br/>[100-find](100-find) contains a MongoDB script that lists all documents with `name` starting by `Holberton` in the collection `school`:
  + The database name will be passed as an option of the `mongo` command.

+ [x] 14. **Top students**<br/>[101-students.py](101-students.py) contains a Python function that returns all students sorted by average score:
  + Prototype: `def top_students(mongo_collection):`.
    + `mongo_collection` will be the `pymongo` collection object.
  + The top must be in descending order of average score.
  + The average score must be part of each item returns with key = `averageScore`.
  + A sample document in the collection is shown below:
    ```json
    {
      "name": "Julia",
      "topics": [
        { "title": "Algo", "score": 10.5 },
        { "title": "C", "score": 10.2 },
        { "title": "Python", "score": 10.1 }
      ]
    }
    ```

+ [x] 15. **Log stats - new version**<br/>[102-log_stats.py](102-log_stats.py) improves [12-log_stats.py](12-log_stats.py) by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:
  + The top 10 IPs must be sorted.

