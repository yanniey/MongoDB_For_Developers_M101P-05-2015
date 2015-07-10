Import the dataset:

```
ongorestore --collection messages --db enron messages.bson
```

Quiz 1:

```
db.messages.find({"headers.From":"andrew.fastow@enron.com","headers.To":["jeff.skilling@enron.com"]}).count()
```

Quiz 2:

```
db.messages.aggregate([{$unwind: "$headers.To"}, {$group: {"_id": {"From": "$headers.From", "To": "$headers.To"}, "Emails": {$sum: 1}}}, {$sort: {"Emails": -1}}, {$limit: 3}])
```

Quiz 3:

```
db.messages.update(
	{"headers.Message-ID":"<8147308.1075851042335.JavaMail.evans@thyme>"},
	{$push:{ "headers.To":"mrpotatohead@10gen.com"}}
)
```

Quiz 4:

note: make sure that you run `mongod` and `python2 blog.py` at the backgroudn when using `python2 validate.py`



```
Welcome to the M101 Final Exam, Question 4 Validation Checker
Trying to grab the blog home page at url and find the first post. http://localhost:8082/
Found a post url:  /post/mxwnnnqaflufnqwlekfd
Trying to grab the number of likes for url  http://localhost:8082/post/mxwnnnqaflufnqwlekfd
Likes value  1
Clicking on Like link for post:  /post/mxwnnnqaflufnqwlekfd
Trying to grab the number of likes for url  http://localhost:8082/post/mxwnnnqaflufnqwlekfd
Likes value  2
Tests Passed for Final 4. Your validation code is 3f837hhg673ghd93hgf8
```

Quiz 5:

```
a_1_b_1_c_-1
c_1
a_1_c_1
a_1_b_1
```

Quiz 6:
adding an index reduces the writing speed because it requires maintainence 

Quiz 7:

```
mongoimport --db photo albums.json
mongoimport --db photo images.json
```

see `Final7.py` in `Final7` folder, and then:

```
db.images.find({tags:'kittens'}).count()
```

Quiz 8:
Not sure about this one, I chose `Yes, always.`

Quiz 9:
best sharding key is `patient_id`

Quiz 10:

```
The query avoided sorting the documents because it was able to use an index's ordering.
The query scanned every document in the collection.
```
