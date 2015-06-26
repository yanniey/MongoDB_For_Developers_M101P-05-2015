use agg
db.products.aggregate([
    {$project:
     {
	 _id:0,
	 'maker': {$toLower:"$manufacturer"},
	 'details': {'category': "$category",
		     'price' : {"$multiply":["$price",10]}
		    },
	 'item':'$name'
     }
    }
])

// quiz

db.zips.aggregate([
    {$project:
        {_id:0,
        "city":{$toLower:"$city"},
        "pop":1,
        "state":1,
        "zip":"$_id"
        }
    }
])

