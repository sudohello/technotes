/*
Title: Maze Architecture & Components
Decription: maze architecture, components etc.
Author: Bhaskar Mangal
Date: 22 Feb 2017
Placing: 1
Tags: Linux, Maze, Architecture
*/

# Maze Architecture Components

[TOC]

## Needel in the Haystack - Search & Retrive GB's of Images and text files
* Problem Statement
- Huge number of photos across large number of directories representing Gigabytes of data, along with equally large number of text files associated with images in their respective directories. The text files contains GPS/IMU information, date and time, camera details.
- Need to search photos by time and location. Additional functionality like search photos by features that people remember is great add-on, such as bike in the picture they are looking for.

* Parts for the Solution
- First, we need robust search engine infrastructure.
- Second, the photos need to be cataloged and added to search engine’s index.
- Third, we need a simple way for users to search through tens of thousands of images by date & time, camera details, metadata, colors or any other feature we choose to add to the index.

### Search Engines
#### Elasticsearch
* Elasticsearch is a search engine based on Lucene
* It is developed in Java and is released as open source under the terms of the Apache License
* It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents
* It can be used to search all kinds of documents.
* It provides scalable search, has near real-time search, and supports multitenancy
* Search is distributed, which means that indices can be divided into shards and each shard can have zero or more replicas
* Elasticsearch uses Lucene and tries to make all its features available through the JSON and Java API
* It supports facetting and percolating, which can be useful for notifying if new documents match for registered queries
* Elasticsearch supports real-time GET requests, which makes it suitable as a NoSQL datastore, but it lacks distributed transactions

##### Requirements
* Logstash 5.2.x, Elasticsearch 5.2.x
  * Ubuntu 16.04
  * Oracle JVM 1.8u40+
* Kibana 5.2.x
  * Supported Browsers: IE11+	Firefox	Chrome	Safari (Mac)

##### Installation on CentOS-5
* References
  * [Install ES on CentOS](https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html)


