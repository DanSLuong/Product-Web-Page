import squareconnect
from squareconnect.models.create_order_request import CreateOrderRequest
from squareconnect.models.money import Money
from squareconnect.models.address import Address
from squareconnect.models.create_checkout_request import CreateCheckoutRequest
from squareconnect.models.create_order_request_line_item import CreateOrderRequestLineItem
from squareconnect.models.create_order_request_discount import CreateOrderRequestDiscount
from squareconnect.models.create_order_request_tax import CreateOrderRequestTax
from squareconnect.models.create_checkout_request_additional_recipient import CreateCheckoutRequestAdditionalRecipient


api = squareconnect.apis.checkout_api.CheckoutApi()
#result = api.create_checkout(LOCATION_ID, CreateCheckoutRequest(
result = api.create_checkout('CBASEI4zih64SK-qL0L7qDKKCDkgAQ', CreateCheckoutRequest(
  idempotency_key='74ae1696-b1e3-4328-af6d-f1e04d947a13',
  order=CreateOrderRequest(
    reference_id='reference_id',
    line_items=[
      CreateOrderRequestLineItem(
        name='Printed T Shirt',
        quantity='2',
        base_price_money=Money(1500, 'USD'),
        discounts=[
          CreateOrderRequestDiscount(
            name='7% off previous season item',
            percentage='7'
          ),
          CreateOrderRequestDiscount(
            name='$3 off Customer Discount',
            amount_money=Money(300, 'USD')
          )
        ]
      ),
      CreateOrderRequestLineItem(
        name='Slim Jeans',
        quantity='1',
        base_price_money=Money(2500, 'USD')
      ),
      CreateOrderRequestLineItem(
        name='Woven Sweater',
        quantity='3',
        base_price_money=Money(3500, 'USD'),
        discounts=[
          CreateOrderRequestDiscount(
            name='$11 off Customer Discount',
            amount_money=Money(1100, 'USD')
          )
        ],
        taxes=[
          CreateOrderRequestTax(
            name='Fair Trade Tax',
            percentage='5'
          )
        ]
      )
    ],
    discounts=[
      CreateOrderRequestDiscount(
        name="Father's day 12% OFF",
        percentage='12'
      ),
      CreateOrderRequestDiscount(
        name='Global Sales $55 OFF',
        amount_money=Money(5500, 'USD')
      )
    ],
    taxes=[
      CreateOrderRequestTax(
        name='Sales Tax',
        percentage='8.5'
      )
    ]
  ),
  additional_recipients=[
    CreateCheckoutRequestAdditionalRecipient(
      location_id='057P5VYJ4A5X1',
      description='Application fees',
      amount_money=Money(60, 'USD')
    )
  ],
  ask_for_shipping_address=True,
  merchant_support_email='merchant+support@website.com',
  pre_populate_buyer_email='example@email.com',
  pre_populate_shipping_address=Address(
    address_line_1='1455 Market St.',
    address_line_2='Suite 600',
    locality='San Francisco',
    administrative_district_level_1='CA',
    postal_code='94103',
    country='US',
    first_name='Jane',
    last_name='Doe'
  ),
  redirect_url='https://merchant.website.com/order-confirm'
))
checkout = result.checkout()
