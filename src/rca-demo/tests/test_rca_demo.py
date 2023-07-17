from rca_demo import __version__

from rca_demo.fevent_dataset import FulfillmentEventType, load_event_types, FULFILLMENT_EVENT_TYPES_SCHEMA


def test_version():
    assert __version__ == '0.1.0'


def test_load_event_types():
    event_types = load_event_types(FULFILLMENT_EVENT_TYPES_SCHEMA)

    assert event_types is not None
    assert isinstance(event_types, list) is True
    assert len(event_types) > 0
    assert isinstance(event_types[0], FulfillmentEventType) is True
