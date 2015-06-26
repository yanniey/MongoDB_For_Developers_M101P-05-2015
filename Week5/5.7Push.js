use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$push:"$category"}
     }
    }
])



// quiz
db.zips.aggregate([
    {"$group":
        {"_id":"$state",
         "pop":{"$max":"$pop"}
     }}   
])