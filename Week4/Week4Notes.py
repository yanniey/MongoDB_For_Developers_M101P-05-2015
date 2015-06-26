# create and see indexes

use school
db.students.createIndex({"class":1, "student_id:1"})
db.students.getIndexes();
db.students.dropIndexes({"student_id":1});

# Dot notation + multikey index = Create index for some 
db.students.createIndex({"scores.score":1})

# find score > 99:
db.students.explain().find({'scores.score':{'$gt':99}});

# find exam score > 99.8
db.students.explain().find({'scores':{$elemMatch:{type:'exam',score:{'$gt':99.8}}}});

# find how many exam scores > 99.8
db.students.explain().find({'scores':{$elemMatch:{type:'exam',score:{'$gt':99.8}}}}).count();


db.people.createIndex({'work_history.company':-1});

# create unique index
db.stuff.createIndex({'stuff':1},{unique:true});

# remove only 1 item
db.stuff.remove({'thing':'apple'},{justOne:true});

QUIZ: INDEX CREATION OPTION, UNIQUE
db.students.createIndex({student_id:1,class_id:1},{unique:true});

# add sparse index
db.employees.createIndex({"cell_phone":1},{unique:true,sparce:true});

# find by id in descending order
db.employees.find().sort({employee_id:-1});

# create index in the background (so that you are not blocked from reading and writing during the period)
db.students.createIndex({'scores.score':1},{background:true});

# use explain() to see what actually happens in the query
# winningPlan: COLLSCAN = scan the whole selection(slow), IXSCAN = scan by index, faster

# Verbosity: executionStats
db.example.explain('executionStats');
db.example.explain('allPlansExecution');

# Covered queries: search by index only, don't need to go through the documents

# How large is your index?
# index needs to be able to fit in working memory
db.students.stats()
db.students.totalIndexSize()
# wiredTiger (storage engier) indexes are a lot smaller than the traditional MMAP indexes

# Geospatial indexes
# find the nearest location
'location':[x,y]
find({location:{$near:[x,y]}}).limit(20)
db.places.find({location:{$near:[74,140]}}).limit(3);


# Geospatial spherical
db.places.createIndex({'location':'2dsphere'})



# in geonear.js:

db.places.find({
	location:{
		$near:{
			$geometry:{
				type:"Point",
				coordinates:[-122.166641,37.4278925], //these are the coordinates of hoover tower
				$maxDistance:2000
			}
		}
	}
}).pretty()

coordinates: [ <longitude> , <latitude> ]

# apply JS file to mongo

mongo < geonear.js


# another example:
# query a collection named "stores" to return the stores that are within 1,000,000 meters of the location latitude=39, longitude=-130
db.stores.find({ loc:{ $near:	{ $geometry: { type: "Point", coordinates: [-130, 39]}, $maxDistance:1000000 } } })


# Full text search (text indexes), in order to seach any word in the text instead of having to match the whole phrase

# first create a text index
db.sentences.createIndex({'words':'text'})

# then search with text index. regular search with find() won't work
db.sentences.find({$text:{$search:'dog'}})

# search a text, then sort the results with a certain field
db.sentences.find({$text:{$search:'dog tree'}},{score:{$meta:'textScore'}}).sort({score:{$meta:'textScore'}})

# index selectivity
# Selectivity is the primary factor that determines how efficiently an index can be used. Ideally, the index enables us to select only those records required to complete the result set, without the need to scan a substantially larger number of index keys (or documents) in order to complete the query. 
db.students.find({student_id:{$gt:500000},class_id:54}).sort({student_id:1}).hints({class_id}).explain("executionStats");

# order of indexes: equity field, then sort field, then range field


# logging slow queries:
# mongod automatically logs all queries that take > 100ms

# profiler
# level 0: off, level 1: log slow queries, level 2: log all queries
mongod -dbpath /usr/local/var/mongodb --profile 1 --slowms 2

db.system.profile().find().pretty()

# sort by time stamp
db.system.profile.find({millis:{$gt:1}}).sort({ts:1}).pretty()

# see which profiling level you are on
db.getProfilingLevel()
db.getProfilingStatus()
db.setProfilingLevel(1,4)

# Quiz: profiling
# Write the query to look in the system profile collection for all queries that took longer than one second, ordered by timestamp descending.

db.system.profile.find({millis:{$gt:1000}}).sort({ts:-1});

# Mongotop
# shows where mongo spends its time
mongotop 3

# Mongostat
# tell you what's going on in your system within 1 sec

# this is the wiredTiger version
mongo --port 27018
mongostat 


# sharding - using multiple servers
# sharding key


# Homework 4.3

#From the mongo shell:

```
use blog
db.posts.drop()
```

# From the mac or PC terminal window

mongoimport -d blog -c posts < posts.json
