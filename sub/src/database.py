# ref: https://www.youtube.com/watch?v=O20Y1XR6g0A&list=PLoVvAgF6geYMb029jpxqMuz5dRDtO0ydM&index=4


from influxdb import InfluxDBClient
from config import DB_HOST, DB_PORT, DB_NAME,DB_USER, DB_PASS 


def client():
    # InfluxDB client setup
    client = InfluxDBClient(host=DB_HOST, port=int(DB_PORT), username=DB_USER, password=DB_PASS)

    # databases
    #client.get_list_database()

    # create a database
    client.create_database(DB_NAME)

    # use a database
    client.switch_database(DB_NAME)

    # measurements/tables
    #client.get_list_measurements()

    return client

def save(db_client, measurement, fields, tags=None):
    # json data
    """
    json_body = {}
    json_body['measurement'] = measurement
    
    if tags != None:
        json_body['tags'] = tags

    json_body['fields'] = fields

    # make list
    json_body = [json_body]
    """

    # alternatively
    json_body = [{'measurement': measurement, 'tags': tags, 'fields': fields}]

    # write / save into a row
    db_client.write_points(json_body)
