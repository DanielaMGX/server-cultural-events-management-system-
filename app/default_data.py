import json

from app.schemas.contractual_mode import CreateContractualMode
from app.schemas.responsability import Createresponsability
from app.schemas.responsability_by_modality import CreateresponsabilityByMode
from app.schemas.space import CreateSpace
from app.services.contractual_mode import service_contractual_mode
from app.services.responsability import service_responsability
from app.services.responsability_by_modality import service_responsability_by_mode
from app.services.space import service_space


async def create_default_data():
    with open("default_data/contractual_mode.json") as file:
        data = json.load(file)
        if isinstance(data, list):
            print("CREATING CONTRACTUAL MODES")
            for obj in data:
                obj_in = CreateContractualMode(**obj)
                await service_contractual_mode.create(obj_in=obj_in)

    with open("default_data/space.json") as file:
        data = json.load(file)
        if isinstance(data, list):
            print("CREATING SPACES")
            for obj in data:
                obj_in = CreateSpace(**obj)
                await service_space.create(obj_in=obj_in)

    with open("default_data/responsability.json") as file:
        data = json.load(file)
        if isinstance(data, list):
            print("CREATING RESPONSABILITIES")
            for obj in data:
                obj_in = Createresponsability(**obj)
                await service_responsability.create(obj_in=obj_in)

    with open("default_data/contractual_mode.json") as file:
        data = json.load(file)
        if isinstance(data, list):
            print("CREATING CONTRACTUALMODES")
            for obj in data:
                obj_in = CreateContractualMode(**obj)
                await service_contractual_mode.create(obj_in=obj_in)
        with open("default_data/responsability_by_modality.json") as file:
            data = json.load(file)
            if isinstance(data, list):
                print("CREATING RESPONSABILITIES BY MODALITIES")
                for obj in data:
                    obj_in = CreateresponsabilityByMode(**obj)
                    await service_responsability_by_mode.create(obj_in=obj_in)
