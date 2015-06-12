#!/usr/bin/env python

import pymongo

# establish a connection to the database
connection = pymongo.MongoClient()

#get a handle to the school database
db=connection.school
students = db.students
def remove_lowest_homework():

	try:
		student_docs = students.find({})

	except:
		print "Unexpected error:", sys.exc_info()[0]

	for doc in student_docs:  
														
		doc["scores"].sort() 				    #	sort each document, ascending to highest score
		for hw in doc["scores"]: 				# look at every document for each student
			if hw['type'] == 'homework':	    # grab first doc which is 'homework'
				id_curr = doc["_id"]  			# set id of document
				students.update({"_id":id_curr},{"$pull":{'scores':hw}})
				break 

remove_lowest_homework()
