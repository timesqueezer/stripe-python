import stripe
from stripe.test.helper import (
    StripeResourceTest
)


class PlanTest(StripeResourceTest):
    def test_get_resource(self):
        stripe.CountrySpec.retrieve('US')
        self.requestor_mock.assert_called_with(
            'get',
            '/v1/country_specs/US',
            {},
            None
        )

    def test_list_resource(self):
        stripe.CountrySpec.all()
        self.requestor_mock.assert_called_with(
            'get',
            '/v1/country_specs',
            {},
            None
        )
