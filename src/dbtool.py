import influxpy
import settings

handler = influxpy.UDPHandler(
    APIKEY.INFLUXDB_IP, APIKEY.INFLUXDB_PORT, "influxpy_logs", global_tags={"app": "example"})
logger.addHandler(handler)
