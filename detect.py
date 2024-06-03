import sched
import time
import blickfeld_qb2
import pymssql

conn = pymssql.connect(
    server='localhost',
    user='sa',
    password='kurs'
)

cursor = conn.cursor()

# Open a secure connection to Qb2
with blickfeld_qb2.Channel(fqdn_or_ip="192.168.26.26") as channel:
    def do_something(scheduler):
        scheduler.enter(5, 1, do_something, (scheduler,))
        zones = blickfeld_qb2.percept_pipeline.services.Zone(channel).list()
        response = blickfeld_qb2.percept_pipeline.services.Zone(
            channel).get_tare_volume(zone_uuid=zones.zones[0].uuid)
        liters = response.tare_volume * 1_000
        rounded_liters = round(liters, 1)

        point_cloud = blickfeld_qb2.core_processing.services.PointCloud.get()

    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(5, 1, do_something, (my_scheduler,))
    my_scheduler.run()
