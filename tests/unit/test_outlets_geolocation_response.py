import pytest
from mock import Mock
import json
from pyptv3 import OutletsGeolocationResponse, OutletGeolocationResponse, StatusResponse, ONLINE

class TestOutletsGeolocationResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "outlets": [
              {
                "outlet_distance": 1000,
                "outlet_slid_spid": "814",
                "outlet_name": "3/67-69 Separation Street",
                "outlet_business": "7-Eleven Geelong North",
                "outlet_latitude": -38.1110878,
                "outlet_longitude": 144.343689,
                "outlet_suburb": "Geelong North",
                "outlet_postcode": 3215,
                "outlet_business_hour_mon": "24 Hours",
                "outlet_business_hour_tue": "24 Hours",
                "outlet_business_hour_wed": "24 Hours",
                "outlet_business_hour_thur": "24 Hours",
                "outlet_business_hour_fri": "24 Hours",
                "outlet_business_hour_sat": "24 Hours",
                "outlet_business_hour_sun": "24 Hours",
                "outlet_notes": null
              },
              {
                "outlet_distance": 2000,
                "outlet_slid_spid": "815",
                "outlet_name": "115 Moorabool Street",
                "outlet_business": "7-Eleven Geelong City",
                "outlet_latitude": -38.1483879,
                "outlet_longitude": 144.3604,
                "outlet_suburb": "Geelong",
                "outlet_postcode": 3220,
                "outlet_business_hour_mon": "24 Hours",
                "outlet_business_hour_tue": "24 Hours",
                "outlet_business_hour_wed": "24 Hours",
                "outlet_business_hour_thur": "24 Hours",
                "outlet_business_hour_fri": "24 Hours",
                "outlet_business_hour_sat": "24 Hours",
                "outlet_business_hour_sun": "24 Hours",
                "outlet_notes": "Buy pre-loaded myki cards only"
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    def test_outlets(self, response):
        subject = OutletsGeolocationResponse(response)
        assert len(subject.outlets) == 2

        assert subject.outlets[0].__class__ == OutletGeolocationResponse
        assert subject[0].__class__ == OutletGeolocationResponse

        assert subject.outlets[0].distance == 1000
        assert subject.outlets[0].id == "814"
        assert subject.outlets[0].name == "3/67-69 Separation Street"
        assert subject.outlets[0].business == "7-Eleven Geelong North"
        assert subject.outlets[0].latitude == -38.1110878
        assert subject.outlets[0].longitude == 144.343689
        assert subject.outlets[0].suburb == "Geelong North"
        assert subject.outlets[0].postcode == 3215
        assert subject.outlets[0].business_hour_mon == "24 Hours"
        assert subject.outlets[0].business_hour_tue == "24 Hours"
        assert subject.outlets[0].business_hour_wed == "24 Hours"
        assert subject.outlets[0].business_hour_thur == "24 Hours"
        assert subject.outlets[0].business_hour_fri == "24 Hours"
        assert subject.outlets[0].business_hour_sat == "24 Hours"
        assert subject.outlets[0].business_hour_sun == "24 Hours"
        assert subject.outlets[0].notes == None

        assert subject.outlets[1].distance == 2000
        assert subject.outlets[1].id == "815"
        assert subject.outlets[1].name == "115 Moorabool Street"
        assert subject.outlets[1].business == "7-Eleven Geelong City"
        assert subject.outlets[1].latitude == -38.1483879
        assert subject.outlets[1].longitude == 144.3604
        assert subject.outlets[1].suburb == "Geelong"
        assert subject.outlets[1].postcode == 3220
        assert subject.outlets[1].business_hour_mon == "24 Hours"
        assert subject.outlets[1].business_hour_tue == "24 Hours"
        assert subject.outlets[1].business_hour_wed == "24 Hours"
        assert subject.outlets[1].business_hour_thur == "24 Hours"
        assert subject.outlets[1].business_hour_fri == "24 Hours"
        assert subject.outlets[1].business_hour_sat == "24 Hours"
        assert subject.outlets[1].business_hour_sun == "24 Hours"
        assert subject.outlets[1].notes == "Buy pre-loaded myki cards only"

    def test_status(self, response):
        subject = OutletsGeolocationResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

