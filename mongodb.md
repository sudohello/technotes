mongodb
---
Title: MongoDB
Decription: MongoDB
Author: Bhaskar Mangal
Date: 30th-Mar-2019
Last updated: 30th-Mar-2019
Tags: MongoDB
---

**Table of Contents**
* TOC
{:toc}



## MongoDB & Python
* MongoDB is: cross-platform, open-source document-oriented database that works on the concept of collections and documents. MongoDB offers high speed, high availability, and high scalability.
* The term ‘NoSQL’ means ‘non-relational’.
* It means that MongoDB isn’t based on the table-like relational database structure but provides an altogether different mechanism for storage and retrieval of data. This format of storage is called BSON ( similar to JSON format)
* Relational Database Management System(RDBMS) is not the correct choice when it comes to handling big data by the virtue of their design since they are not horizontally scalable. 

| RDBMS       | MongoDB             |
|:------------|:--------------------|
| Table       | Collection          |
| Tuple (ROW) | Document (JSON)     |
| Column      | Field               |
| Index       | Index               |
| Join        | Embedding & Linking |
| Partition   | Shard               |


* MongoDB provides a default ‘_id’ (if not provided explicitly) which is a 12 byte hexadecimal number which assures the uniqueness of every document. It is similar to the Primary key in RDBMS.



### [mongodb-an-introduction](https://www.geeksforgeeks.org/mongodb-an-introduction/)
* [mongodb-and-python](https://www.geeksforgeeks.org/mongodb-and-python/)


## FAQ's MongoDB
* **Why to opt for MongoDB?**
  - hierarchical data structure
  - associate arrays like Dictionaries in Python.
  - Built-in Python drivers to connect python-application with Database. Example- `PyMongo`
* **Where do we use MongoDB?**
  * MongoDB is preferred over RDBMS in the following scenarios:
    - Big Data
      + has built in solution for partitioning and sharding your database
    - Unstable Schema
      + MongoDB is schema-less. Adding a new field, does not effect old documents and will be very easy
    - Distributed Data
      + recovery of data is instant and safe even if there is a hardware failure
* **Who’s using MongoDB?**
  - EA, Cisco, Shutterfly, Adobe, Ericsson, Craigslist, eBay, and Foursquare.


## Keywords
* sharding (partitioning data across various servers).
  - Data is partitioned into data chunks using the shard key, and these data chunks are evenly distributed across shards that resides across many physical servers. Also, new machines can be added to a running database.