##### Installation on Ubuntu
* References
  * [Install Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
  * [Install on Ubuntu](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#deb-repo)

++**NOTE**++
- If you install via a package manager (deb or apt-get), you should run via the service.
- If you want to run outside a service, you should install from an archive (tar) distribution.
- If installation is done via a package manager and you are trying to run as standalone, you will get the following error:
NoSuchFileException: /usr/share/elasticsearch/config. This problem arises if you install the package but attempt to run it outside the service.

(Following installation has been made using apt-get package manager)

1. Install the apt-transport-https package on Debian before proceeding:

```
sudo apt-get install apt-transport-https
```

2. Save the repository definition to /etc/apt/sources.list.d/elastic-5.x.list:
```
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
```

3. Update repository and install
```
sudo apt-get update && sudo apt-get install --assume-yes elasticsearch
```

4. Configure to run on start and stop
```
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service
```

5. Start and Stop elasticsearch
* Default elasticsearch node port is 9200

```
Start elasticsearch service:
sudo systemctl start elasticsearch.service

Test that your Elasticsearch node is running by sending an HTTP request to port 9200 on localhost
curl localhost:9200
curl http://localhost:9200
curl -XGET 'localhost:9200/?pretty'

If webserver is installed, check in browser, else install apache2 webserver:-
http://localhost:9200/

Stop elasticsearch service:
sudo systemctl stop elasticsearch.service

```

* SysV init vs systemdedit
How to start and stop Elasticsearch depends on whether your system uses SysV init or systemd (used by newer distributions)
```
ps -p 1
```

* Information will be written in the log files located in /var/log/elasticsearch/
* By default the Elasticsearch service doesn’t log information in the systemd journal
* To enable journalctl logging, the --quiet option must be removed from the ExecStart command line in the elasticsearch.service file.

6. logging
- When systemd logging is enabled, the logging information are available using the journalctl commands:
```
sudo journalctl -f
```
- To list journal entries for the elasticsearch service:
```
sudo journalctl --unit elasticsearch
```

7. Configurations & Settings
* References
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html

* Elasticsearch loads its configuration from the /etc/elasticsearch/elasticsearch.yml file by default.
* The Debian package also has a system configuration file (/etc/default/elasticsearch), which allows you to set the certain parameters.
* Elasticsearch has two configuration files:
  - elasticsearch.yml for configuring Elasticsearch
  - log4j2.properties for configuring Elasticsearch logging
* Debian and RPM packages set the config directory location to /etc/elasticsearch

* **NOTE**: Distributions that use systemd require that system resource limits be configured via systemd rather than via the /etc/sysconfig/elasticsearch file. [See Systemd configuration for more information](https://www.elastic.co/guide/en/elasticsearch/reference/current/setting-system-settings.html#systemd)

* Q) how do-i-find-where-elasticsearch-is-installing-my-plugins
  * References:
    - http://stackoverflow.com/questions/11954677/how-do-i-find-where-elasticsearch-is-installing-my-plugins

  ```
  To find your elasticsearch home directory & install plugin(s) follow these steps below. In the response of below command, locate home directory ( Look for Settings -> Path -> Home for value )

  curl "localhost:9200/_nodes/settings?pretty=true"
  ```

* Q) How to install plugins?
  * Goto Location (Example settings.path.home value: /usr/share/elasticsearch).
  * Install Plugin (Example plugin: [elasticsearch-head](http://mobz.github.io/elasticsearch-head/)

  ```
  bin/plugin -install mobz/elasticsearch-head
  ```

//export ES_HOME=""/usr/share/elasticsearch"

8. Install plugins
* x-pack for elasticsearch
  - It allows user management and access control for elasticsearch

```
sudo ./bin/elasticsearch-plugin install x-pack
```

- shards
- we are talking to an index, index is the virtual namespace
- shards are where actual data is stored on disks. It is the smallest unit of scale in elastic search. It's an search engine in its own right, move shards from node to node or copy shards to give you high availability. Put document into index and finguers out which shards it should belong.
When we search against the index, it looks for all of the shards in the index, runs the search on each of them, gets the results back

- results paginated data, in default size of 10, and total resultss

https://gist.github.com/ondrej-kvasnovsky/9363975
https://blog.pushapps.mobi/installing-elasticsearch-2-2-and-kibana-4-4-on-amazon-linux/



- Indexing
A. full-text/full-value search
=> Inverted Indexing
- separates words and each terms
- sort unique terms
- list docs containing terms

- searching
  - normalize terms - by lower casing, grouping with synonymns, soundex etc.
  - normalize query ( to search the normalize terms) - called Analysis (in elasticsearch) and is done by analyzer
  - Tokenization is done by tokenizer
  - normalization is done by token filters
  - every analyzer has to have a tokenizer and can have zero or more token filters
  - out of the box analyzer - standard analyzer
    - standard tokenizer
    - lowercase filter
    - stopwords filter
      - words with lower weight like - the, is, an etc.
  - english analyzer
    - standard tokenizer
    - lowercase filter
    - english stemmer
    - english stopwords

- Understanding Field Mapping is essential
- Core field types
  - Strings: string
  - Datetimes: date
  - Wholenumbers: byte, short, integer, long
  - Floats: float, double
  - Booleans: boolean
  - Objects: object
  - Others: multi_field (one field for multiple purposes), ip, geo_point, geo_shape
  - arrays: detects type based on the first value in array
- Dynamic detecion
- full text - index as analyzed
- exact value - index is not_analyzed
- not searchable - no
- updating Mapping
  - add new fields: PUT /myapp/tweet/_mapping -d
  - cannot change exitings fields: change the field, delete index, re-index
- Full body search - because we pass everything in the request query
GET /_search -d '
{
  "query":{
    "match_all": {}
  },
  "form": 0,
  "size": 10
}
'
- Query DSL - JSON structured rich flexible query language
- Examples: look for term search in the tweet field
{
  "match":{"tweet":"search"}
}
- Filers Vs queries
  - Filetrs for exact matching whereas queries for full tex search
  - Fileters gives yes/no, whereaas queries tells how well documents matches
  - fast, heavier
  - cacheable , not cachable
- Example: filter documents tweets only by marry
GET /_search -d '
{
  "query":{
    "filtered":{  
      "query":{
        "match":{"tweet":"search"} //"match_all":{}
      }
      "filter":{
        "term":{"nick":"@marry"}
        "range":{
          "date":{
            "gte":"2013-05-01",
            "lt":"2013-06-01"
          }
        }
      }  
    }
  }
  "sort":{"date":"desc"}
}
'
- facets:
GET /_all/tweet/_search -d '
{
  "facets":{
    "top_tweeters":{
      "terms":{
        "field":"nick"
      }
    },
    "tweets_by_month":{
      "date_histogram":{
        "field":"date",
        "interval":"month"
      }
    }
  }
}
'
- Autocomplete: search as while typing, problem is if it's not in the index, one cannot search  
  - N-grams == windown-on-a-word:
    - good for partial matching but not for Autocomplete
  - Edge N-grams == anchored N-grams
    - they are anchored to the begining of each word

- Edge N-gram token filter
{
  "filter":{
    "autocomplete:{
      "type": "edge_ngrams",
      "min_gram":1,
      "max_gram":20
      }"
  }
  //Name field analyzer
  "analyzer":{
    "name":{
      "type": "standard",
      "stopwords:[]
    },
    "name_autocomplete":{
      "type":"custom",
      "tokenizer":"standard",
      "filter":["lowercase","autocomplete"]
    }
  },
  //name field mapping
  "name":{
    "type":"multi_field",
    "fields":{
      "name":{
        "type":"string",
        "analyzer":"name"
      },
      "autocomplete":{
        "type":"srting",
        "index_analyzer":"name_autocomplete",
        "search_analyzer":"name"
      }
    }
  }
}

- Autocomplete query
{
  "match":{
    "name.autocomplete":"john smi"
  }
}
//Can do better
{
  "bool":{
    "must":[{},{}],
    "must_not":[{},{}],
    "should":[{},{}] //if they do match document gets some extra ppoints
  }
}

{
  "bool":{
    "must":{
      "match":{
        "name.autocomplete":"john smi"
      }
    },
    "should":{
      "match":{
        "name":"john smi"
      }
    }
  }
}

"filter":{
  "geo_distance":{
    "distance":"10km",
    "loc":{
      "lat":13.4,
      "lon": 52.5
    }
  }
}
// gaussing query compared to harsh barrier what if result is at 10.5km. Use gaussing curve in order of decreasing boost
"filter":{
  "gauss":{
    "loc":{
      "origin":{"lat":13.4,"lon": 52.5},
      "scale":"20km"
    }
  }
}

What you can do:-
- Full text search
- Big data
- facetting
- Geographical queries

- It's a document store using JSON datasctructure like MongoDB

- Try to use consistent field names across multiple docutypes
- it tries to guess the datatype of the data and does internal mapping

GET http://localhost:9200/test/persons/1 HTTP/1.1

https://www.youtube.com/watch?v=3xb1dHLg-Lk

https://www.opensemanticsearch.org/

echo "$JAVA" ${JAVA_OPTS} -cp "$FS_CLASSPATH" -jar "$FS_HOME/lib/fscrawler-2.3-SNAPSHOT.jar" "$@"

/usr/lib/jvm/java-8-openjdk-amd64/bin/java -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djava.util.logging.manager=org.apache.logging.log4j.jul.LogManager -cp /home/bhaskar/Documents/fscrawler-2.3-SNAPSHOT/lib/* -jar /home/bhaskar/Documents/fscrawler-2.3-SNAPSHOT/lib/fscrawler-2.3-SNAPSHOT.jar firstrun --loop 1 --restart




##### Kibana
* Kibana is an open source data visualization plugin for Elasticsearch
* It provides visualization capabilities on top of the content indexed on an Elasticsearch cluster
* Users can create bar, line and scatter plots, or pie charts and maps on top of large volumes of data
* The combination of Elasticsearch, Logstash, and Kibana (also known as ELK stack or Elastic stack) is available as products or service
* Logstash provides an input stream to Elastic for storage and search, and Kibana accesses the data for visualizations such as dashboards
* Default kibana node port is 5601 (refer Kibana Installation)

```
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list

sudo systemctl start kibana.service
sudo systemctl stop kibana.service

Kibana loads its configuration from the /etc/kibana/kibana.yml

These commands provide no feedback as to whether Kibana was started successfully or not. Instead, this information will be written in the log files located in /var/log/kibana/.

http://localhost:5601

bhaskar@maze:/usr/share/kibana$ sudo ./bin/kibana-plugin install x-pack
Attempting to transfer from x-pack
Attempting to transfer from https://artifacts.elastic.co/downloads/kibana-plugins/x-pack/x-pack-5.2.0.zip

```
##### x-pack plugin for elasticsearch, kibana and Logstash
* References
  - https://www.elastic.co/guide/en/x-pack/current/installing-xpack.html

- After installating x-pack, following default username/password is used
  * Default username : elastic
  * Default password: changeme

##### Create index
* https://www.elastic.co/guide/en/elasticsearch/reference/current/indices.html

###### Indices Existsedit
- Used to check if the index (indices) exists or not. For exampl

```
curl -XHEAD 'localhost:9200/twitter?pretty'
```

###### Index Settings
* [ All Index Settings ](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html)

```
curl -XPUT 'localhost:9200/twitter?pretty' -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "index" : {
            "number_of_shards" : 3,
            "number_of_replicas" : 2
        }
    }
}
'
```

OR

- You do not have to explicitly specify index section inside the settings section.
```
curl -XPUT 'localhost:9200/twitter?pretty' -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "number_of_shards" : 3,
        "number_of_replicas" : 2
    }
}
'

curl -XPUT 'localhost:9200/gazedata?pretty' -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "number_of_shards" : 2,
        "number_of_replicas" : 1
    }
}
'

curl -I 'localhost:9200/gazedata?pretty'

```
###### Index Mapping
- The create index API allows to provide a set of one or more mappings

```
curl -XPUT 'localhost:9200/test?pretty' -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "number_of_shards" : 1
    },
    "mappings" : {
        "type1" : {
            "properties" : {
                "field1" : { "type" : "text" }
            }
        }
    }
}
'
* [ES Filed Mapping - Datatypes](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html)
* [ES date type]()
  * https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-date-format.html#strict-date-time
  * http://stackoverflow.com/questions/17832217/store-date-format-in-elasticsearch

curl -XPUT 'localhost:9200/twitter?pretty' -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "tweet": {
      "properties": {
        "message": {
          "type": "text"
        }
      }
    }
  }
}
'
curl -XPUT 'localhost:9200/twitter/_mapping/user?pretty' -H 'Content-Type: application/json' -d'
{
  "properties": {
    "name": {
      "type": "text"
    }
  }
}
'
curl -XPUT 'localhost:9200/twitter/_mapping/tweet?pretty' -H 'Content-Type: application/json' -d'
{
  "properties": {
    "user_name": {
      "type": "text"
    }
  }
}
'

-Examples:
  - "format": "yyyy/MM/dd HH:mm:ss" //2013/07/24 00:00:00"
  - "format": "dd-MM-yyyy HH:mm:ss:SSS" //27-01-2017 17:03:03:901

curl -XPUT 'localhost:9200/gazedata?pretty' -H 'Content-Type: application/json' -d'
{
    "mappings" : {
        "files" : {
            "properties" : {
                "prefix" : {
                  "type" : "text"
                },
                "teamId" : {
                  "type" : "integer"
                },
                "fileDateAndTime" : {
                  "type" : "date",
                  "format": "dd-MM-yyyy HH:mm:ss:SSS"
                },
                "device" : {
                  "type" : "text"
                },
                "fileExt" : {
                  "type" : "text"
                },
                "fullFilePath" : {
                  "type" : "text"
                }
            }
        }
    }
}
'
##References
* https://www.elastic.co/guide/en/elasticsearch/reference/1.4/mapping-array-type.html
* https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html
//location string is "lat,lon" where as location array: [lon,lat] in latest version, GeoJson compliant

## orientation,body_acceleration,longitude,unix_time_seconds,microseconds,latitude,velocity,gpsDateAndTime
## Arrays are supported out of the box, no mapping required

curl -XPUT 'localhost:9200/gpsdata/_mapping/gps?pretty' -H 'Content-Type: application/json' -d'
{
  "properties" : {
    "prefix" : {
      "type" : "text"
    },
    "teamId" : {
      "type" : "integer"
    },
    "fileDateAndTime" : {
      "type" : "date",
      "format": "dd-MM-yyyy HH:mm:ss:SSS"
    },
    "device" : {
      "type" : "text"
    },
    "fileExt" : {
      "type" : "text"
    },
    "fullFilePath" : {
      "type" : "text"
    },
    "longitude" : {
      "type" : "float"
    },
    "unix_time_seconds" : {
      "type" : "integer"
    },
    "microseconds" : {
      "type" : "integer"
    },
    "latitude" : {
      "type" : "float"
    },
    "gps_date_and_time" : {
      "type" : "date",
      "format": "dd-MM-yyyy HH:mm:ss:SSS"
    },
    "gps_location": {
      "type": "geo_point"
    }
  }
}
'

curl -XPUT 'localhost:9200/gazedata/_mapping/files?pretty' -H 'Content-Type: application/json' -d'
{
  "properties" : {
      "prefix" : {
        "type" : "text"
      },
      "teamId" : {
        "type" : "integer"
      },
      "fileDateAndTime" : {
        "type" : "date",
        "format": "dd-MM-yyyy HH:mm:ss:SSS"
      },
      "device" : {
        "type" : "text"
      },
      "fileExt" : {
        "type" : "text"
      },
      "fullFilePath" : {
        "type" : "text"
      }
  }
}
'


# Search Query
curl -XPOST localhost:9200/gazedata/_search?pretty -d'{"query" : {"range" : {"fileDateAndTime" : {"gte" : "27-01-2017 16:49:06:128","lte" : "27-01-2017 16:49:07:148"}}}}'

# Get Mapping
curl -XGET 'localhost:9200/gazedata/_mapping/files?pretty'

curl -XPUT 'localhost:9200/gazedata/files/2?pretty' -H 'Content-Type: application/json' -d'
{
  "prefix": "GAZE",
  "teamId": 1,
  "fileDateAndTime": "27-01-2017 16:49:06:266",
  "device": "15398985",
  "fileExt": "jpg",
  "fullFilePath": "GAZE-270117-T1/16/49/06/15398985_266.jpg"
}
'
prefix,teamId,fileDateAndTime,device,fileExt,fullFilePath
GAZE,1,27-01-2017 16:49:06:498,15398985,jpg,GAZE-270117-T1/16/49/06/15398985_498.jpg
GAZE,1,27-01-2017 16:49:06:176,gps,json,GAZE-270117-T1/16/49/06/gps_176.json
GAZE,1,27-01-2017 16:49:06:126,gps,json,GAZE-270117-T1/16/49/06/gps_126.json
GAZE,1,27-01-2017 16:49:06:266,15398985,jpg,GAZE-270117-T1/16/49/06/15398985_266.jpg

curl -XGET 'http://localhost:9200/gazedata/files/1?pretty=true'

###### DELETE
```
curl -XDELETE 'localhost:9200/gazedata?pretty'
```

```
###### Types Exists
- Used to check if a type/types exists in an index/indices.
```
curl -XHEAD 'localhost:9200/twitter/_mapping/tweet?pretty'
curl -I 'localhost:9200/twitter/_mapping/tweet?pretty'
```

Note: while using -XHEAD
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the
Warning: way you want. Consider using -I/--head instead.

The HTTP status code indicates if the type exists or not. A 404 means it does not exist, and 200 means it does.

##### Logstash

##### Geting started
* Elasticsearch - localhost:9200
* Kibana - localhost:5601

#### Apache Solr

### References
* https://en.wikipedia.org/wiki/Elasticsearch
* https://en.wikipedia.org/wiki/Multitenancy
* https://en.wikipedia.org/wiki/Kibana
* https://www.elastic.co/
* [YAML](http://www.yaml.org/)
* [protecting-against-attacks-that-hold-your-data-for-ransom](https://www.elastic.co/blog/protecting-against-attacks-that-hold-your-data-for-ransom)
* [Elasticsearch - search by color](https://dpb587.me/blog/2014/04/24/color-searching-with-elasticsearch.html?utm_source=sandeepchivukula.com&utm_medium=blog&utm_campaign=photosearch-3)
* [Categorizing images with deep learning into Elasticsearch](https://www.elastic.co/blog/categorizing-images-with-deep-learning-into-elasticsearch)
* [Logging on systemd using journalctl](https://www.freedesktop.org/software/systemd/man/journalctl.html)

### Videos
#### Elasticsearch
* https://www.elastic.co/webinars/getting-started-elasticsearch?elektra=home&iesrc=ctr

### Tutorials
* [Photo Search Tut1](https://github.com/jettro/nodejs-photo-indexer)
* [Photo Search Tut2 Part-1](http://blog.sandeepchivukula.com/posts/2016/03/06/photo-search/)
* [Photo Search Tut2 Part-2](http://blog.sandeepchivukula.com/posts/2016/03/07/photo-search-2/)
* [Photo Search Tut2 Part-3](http://blog.sandeepchivukula.com/posts/2016/03/07/photo-search-3/)
* [Photo Search Tut2 Src](https://github.com/sandeep/photosearch/tree/master/indexer)

### Google search phrases
* List of information retrieval libraries
* Information extraction
* Multitenancy architectures V/s multi-instance architectures
* Transform HTTP requests into events

### Keywords
* Logstack
* Kibana
* ELK stack - The three products (Elasticsearch, Logstack, Kibana) are designed to be used as an integrated solution, referred to as the "ELK stack"
* near real-time search -
* multitenancy - It is a software architecture in which a single instance of software runs on a server and serves multiple tenants. A tenant is a group of users who share a common access with specific privileges to the software instance. With a multitenant architecture, a software application is designed to provide every tenant a dedicated share of the instance - including its data, configuration, user management, tenant individual functionality and non-functional properties
* shards
* facetting
* percolating
* CBIR - Content-based image retrieval (CBIR)

## Technologies

### Streaming data
* https://www.confluent.io/blog/stream-data-platform-1/
* https://www.elastic.co/guide/en/logstash/current/introduction.html

### Apache
* http://httpd.apache.org/docs/trunk/urlmapping.html

### Lucene
#### LIRE
- LIRE (Lucene Image REtrieval) is a plugin for Lucene to index and search images
- LIRE is a Java library that provides a simple way to retrieve images based on their colours and texture features

* http://mad4search.blogspot.in/2013/06/implementing-geospatial-search-using.html
* https://lingpipe-blog.com/2008/11/22/lucene-or-a-database-yes/
* http://www.lucenetutorial.com/techniques/lucene-php.html

## Extra Readings
* http://xavier.perseguers.ch/en/tutorials/typo3/articles/indexed-search-crawler.html
* https://en.wikipedia.org/wiki/List_of_CBIR_engines

## Linux Tools
### Exiftool - For Images
ExifTool is a platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files.

* References
  * http://www.sno.phy.queensu.ca/~phil/exiftool/

```
sudo apt-get install libimage-exiftool-perl
```

### wget - For Downloading files
```
If here are files with *.tar.bz2 extention at download.mobatek.net/sources, then we can download all those sources with "wget" such way:

lnx#> wget -r -l1 -A bz2 download.mobatek.net/sources
where -r --donwload recursively
-l1 one level of recurcivity
-A files extention

to download multiple files from the text file, store urls in new lines and run
wget -i <filename>
```

### tree
```
sudo apt-get install tree
```

wget https://repo1.maven.org/maven2/fr/pilato/elasticsearch/crawler/fscrawler/2.2/fscrawler-2.2.zip
https://www.youtube.com/watch?v=60UsHHsKyN4

## Python 2
https://learnpythonthehardway.org/book/ex0.html
https://docs.python.org/2/using/cmdline.html
https://github.com/datacamp/datacamp-light
http://sector7.xray.aps.anl.gov/~dohnarms/programming/python/python-2.7.2-pdf/
https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics?ex=1


### Study tips-and-tricks
Take your ex2.py file and review each line going backward. Start at the last line, and check each word in reverse against what you should have typed.
Read what you typed above out loud, including saying each character by its name. Did you find more mistakes? Fix them.

Why do I have to read code backward?
It's a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly. This catches errors and is a handy error-checking technique.

github.com
launchpad.net
gitorious.org
sourceforge.net

http://stackoverflow.com/questions/7588511/format-a-datetime-into-a-string-with-milliseconds

Install the following Python packages:

pip from http://pypi.python.org/pypi/pip
distribute from http://pypi.python.org/pypi/distribute
nose from http://pypi.python.org/pypi/nose/
virtualenv from http://pypi.python.org/pypi/virtualenv

https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers

```
sudo apt-get install python-pip
pip install -U pip setuptools

pip install --upgrade pip

#test module
pip install nose
```

https://pypi.python.org/pypi/csv2es

```
pip install csv2es
```

Successfully built csv2es pyelasticsearch retrying simplejson
Installing collected packages: click, urllib3, elasticsearch, joblib, simplejson, six, pyelasticsearch, retrying, csv2es
Exception:
Traceback (most recent call last):
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/commands/install.py", line 342, in run
    prefix=options.prefix_path,
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/req/req_set.py", line 784, in install
    **kwargs
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/req/req_install.py", line 851, in install
    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/req/req_install.py", line 1064, in move_wheel_files
    isolated=self.isolated,
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/wheel.py", line 345, in move_wheel_files
    clobber(source, lib_dir, True)
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/wheel.py", line 316, in clobber
    ensure_dir(destdir)
  File "/home/bhaskar/.local/lib/python2.7/site-packages/pip/utils/__init__.py", line 83, in ensure_dir
    os.makedirs(path)
  File "/usr/lib/python2.7/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/click-4.0.dist-info'
bhaskar@maze:/usr/share/elasticsearch$

### Filebeat

#### Install Filebeat
* https://www.elastic.co/guide/en/beats/libbeat/current/setup-repositories.html
* https://discuss.elastic.co/t/can-filebeat-parse-csv-file-and-send-the-data-in-fields-to-elastic-search-directly/68507/3

```
sudo apt-get install filebeat

sudo systemctl restart networking
sudo systemctl restart networking.service
```

#### Configure
/etc/filebeat/filebeat.yml


## VIM
http://vim.wikia.com/wiki/Converting_tabs_to_spaces
http://superuser.com/questions/384717/save-vim-settings-across-launches

```
sudo vim /etc/vim/vimrc.local
set expandtab
set tabstop=2
set nu
```

# Install LAMP Stack on Ubuntu
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04
* https://www.digitalocean.com/community/tutorials/how-to-move-an-apache-web-root-to-a-new-location-on-ubuntu-16-04

## PHP
### Install PHP on Ubuntu
```
sudo apt-get install php5.6 php7.0
```

## Apache2
### Install Apache2 on Ubuntu
* Check man apache2ctl for manual pages. Used to help admins.
```
sudo apt-get install apache2
sudo apache2ctl configtest
sudo systemctl status apache2
OR
sudo service --status-all
```
### Configurations
* The default Ubuntu document root is /var/www/html
* The configuration layout for an Apache2 web server installation on Ubuntu systems is as follows:
```
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
```
* apache2.conf is the main configuration file. It puts the pieces together by including all remaining configuration files when starting up the web server.
```
sudo vi /etc/apache2/apache2.conf

(then u can do ip for server at local machine eg: 10.4.71.231)
sudo service apache2 restart

ls /var/log/apache2/
gvim /etc/apache2/sites-available/000-default.conf
```
* ports.conf is always included from the main configuration file. It is used to determine the listening ports for incoming connections, and this file can be customized anytime.
* Configuration files in the mods-enabled/, conf-enabled/ and sites-enabled/ directories contain particular configuration snippets which manage modules, global configuration fragments, or virtual host configurations, respectively.
* They are activated by symlinking available configuration files from their respective available/ counterparts. These should be managed by using our helpers a2enmod, a2dismod, a2ensite, a2dissite, and a2enconf, a2disconf . See their respective man pages for detailed information.
* The binary is called apache2. Due to the use of environment variables, in the default configuration, apache2 needs to be started/stopped with /etc/init.d/apache2 or apache2ctl. Calling /usr/bin/apache2 directly will not work with the default configuration.

### Install PHP and MySQL modules for Apache2
```
sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql
```
#### Install PHP Modules
- To enhance the functionality of PHP, we can optionally install some additional modules.

* How to see the available options for PHP modules and libraries?
```
apt-cache search php- | less
```
* To get more information about what each module does:-
```
apt-cache show package_name
```

### Test and Check PHP Info

```
sudo sh -c 'echo "<?php phpinfo(); ?>" > /var/www/html/info.php'
```
* Following command will give you permission denied
```
sudo echo "<?php phpinfo() ?>" >  /var/www/html/info.php
> bash: /var/www/html/info.php: Permission denied
```
* Remove info.php after testing for security reasons
```
sudo rm /var/www/html/info.php
```

### Essential Modules
```
sudo a2enmod rewrite
sudo service apache2 restart
```

### Per-User configuration
* https://httpd.apache.org/docs/2.4/howto/public_html.html
* [Enable userdir module](http://ubuntuserverguide.com/2012/10/how-to-enable-and-configure-apache2-userdir-module-in-ubuntu-server-12-04.html)
* http://www.techytalk.info/enable-userdir-apache-module-ubuntu-debian-based-linux-distributions/

```
sudo a2enmod userdir
sudo service apache2 restart
mkdir ~/public_html && chmod 0755 ~/public_htm
```

- Check Apache version
- Configure Apache module userdir by editing userdir.conf file like this
```
apache2ctl -v
sudo vi /etc/apache2/mods-enabled/userdir.conf

<IfModule mod_userdir.c>
        UserDir public_html
        UserDir disabled root

        <Directory /home/*/public_html>
		AllowOverride All
		Options MultiViews Indexes SymLinksIfOwnerMatch
		<Limit GET POST OPTIONS>
			# Apache <= 2.2:
      #Order allow,deny
      #Allow from all

      # Apache >= 2.4:
      Require all granted
		</Limit>
		<LimitExcept GET POST OPTIONS>
			# Apache <= 2.2:
      #Order deny,allow
      #Deny from all

			# Apache >= 2.4:
			Require all denied
		</LimitExcept>
        </Directory>
</IfModule>
```
- This HTML files would be accessible using the http://example.com/~user/ syntax. Serving PHP files from user's public_html directoriy is disabled by default for security reasons.
- Enable PHP processing when using userdir, by commenting off the line "php_admin_flag engine Off" in /etc/apache2/mods-available/php7.0.conf file
```
sudo vi /etc/apache2/mods-available/php7.0.conf

# Running PHP scripts in user directories is disabled by default
#
# To re-enable PHP in user directories comment the following lines
# (from <IfModule ...> to </IfModule>.) Do NOT set it to On as it
# prevents .htaccess files from disabling it.
<IfModule mod_userdir.c>
     <Directory /home/*/public_html>
         #php_admin_flag engine Off
     </Directory>
</IfModule>
```

### Error Logs - Debugging PHP Applications
```
tail -f /var/log/apache2/error.log
```

### FAQs
* How to check which apache modules are enabled/installed?
* What modules do you have on disk. What are all the modules you can use?
* What modules is any specific instance configured to run?
* What's in a running apache?
  * http://superuser.com/questions/284898/how-to-check-which-apache-modules-are-enabled-installed

  - Enabled modules: ls /etc/apache2/mods-enabled/
  ```
  a2query -m
  ```
  - Available modules: ls /etc/apache2/mods-available/
  ```
  apache2ctl -M
  sudo apache2ctl -M | sort
  apache2ctl --help
  apachectl -t -D DUMP_MODULES
  ```

* Apache will first look for a file called index.html. We want to tell our web server to prefer PHP files, so we'll make Apache look for an index.php file first.
```
sudo vi /etc/apache2/mods-enabled/dir.conf
sudo systemctl restart apache2
sudo systemctl status apache2
```

To do this, type this command to open the dir.conf file in a text editor with root privileges:

## PHP Developement
*  PHP (recursive acronym for PHP: Hypertext Preprocessor)

### Install Composer

- Composer is a tool for dependency management in PHP. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
- Composer is not a package manager in the same sense as Yum or Apt are. Yes, it deals with "packages" or libraries, but it manages them on a per-project basis, installing them in a directory (e.g. vendor) inside your project.
- Two ways to install Composer. Locally as part of your project, or globally as a system wide executable
- I prefer to install globally

* Download the installer to the current directory
* Verify the installer SHA-384 which you can also cross-check with public keys
* Run the installer
* Remove the installer
* Put it in a directory that is part of your PATH, you can access it globally
* Now just run composer in order to run ```composer``` instead of ```php composer.phar```
```
sudo mv composer.phar /usr/local/bin/composer
composer -h
```
#### References:
* [Composer installation-linux-unix-osx](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx)
* [Composer download](https://getcomposer.org/download/)
* [Install Composer Programmatically](https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md)

### Install PHP Extensions
-These are some of the extension required by different web applications or in your custom Developement
```
sudo apt-get install php7.0-mbstring

* Following message is shows on successful installation:
Creating config file /etc/php/7.0/mods-available/mbstring.ini with new version
Processing triggers for libapache2-mod-php7.0 (7.0.13-0ubuntu0.16.04.1) ...
Processing triggers for php7.0-fpm (7.0.13-0ubuntu0.16.04.1) ...
```
#### References:
* [Install php extensions](http://askubuntu.com/questions/491629/how-to-install-php-mbstring-extension-in-ubuntu)
* [how-to-enable-mbstring-in-php](http://www.knowledgebase-script.com/kb/article/how-to-enable-mbstring-in-php-46.html)

#### Error Logs - Debugging PHP Applications
```
tail -f /var/log/apache2/error.log
```

### Webapplications on your server

### Grav
#### Troubleshooting
* [Installation, permission denied](https://www.vultr.com/docs/setup-grav-cms-on-ubuntu-14)
* [Check <?php echo exec('whoami');?>](https://github.com/getgrav/grav/issues/912)
* [mod_rewrite module](https://www.digitalocean.com/community/tutorials/how-to-set-up-mod_rewrite-for-apache-on-ubuntu-14-04)
* [Virtual Host Setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-16-04)
* [Permission issues](https://www.digitalocean.com/community/questions/should-i-enable-a-password-for-user-www-data)
* [Setting Permission for APache directory](http://askubuntu.com/questions/749697/how-do-i-give-myself-access-to-var-www-to-create-and-edit-files-and-folders-in)
* [Grav as LMS - Educational Technology](https://edtech.bccampus.ca/2017/01/05/grav-cms-edtech-demo/)
* [Setting www-data permissions](http://askubuntu.com/questions/46331/how-to-avoid-using-sudo-when-working-in-var-www)
```
# First, to create the folder, replacing 'mysite' with whatever name you wish to use: - create directory
mkdir -p /var/www/mysite && cd /var/www/mysite

# set permissions - Second, lets give you access, and the WebServer access. Apache2 runs as www-data by default
sudo chmod -R 775 /var/www/mysite
##sudo chown -R www-data:www-data /var/www/mysite
sudo chown -R $USER:www-data /var/www/mysite

# Thirdly, we need to make sure any files created in the folder are automatically given www-data as the group owner (so that it can actually read files it needs to read); we set the "SetGID" sticky bit for this.
sudo chmod -R g+s /var/www/mysite
##sudo chmod g+s /var/www/mysite

# We also may want to stop other users (except superuser and the web server) from accessing the folder too, in case there's passwords stored in the data that should not be exposed
(Grav needs write permission)
sudo chmod -R o-rwx /var/www/mysite

## Adding yourefy to www-data group
sudo gpasswd -a "$USER" www-data
Adding user bhaskar to group www-data

# Module required
##PHP GD (Image Manipulation Library) is not installed
##PHP Curl (Data Transfer Library) is not installed
##PHP XML Library is not installed
##PHP Zip extension is not installed
##PHP Mbstring (Multibyte String Library)
##PHP OpenSSL (Secure Sockets Library)

sudo apt-get install php7.0-gd php7.0-curl php7.0-xml php7.0-zip php7.0-mbstring

##mod_rewrite Apache module
sudo a2enmod rewrite
```
#### Admin, Login plugin
* Creating new user - command line; Inside grav installation directory
```
bin/plugin login newuser -u vidteq -p Vidteq123 -e bhaskar@vidteq.com -P s -N "Vidteq" -t "Content Editor"
```

#### Install Plugins/Packages

*  archives - The Archives plugin creates links for pages grouped by month/year
featherlight - Featherlight is a simple Grav plugin that adds lightbox functionality via the jQuery plugin Featherlight.js.
*  external_links - This plugin adds small icons to external and mailto links, informing users the link will take them to a new site or open their email client.
*  feed
*  git-sync
*  markdown-fontawesome
*  page-inject - Page Inject is a powerful plugin that lets you inject entire pages or page content into other pages using simple markdown syntax
*  pagination - Pagination is a very useful plugin to help navigate a large collection of pages, such as for a blog.
*  relatedpages - A highly sophisticated and configurable plugin that calculates related pages in relation to the current page.
*  simplesearch - Don't be fooled, the SimpleSearch plugin provides a fast and highly configurable way to search your content.
*  taxonomylist - With the TaxonomyList plugin you can easily create list of taxonomy items such as tags, categories, etc.
*  youtube - YouTube is a simple plugin that converts markdown links into responsive embeds.
* Editor Buttons - The Editor Buttons Plugin for Grav adds additional buttons to the Grav Admin Editor.
* GitHub - This plugin wraps the GitHub v3 API and uses the php-github-api library to add a nice GitHub touch to your Grav pages.
* Guestbook - Adds a Guestbook functionality to a page
* Highlight - This plugin provides code highlighting functionality via the Highlight.js jQuery plugin
* Login Plugin OAuth Addon
* Sitemap - Provide automatically generated XML sitemaps with this very useful, but simple to configure, Grav plugin.
* Snipcart - This plugin wraps the very good Snipcart application and let's you turn your Grav site into a shopping cart very easily.
* SweetCaptcha - Enables the ability to use sweetCaptcha form field in your forms

```
bin/gpm install archives
bin/gpm install external_links
bin/gpm install featherlight
bin/gpm install feed
bin/gpm install git-sync
bin/gpm install markdown-fontawesome
bin/gpm install page-inject
bin/gpm install pagination
bin/gpm install relatedpages
bin/gpm install simplesearch
bin/gpm install taxonomylist
bin/gpm install youtube
bin/gpm install login-oauth
```


- User Provided plugins
---------------------------
* aboutme - Simple plugin to show some information about yourself, with a nice picture, your name, your title/job and a description.You can also add links to your social network pages (Twitter, Facebook, GitHub, Google Plus, LinkedIn, Instagram).
* Breadcrumbs (not updated but can be used to create my own)
* CC-Linker - This plugin creates links/button/badge for cc-licences using shortcode syntax eg: ([CC by-sa])
* Comments - The Comments Plugin for Grav adds the ability to add comments to pages, and moderate them.
* CORS - Enables and allows to manage CORS (Cross-Origin Resource Sharing) in Grav
* Events - The Events plugin provides events for a Grav site using event frontmatter.
* facebook - Facebook is a plugin that embeds Facebook page content, album or events into your Grav website
* IPLocate
* Leaflet
* LoginLdap
* Mautic
* piwik


bin/gpm install aboutme


#### References
* [permissions](https://learn.getgrav.org/troubleshooting/permissions)
* [Markdown syntax for Grav](https://learn.getgrav.org/content/markdown)

### Keywords
* PHAR - PHP archive, which is an archive format for PHP which can be run on the command line, amongst other things

## Elastic Search Client Integrations using PHP
* [Elasticsearch PHP official plugin](https://github.com/elastic/elasticsearch-php)
* https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html

## Everyday Handy Linux commands

* Find something in all the files and print the line numbers and files and highlight the match
```
find . -iname '*' -type f -exec grep -inh --color='auto' 'userdir' {} \;
```

## System Troubleshooting

* Add and remove modules from Linux kernel
```
man modprobe
```
* Frequent wifi disconnection on Ubuntu 16.04
```
iwconfig
sudo iwconfig wlp7s0 power off

lspci -knn | grep Net -A2

sudo apt-get install dos2unix

```


### PostGresSQL
* https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
* https://askubuntu.com/questions/410244/a-command-to-list-all-users-and-how-to-add-delete-modify-users
* https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

* List All users
```
cut -d: -f1 /etc/passwd
awk -F':' '{ print $1}' /etc/passwd
```

#### Install PostgresSQL

* https://www.howtoforge.com/tutorial/ubuntu-postgresql-installation/

```
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib pgadmin3
```


## 3D City
* http://www.virtualcitysystems.de/en/products/virtualcitydatabase
* https://www.researchgate.net/publication/235635196_From_point_cloud_to_web_3D_through_CityGML
* https://justobjects.nl/3d-geospatial-open-standards-v0/
* https://cesiumjs.org/2015/08/10/Introducing-3D-Tiles/

Examples:
* https://www.gamesim.com/3d-geospatial-conform/#
* https://www.turbosquid.com/3d-models/3d-city-road-street-building/320842
* https://mapzen.com/projects/vector-tiles/
* itowns-project.org

### Vector Tiles
* https://mapzen.com/projects/vector-tiles/
* https://www.mapbox.com/vector-tiles/
* https://openmaptiles.org/styles/
* http://www.giscloud.com/blog/realtime-map-tile-rendering-benchmark-rasters-vs-vectors/
* https://www.bountysource.com/issues/28159922-best-way-to-display-fields-of-arrows-wind-fields-ocean-currents-in-terriajs


### Game Engines

http://forums.cgarchitect.com/79999-stingray-vs-unity-difference-similarities.html

https://www.cryengine.com/ 
The most powerful game development platform is now available to everyone. Full engine source code. All features. No royalties. No obligations. No license fee.

(
http://www.7cgi.com/

Main applications that we have huge competencies with are:- -> Autodesk 3ds Max -> Chaosgroup Vray
-> Pixologic Zbrash -> Marvelous Designer
-> Adobe Photoshop -> Adobe After Effects
-> Autodesk AutoCAD -> Google Sketchup
-> Adobe Illustrator
)

Stingray
Stingray's big advantage is that it supposedly works within the Autodesk workflow. The less software you have to jump though, the easier it is to make changes. However, it should be noted that even Autodesk screws their own workflows up, FBX linking in Max 2016 and the empty Revit link bug in 2016 I'm looking at you. So while it may work, you can count on Autodesk to figure out how to mess it up. The collaboration tools look pretty slick as well.

The big disadvantage, other than being under the Autodesk development umbrella, is that you have to pay for it. It's not necessarily cheap either, about $240 US per year.

https://www.unrealengine.com/
UE4:
Too many advantages to list. Huge advantage goes to their development, their track history, it's 100% free for architecure, and the community resources.

A negative to UE4 is that it can be resource intensive to run and install onto 3rd party systems. You generally need newer hardware to run UE4 apps.

Unity:
Again, quite a few advantages. A huge plus is that Unity will run on anything and has very low system requirements. Of course, the requirements increase as you push the quality, but base Unity scenes will run on even older hardware and mobile devices. Unity also has better (for the moment) web deployment tools. Unity excels in the mobile side due to the mentioned low requirements to run. Their GDC showreel and Adam short film is highly impressive and is starting to give UE4 a run for their money.

A negative is that Unity can be hard to start initially. It is very bare bones and you are left to yourself to write a lot of the initial code. The good news is that on the Unity store there is a ton of pre-made resources and the community is incredibly helpful. For the pro version of Unity, you have to pay for it. The standard edition, however, is totally free. You have to do some research on which one is best for you. Unity does have an AEC side that you can contact, maybe they do deals?


https://aws.amazon.com/lumberyard/




Interior viz, exetrior viz, large scale, small scale, just a movie? a playable game? do you need interactivity? do you know how to code? do you need it photoreal? 100% dynamic lighting or baked? Of course different apps can be better in certain situations but I still think ue4 is one of the most well-rounded engine!


It's always a good idea to stay informed about multiple softwares and technologies :-)

Now, if you want to start learning I think you are better off with Ue4 or Unity because they have the biggest communities and the most learning ressources available right now! No matter what engine you use, in the end your skills will be transferable between each engines. You should download both ue4 and unity, play with them a little bit and see which one feels the best! But trying to learn with Stingray or Cry/Lumberyard will be much harder I think. 

I never checked the Unity asset store but in ue4 marketplace you have a ton of free scenes/games to download and reverse-engineer. I even learned stuff from the unreal tournament editor and it's free maps!!!

And for your furniture, any 3d modeling package will do. Not sure what are the needs right now tho, if there are any hehe! Just make sure you master uvmapping/uv unwrapping because we always want the most realistic stuff even if it's for a game engine!
Good luck!

### 3D City Modeling + GIS
http://vterrain.org/
https://alternativeto.net/software/cityengine/?license=opensource
https://spatiametrics.wordpress.com/2013/04/16/building-a-3d-world-with-openstreetmap-cityengine-unity-3d/

### Blender on Ubuntu
* http://ubuntuhandbook.org/index.php/2016/10/install-blender-2-78-in-ubuntu-16-04-14-04/

A revival of Irie Shinsuke's PPA: Blender is compiled with all bells and whistles (OSL, OpenCollada, OpenVDB, OSD, jemalloc & precompiled CUDA kernels) and adapted to Ubuntu (python, ffmpeg, ilmbase, openEXR, Ubuntu packages are used directly to avoid redundancy).

If you find this PPA useful, you can offer me a coffee or a beer at

  https://goo.gl/lD5eNE

Yes, in 3 years, 20 persons/companies did it: $(5+10+5+5+5+5+10+5+10+3+5+ 4+10+5+10+10+10)+€(50.79+3.64+13.37). I enjoyed the drinks! (updated March 17, 2017).

Two (conflicting) versions of blender are provided:

- blender is the last active tag of blender git repository, with only releases or releases candidate, focusing on stability. The blender version is followed by the last commit number and hash. The contrib addons are always included.

- blender-edge lives on the edge: is the last commit of the master branch of blender git repository. The first number is the number of commits since the beginning of blender git, followed by the commit hash.

For CUDA to work, add the blender user(s) to the 'video' group through:

  sudo adduser <user> video

It is also useful to install the nvidia-modprobe package (which is not a dependency because it depends on your hardware).

This PPA is usually updated every Friday (except while I'm on vacations). While I try to automatize things heavily, there are often changes in Blender (or Ubuntu) that require non negligible manual intervention. If you see issues, please contact me with suggestions (but do not expect an instantaneous reaction :-)
 More info: https://launchpad.net/~thomas-schiex/+archive/ubuntu/blender
Press [ENTER] to continue or ctrl-c to cancel adding it
