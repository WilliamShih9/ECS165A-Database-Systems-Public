from db import Database
from query import Query

db = Database()
grades_table = db.create_table('Grades', 5, 0)
query = Query(grades_table)

query.insert(1,2,3,4,5)
query.insert(2,3,4,5,6)
query.insert(3,4,5,6,7)
query.insert(4,4,5,6,7)
query.insert(5,10,20,30,40)


grades_table.index.create_index(1)
grades_table.index.create_index(2)
grades_table.index.create_index(3)
grades_table.index.create_index(4)

grades_table.index.indices

grades_table.index.indices[3]

res = query.select(4, 1, [1,1,1,1,1])

for i in res:
    print(i.columns)

res2 = query.select(5, 2, [1,1,1,1,1])

for i in res2:
    print(i.columns)

res3 = query.select(6, 3, [1,1,1,1,1])

for i in res3:
    print(i.columns)

res4 = query.select(7, 4, [1,1,1,1,1])

for i in res4:
    print(i.columns)

query.select(5, 0, [1,1,1,1,1])
query.update(5,20,30,40,50)
query.select(5, 0, [1,1,1,1,1])

for i in range(5):
    query.sum(0, 999, i, 0)

for i in range(5):
    query.delete(i)

for i in range(5):
    query.sum(0, 9999, i, 0)
  
grades_table.index.indices

query.insert(1,2,3,4,5)

grades_table.index.indices

query.insert(1000,3,5,6,7)

for i in range(5):
    grades_table.index.drop_index(i)

grades_table.index.indices


