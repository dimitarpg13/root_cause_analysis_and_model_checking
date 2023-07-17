from dataclasses import dataclass
from fevent import FulfillmentEvent, FulfillmentEventType

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
    
    pass
