
from multiprocessing import Process

from .models import PlantRecord, ChannelData, PlantDb

def save_record(data):
    print(f"msg: {data}")
    msg = data.split(',')
    record = PlantRecord.objects.create(
        name = "plant1",
        plant_type = "ZZ Plant",
        moisture_lvl=msg[1]
    )
    record.save()
    record = PlantRecord.objects.create(
        name = "plant2",
        plant_type = "ZZ Plant",
        moisture_lvl=msg[2]
    )
    record.save()
    record = PlantRecord.objects.create(
        name = "plant3",
        plant_type = "Dracaena",
        moisture_lvl=msg[3]
    )
    record.save()