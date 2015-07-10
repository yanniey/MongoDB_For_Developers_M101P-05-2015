import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.photo
images = db.images
albums = db.albums

cursor = images.find({},{'_id':1})

for image in cursor:
	image_id = image['_id']
	image_in_alubms = albums.find_one({'images':image_id})

	if not image_in_alubms:
		images.remove({'_id':image_id})

print 'removed orphan images'
