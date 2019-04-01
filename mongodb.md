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
* https://www.tecmint.com/install-mongodb-on-ubuntu-18-04/
* By default MongoDB runs on port 27017, to allow access from everywhere you can use
* By default MongoDB comes with user authentication disabled, its therefore started without access control
* To enable access control on your MongoDB deployment to enforce authentication; requiring users to identify themselves every time they connect to the database server
* MongoDB uses the **Salted Challenge Response Authentication Mechanism (SCRAM)** authentication mechanism by default
* You need to create a user administrator (analogous to root user under MySQL/MariaDB) in the admin database. This user can administrate user and roles such as create users, grant or revoke roles from users, and create or modify customs roles
```bash
## Launch the mongo shell
mongo
## List all available databases
show dbs
## switch to the admin database, then create the root user
use admin 
db.createUser({user:"root", pwd:"=@!#@%$admin1", roles:[{role:"root", db:"admin"}]})
## exit the mongo shell
## edit the file and enabale authentication
sudo vim /lib/systemd/system/mongodb.service
## replcae with the following line
ExecStart=/usr/bin/mongod --auth --unixSocketPrefix=${SOCKETPATH} --config ${CONF} $DAEMON_OPTS
systemctl daemon-reload
sudo systemctl restart mongodb
mongo -u "root" -p --authenticationDatabase "admin"
##
## Create DB
use <dbName>
## drop DB
db.dropDatabase()
## Collections
show collections
## create collection
db.collection_name.insert({})
db.createCollection(name, options)
## drop collection
db.collection_name.drop()
## insert, pass array for bulk inserts
db.collection_name.insert()
## Verification
db.collection_name.find()
db.collection_name.find().forEach(printjson)
## OR
db.collection_name.find().pretty()
## Query
db.collection_name.find({"field_name":{$gt:criteria_value}}).pretty()
db.collection_name.find({"field_name":{$lt:criteria_value}}).pretty()
db.collection_name.find({"field_name":{$ne:criteria_value}}).pretty()
db.collection_name.find({"field_name":{$gte:criteria_value}}).pretty()
db.collection_name.find({"field_name":{$lte:criteria_value}}).pretty()
## Update
## By default the update method updates a single document.
## To enable update() method to update multiple documents you have to set “multi” parameter of this method to true as shown below.
db.collection_name.update(criteria, update_data)
##
## A very important point to note is that when you do not provide the _id field while using save() method, it calls insert() method and the passed document is inserted into the collection as a new document
db.collection_name.save( {_id:ObjectId(), new_document} )
##
## The remove() method is used for removing the documents from a collection in MongoDB.
db.collection_name.remove(delete_criteria)
db.collection_name.remove(delete_criteria, justOne)
##
## remove all documents
db.collection_name.remove({})
##
## Projection, used when we want to get the selected fields of the documents rather than all fields
db.collection_name.find({},{field_key:1 or 0})
##
## limits the number of documents returned in response to a particular query
db.collection_name.find().limit(number_of_documents)
## The `skip()`` method is used for skipping the given number of documents in the Query result.
##
## ort() method, you can sort the documents in ascending or descending order based on a particular field of document.
db.collecttion_name.find().sort({field_key:1 or -1})
##
## Create Index
## The value 1 is for ascending order and -1 is for descending order.
db.collection_name.createIndex({field_name: 1 or -1})
##
## getIndexes() method to find all the indexes created on a collections
db.collection_name.getIndexes()
##
## either drop a particular index or all the indexes
db.collection_name.dropIndex({index_name: 1})
##
## dropping the all indices
db.collection_name.dropIndex()
##
## load JSON data/file
mongoimport --db dbName --collection collectionName --file fileName.json --jsonArray
```
* https://docs.mongodb.com/manual/reference/method/load/


```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
  http://docs.mongodb.org/
Questions? Try the support group
  http://groups.google.com/group/mongodb-user
Server has startup warnings: 
2019-03-30T23:48:20.196+0530 I STORAGE  [initandlisten] 
2019-03-30T23:48:20.196+0530 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2019-03-30T23:48:20.196+0530 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2019-03-30T23:48:20.801+0530 I CONTROL  [initandlisten] 
2019-03-30T23:48:20.801+0530 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-03-30T23:48:20.801+0530 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2019-03-30T23:48:20.801+0530 I CONTROL  [initandlisten] 
```


## Client / UI
* https://stackabuse.com/spring-data-mongodb-tutorial/
* https://www.guru99.com/top-20-mongodb-tools.html
* http://www.codeandyou.com/2015/07/list-of-mongodb-gui-management-tools.html

http://www.phpmoadmin.com/
http://www.vork.us/
https://github.com/Studio3T/robomongo

http://leveldb.org/
https://github.com/google/leveldb
https://beginnersbook.com/2017/09/mongodb-create-database/


  

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
* **Default settings**
  -  By default MongoDB comes with user authentication disabled, its therefore started without access control. To launch the mongo shell, run the following command.



## Keywords
* sharding (partitioning data across various servers).
  - Data is partitioned into data chunks using the shard key, and these data chunks are evenly distributed across shards that resides across many physical servers. Also, new machines can be added to a running database.

