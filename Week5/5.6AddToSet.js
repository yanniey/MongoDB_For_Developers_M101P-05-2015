use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$addToSet:"$category"}
     }
    }
])


// quiz
db.zips.aggregate([
    {"$group":
        {"_id":"$city",
        "postal_codes":{"$addToSet":"$_id"}
    }
    }
])