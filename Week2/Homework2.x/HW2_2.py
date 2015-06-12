# Anyi Guo
# https://github.com/yanniey


import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the students database
db=connection.students
grades = db.grades

try:
    # list all homework scores according to student_id
    sorted_homework = grades.find( { "type": "homework" }).sort([("student_id", pymongo.ASCENDING),("score", pymongo.ASCENDING)])

except Exception as e:
    print "Unexpected error:", type(e), e

current_student = 0
for grade in sorted_homework:
    if grade['student_id'] == current_student:
        grades.remove(grade)
        current_student += 1


```
To verify that you have completed this task correctly, provide the identity of the student with the highest average in the class with following query that uses the aggregation framework. The answer will appear in the _id field of the resulting document.

db.grades.aggregate( { '$group' : { '_id' : '$student_id', 'average' : { $avg : '$score' } } }, { '$sort' : { 'average' : -1 } }, { '$limit' : 1 } )
```

# answer is 54



