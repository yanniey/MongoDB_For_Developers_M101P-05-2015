use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "category":"$category"
	 },
	 avg_price:{$avg:"$price"}
     }
    }
])


// quiz
db.zips.aggregate([
	{$group:
		{
		_id:{
			"state":"$state"
		},
		avg_pop:{$avg:"pop"}
	}
	}	
])