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