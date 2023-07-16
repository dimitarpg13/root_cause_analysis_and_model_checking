from dataclasses import dataclass
from fevent import FulfillmentEvent


@dataclass
class FulfillmentEventDataset:
    """container for Fulfillment event dataset"""
    name: str
    events: list[FulfillmentEvent]


class FulfillmentEventDatasetGenerator:
    def __init__(self):
        pass
