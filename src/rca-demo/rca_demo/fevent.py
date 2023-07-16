from datetime import datetime
from dataclasses import dataclass


@dataclass
class FulfillmentEvent:
    """container for Fulfillment event"""
    timestamp: datetime
    