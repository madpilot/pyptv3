# pyptv3 - Access the Public Transport Victoria API with Python 3

pyptv3 is a Python library that provides a light wrapper around version 3 of the Public Transport Victoria (PTV) API.

The PTV Timetable API provides direct access to Public Transport Victoria’s public transport timetable data.

The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).

The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.

## Getting Started

You will need a developer key from PTV. The instructions (in RTF format) are [here](https://static.ptv.vic.gov.au/PTV/PTV%20docs/API/1475462320/PTV-Timetable-API-key-and-signature-document.RTF), though if you can't be bothered downloading that, the TL;DR is to send an email to [APIKeyRequest@ptv.vic.gov.au](mailto:APIKeyRequest@ptv.vic.gov.au) with the following information in the subject line of the email.

## Installation

```bash
pip install pyptv3
```

## Example

All API endpoints require a client object to be setup first. The client object takes your developer id and api key as arguments.
```python
from pyptv3 import Client
client = Client("your developer id", "your api key")
```

As a general rule, required path parameters are passed as positional arguments, and optionals are passed as lists. See the [swagger documentation](http://timetableapi.ptv.vic.gov.au/swagger/ui/index) for more information.

```python
from pyptv3 import Client, Departures
client = Client("your developer id", "your api key")
departures = Departures(client, 0, 1341).by_route(4122, platform_numbers=[0, 1], direction_id=1, look_backwards=False, gtfs=123, date_utc="2018-06-28T07:00:00Z", max_results=10, include_cancelled=True, expand=["stop", "route"])
print(departures)
```

## AsyncIO Example

There is a Async IO client if you want non-blocking behaviour

```python
import asyncio
from pyptv3 import AsyncClient, Departures

loop = asyncio.get_event_loop()
client = AsyncClient(loop, "your developer id", "your api key")

def main():
  departures = await Departures(client, 0, 1341).by_route(4122, platform_numbers=[0, 1], direction_id=1, look_backwards=False, gtfs=123, date_utc="2018-06-28T07:00:00Z", max_results=10, include_cancelled=True, expand=["stop", "route"])
  print(departures)

loop.run_until_complete(main())
loop.close()
```

# TODO

* pydoc
* Map the parsed JSON object to Python objects.
