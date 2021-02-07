from influxdb import InfluxDBClient
import settings
import datetime


def log_request(title, id, user):
    t = datetime.datetime.utcnow()

    d = [
        {
            'measurement': 'request',
            "time": t,
            "fields": {
                "title": title,
                "id": id,
                "user": user
            }
        }
    ]

    ifclient = InfluxDBClient(settings.INFLUXDB_IP, settings.INFLUXDB_PORT,
                              settings.INFLUXDB_USER, settings.INFLUXDB_PASS, settings.INFLUXDB_DB)
    ifclient.write_points(d)
