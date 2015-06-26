## M101P: MongoDB For Developers (Python) 05/2015

#### [Course Link](https://university.mongodb.com/courses/M101P/about)

#### Goal:
 
To build a blog with [MongoDB](https://www.mongodb.org/) and [Bottle](http://bottlepy.org/docs/dev/index.html) framework in Python(PyMongo)

---
+ Week 5
	Aggregate

Aggregation Pipeline:
$project,$match,$group,$sort,$skip,$limit,$unwind,$out

Aggregation Expressions:
$sum,$avg,$min,$max,$push,$addtoset,$first,$last


---
+ Week 4, finished 06/20/2015

	All about indexing. Using indexes, monitoring and understanding performance. Performance in sharded environments.

	Pluggable storage engines: **MMAP**(default) vs. **WiredTiger**

	Storage engines talk to drivers and influence how data is indexed and formated on the hard drive

	How to change default storage engine to Wired Tiger:

	```
	# kill current MongoDB session
	killall mongod
	# make a new directory
	mkdir WT
	# change the storage engine
	mongod --storageEngine wiredTiger
	```

	```
	db.foo.stats()
	```



---
+ Week 3, completed 6/11/15

	Schema Design - Patterns, case studies and tradeoffs. **$Pull**(remove) and **$Push**(insert)

Import Json file into MongoDB

```mongoimport -d school -c students < HW3.1students.json```


HW 3.2 

```
# XXX HW 3.2 Work Here to insert the post

self.posts.insert(post, j=True)
```

```
# XXX HW 3.2 Work here to get the posts

cursor = self.posts.find().sort([('date',-1)]).limit(num_posts)
```

```
# XXX Work here to retrieve the specified post

post = self.posts.find_one({'permalink':permalink})
```


Shell output:

```
(mongo)Anyis-MacBook-Pro:HW3.2and3.3 Anyi$ python validate.py
Welcome to the HW 3.2 and HW 3.3 validation tester
Trying to create a test user  itBHbTE
Found the test user  itBHbTE  in the users collection
User creation successful. 
Trying to login for test user  itBHbTE
User login successful.
Trying to submit a post with title  zIYJVuUakbtdSxzqPsVhzWTkAnmZWg
Submission of single post successful
Trying to submit a post with title  CPxFWALizvMzJpGqlGApzumGbSISCy
Submission of second post successful
Trying to grab the blog home page at url  http://localhost:8082/
Block index looks good.
Found blog post in posts collection
Tests Passed for HW 3.2. Your HW 3.2 validation code is 89jklfsjrlk209jfks2j2ek
Trying to submit a blog comment for post with title zIYJVuUakbtdSxzqPsVhzWTkAnmZWg
Can't add blog comments (so HW 3.3 not yet complete)
```

HW 3.3

```
self.posts.update({'permalink':permalink},{'$push':{'comments':comment}})
```

Shell output:

```
Successfully added blog comments
Tests Passed for HW 3.3. Your HW 3.3 validation code is jk1310vn2lkv0j2kf0jkfs
```

---

+ Week 2, completed 6/8/2015
	
  CRUD (Creating, Reading and Updating Data) - Mongo shell, query operators, update operators and a few commands. Create the `user` and `session` class for the blog app


	Use curl to download a json file and read it in python 

	``` 
	curl https://www.reddit.com/r/technology/.json > reddit.json
	cat reddit.json | python -m json.tool | more
	python read_reddit.py
	mongo
	# in mongo shell
	use reddit
	show collections
	db.stories.findOne()
	db.stroies.find().pretty()
	```

	2.1 JS file that creates a database in Mongo
	`mongo < 2.1school.js`

	2.4 Regex
	Mongo regex has an option of case insensitivity `'$options':'i'`

	2.5 Skip, limit, sort 
	order: sort first, then skip, then limit

	2.6 insert_one()

	2.7 insert_many()
	In `people.insert_many(people_to_insert,ordered=False)`, the `ordered=False` does not preserve the data when it's inserted into the database as in `people_to_insert = [andrew,richard]`

	`ordered = True` by default

	2.8 update_one() and update_many()

	2.9 replace_one()
	Cannot use `$set` in `replace_one()`

	2.11 delete_one() and delete_many()

	2.12 find_and_modify(), find_one_and_update()

	HW 2.1

	import json file into MongoDB

	```mongoimport -d students -c grades < grades.json```

---

+ Week 1, completed 5/28/2015:

  Introduction	Introduction & Overview - Overview, Design Goals, the Mongo Shell, JSON Intro, installing tools, overview of blog project. Bottle, Pymongo.



