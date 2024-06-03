import pymssql
import sched
import time
import random
from datetime import datetime, timedelta

counter = 1

conn = pymssql.connect(
    server='localhost',
    port="1433",
    user='sa',
    password='YourSTRONG!Passw0rd',
    database='industriuka',
    as_dict=True
)

cursor = conn.cursor()


def random_datetime(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def insert_random_frames(n):
    for _ in range(n):
        volume = random.uniform(0, 100)
        frame_time = random_datetime(
            datetime(2020, 1, 1), datetime(2024, 1, 1))
        cursor.execute('''
        INSERT INTO Frames (Volume, FrameTime) VALUES (%s, %s)
        ''', (volume, frame_time))
    conn.commit()


def insert_random_points(n):
    for _ in range(n):
        frame_id = counter
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        z = random.uniform(-100, 100)
        distance = random.uniform(0, 1000)
        intensity = random.uniform(0, 1)
        point_id = random.uniform(0, 1000)
        return_id = random.uniform(0, 10)
        ambient = random.uniform(0, 10)
        timestamp = random.uniform(0, 1)
        cursor.execute('''
        INSERT INTO Points (FrameId, X, Y, Z, Distance, Intensity, Point_Id, Return_Id, Ambient, Timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (frame_id, x, y, z, distance, intensity, point_id, return_id, ambient, timestamp))
    conn.commit()


def do_something(scheduler):
    global counter
    scheduler.enter(10, 1, do_something, (scheduler,))
    insert_random_frames(1)
    insert_random_points(50)
    counter = counter + 1
    print("Inserted data into DB")


my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(10, 1, do_something, (my_scheduler,))
my_scheduler.run()
