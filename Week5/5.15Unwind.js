use agg;
db.items.drop();
db.items.insert({_id:'nail', 'attributes':['hard', 'shiny', 'pointy', 'thin']});
db.items.insert({_id:'hammer', 'attributes':['heavy', 'black', 'blunt']});
db.items.insert({_id:'screwdriver', 'attributes':['long', 'black', 'flat']});
db.items.insert({_id:'rock', 'attributes':['heavy', 'rough', 'roundish']});
db.items.aggregate([{$unwind:"$attributes"}]);





use blog;
db.posts.aggregate([
    /* unwind by tags */
    {"$unwind":"$tags"},
    /* now group by tags, counting each tag */
    {"$group": 
     {"_id":"$tags",
      "count":{$sum:1}
     }
    },
    /* sort by popularity */
    {"$sort":{"count":-1}},
    /* show me the top 10 */
    {"$limit": 10},
    /* change the name of _id to be tag */
    {"$project":
     {_id:0,
      'tag':'$_id',
      'count' : 1
     }
    }
    ])