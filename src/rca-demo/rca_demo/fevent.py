from datetime import datetime
from dataclasses import dataclass


class FulfillmentEventParameter:
    pass


@dataclass
class FulfillmentEventType:
    """container for Fulfillment event type"""
    name: str
    parameters: list[FulfillmentEventParameter]


@dataclass
class FulfillmentEvent:
    """container for Fulfillment event"""
    timestamp: datetime

    type: FulfillmentEventType
