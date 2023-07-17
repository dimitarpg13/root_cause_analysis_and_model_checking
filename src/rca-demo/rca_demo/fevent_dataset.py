from dataclasses import dataclass
from rca_demo.fevent import FulfillmentEvent, FulfillmentEventType
from ruamel.yaml import YAML

FULFILLMENT_EVENT_TYPES_SCHEMA = "fulfillment_events.yaml"


@dataclass
class FulfillmentEventDataset:
    """container for Fulfillment event dataset"""
    name: str
    events: list[FulfillmentEvent]


class FulfillmentEventDatasetGenerator:
    def __init__(self):
        pass


def load_event_types(file: str) -> list[FulfillmentEventType]:
    yaml = YAML(typ='safe')
    with open(file, 'r') as stream:
        fevent_types_dict = yaml.load(stream)
        fevent_types = list()
        for key, fevent_dict in fevent_types_dict.items():

            fevent = FulfillmentEventType(name=fevent_dict['name'], parameters=fevent_dict['parameters'])
            fevent_types.add(fevent)
        return fevent_types

