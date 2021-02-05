from db import Database
from query import Query
from time import process_time
from random import choice, randrange, seed
import csv

def repeat(grades_table, query, keys):
    seed(3562901)
    insert_time_0 = process_time()
    for i in range(0, 10000):
        query.insert(906659671 + i, randrange(0, 100), randrange(0, 100), randrange(0, 100), randrange(0, 100))
        keys.append(906659671 + i)
    insert_time_1 = process_time()
    insert_time = insert_time_1 - insert_time_0
    # Measuring update Performance
    update_cols = [
        [randrange(0, 100), None, None, None, None],
        [None, randrange(0, 100), None, None, None],
        [None, None, randrange(0, 100), None, None],
        [None, None, None, randrange(0, 100), None],
        [None, None, None, None, randrange(0, 100)],
    ]
    update_time_0 = process_time()
    for i in range(0, 10000):
        query.update(choice(keys), *(choice(update_cols)))
    update_time_1 = process_time()
    update_time = update_time_1 - update_time_0
    # Measuring Select Performance
    select_time_0 = process_time()
    for i in range(0, 10000):
        query.select(choice(keys), 0, [1, 1, 1, 1, 1])
    select_time_1 = process_time()
    select_time =  select_time_1 - select_time_0
    delete_time_0 = process_time() 
    for i in range(0, 10000):
        query.delete(906659671 + i)
    # Query Time

    
    delete_time_1 = process_time()
    delete_time = delete_time_1 - delete_time_0
    result = [insert_time, update_time, select_time, delete_time]
    print(result)
    return result

# Student Id and 4 grades
db = Database()
grades_table = db.create_table('Grades', 5, 0)
query = Query(grades_table)
keys = []

result = []



with open('performance5v0.csv','w') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):
        db = Database()
        grades_table = db.create_table('Grades', 5, 0, [1,2,3,4,5])
        query = Query(grades_table)
        keys = []
        writer.writerow(repeat(grades_table, query, keys))

with open('performance2v0.csv','a') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):
        db = Database()
        grades_table = db.create_table('Grades', 5, 0, [1])
        query = Query(grades_table)
        keys = []
        writer.writerow(repeat(grades_table, query, keys))


db = Database()
grades_table = db.create_table('Grades', 5, 0, [1, 2])
query = Query(grades_table)
keys = []

with open('performance3v0.csv','a') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):
        print(i)
        db = Database()
        grades_table = db.create_table('Grades', 5, 0, [1, 2])
        query = Query(grades_table)
        keys = []
        writer.writerow(repeat(grades_table, query, keys))



db = Database()
grades_table = db.create_table('Grades', 5, 0, [1, 2, 3])
query = Query(grades_table)
keys = []

with open('performance4v0.csv','a') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):
        db = Database()
        grades_table = db.create_table('Grades', 5, 0, [1, 2, 3])
        query = Query(grades_table)
        keys = []
        print(i)
        writer.writerow(repeat(grades_table, query, keys))





with open('performance1v0.csv','a') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):
        db = Database()
        grades_table = db.create_table('Grades', 5, 0)
        query = Query(grades_table)
        keys = []
        print(i)
        writer.writerow(repeat(grades_table, query, keys))


def repeat(grades_table, query, keys):
    seed(3562901)
    insert_time_0 = process_time()
    for i in range(0, 10000):
        query.insert(906659671 + i, randrange(0, 100), randrange(0, 100), randrange(0, 100), randrange(0, 100))
        keys.append(906659671 + i)
    insert_time_1 = process_time()
    insert_time = insert_time_1 - insert_time_0
    # Measuring update Performance    
    select_time_0 = process_time()
    for i in range(0, 1000):
        query.select(randrange(0, 100), 1, [1, 1, 1, 1, 1])
    select_time_1 = process_time()
    select_time =  select_time_1 - select_time_0
    sum_time0 = process_time()
    for i in range(0, 10):
        query.sum(0, 0, 3, 1)
    sum_time1 = process_time()
    sum_1time = sum_time1 - sum_time0
    sum_time0 = process_time()
    for i in range(0, 10):
        query.sum(0, 4, 3, 1)
    sum_time1 = process_time()
    sum_2time = sum_time1 - sum_time0
    sum_time0 = process_time()
    for i in range(0, 10):
        query.sum(0, 9, 3, 1)
    sum_time1 = process_time()
    sum_3time = sum_time1 - sum_time0
    sum_time0 = process_time()
    for i in range(0, 10):
        query.sum(0, 19, 3, 1)
    sum_time1 = process_time()
    sum_4time = sum_time1 - sum_time0
    sum_time0 = process_time()
    for i in range(0, 10):
        query.sum(0, 29, 3, 1)
    sum_time1 = process_time()
    sum_5time = sum_time1 - sum_time0
    return [select_time, sum_1time, sum_2time, sum_3time, sum_4time, sum_5time]

# Student Id and 4 grades
db = Database()
grades_table = db.create_table('Grades', 5, 0)
query = Query(grades_table)
keys = []

result = []



with open('performance_selectsum_with_index.csv','w') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):    
        print(i)
        db = Database()
        grades_table = db.create_table('Grades', 5, 0, [1])
        query = Query(grades_table)
        keys = []
        writer.writerow(repeat(grades_table, query, keys))

with open('performance_selectsum_without_index.csv','w') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for i in range(100):
        print(i)
        db = Database()
        grades_table = db.create_table('Grades', 5, 0)
        query = Query(grades_table)
        keys = []
        writer.writerow(repeat(grades_table, query, keys))

