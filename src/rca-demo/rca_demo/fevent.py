from datetime import datetime
from dataclasses import dataclass


@dataclass
class FulfillmentEventType:
    """container for Fulfillment event type"""
    name: str
    parameters: list[str]


@dataclass
class FulfillmentEvent:
    """container for Fulfillment event"""
    timestamp: datetime

    type: FulfillmentEventType
