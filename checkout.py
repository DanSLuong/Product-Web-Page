api = squareconnect.apis.checkout_api.CheckoutApi()
result = api.create_checkout(LOCATION_ID, CreateCheckoutRequest(
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
        name='Father's day 12% OFF',
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



"""
# TEMPLATE
{
  "redirect_url": "{{URL TO CONFIRMATION PAGE}}",
  "idempotency_key": "{{UNIQUE STRING FOR THIS TRANSACTION}}",
  "ask_for_shipping_address": {{true or false}},
  "merchant_support_email": "{{SUPPORT EMAIL ADDRESS}}",

  "order": {
    "reference_id": "{{STORE ORDER ID}}",
    "line_items": [

      // List each item in the order as an individual line item
      {
        "name": "{{ITEM_1 NAME}}",
        "quantity": "{{ITEM_1 QUANTITY}}",
        "base_price_money": {
          "amount": {{ITEM_1 COST IN BASE MONETARY UNIT}},
          "currency": "{{ITEM_1 CURRENCY USED}}"
        },
        discounts: [
          {
            "name": "{{ITEM_1_DISCOUNT NAME}}",
            "amount_money": {
              "amount": {{ITEM_1_DISCOUNT AMOUNT}},
              "currency": "{{ITEM_1_DISCOUNT CURRENCY USED}}"
            }
          }
        ],
        "taxes": [
          {
           "name": "{{ITEM_1_TAX NAME}}",
           "percentage": "{{ITEM_1_TAX PERCENTAGE}}",
           "type": "{{ITEM_1_TAX TYPE}}"
         }
        ]
      },
      {
        "name": "{{ITEM_2 NAME}}",
        "quantity": "{{ITEM_2 QUANTITY}}",
        "base_price_money": {
          "amount": {{ITEM_2 COST IN BASE MONETARY UNIT}},
          "currency": "{{ITEM_2 CURRENCY USED}}"
        }
      },
      . . .
      {
        "name": "{{ITEM_N NAME}}",
        "quantity": "{{ITEM_N QUANTITY}}",
        "base_price_money": {
          "amount": {{ITEM_N COST IN BASE MONETARY UNIT}},
          "currency": "{{ITEM_N CURRENCY USED}}"
        },
        discounts: [
         {
           "name": "{{ITEM_N_DISCOUNT NAME}}",
           "percentage": "{{ITEM_N PERCENTAGE USED}}"
         }
       ]
      },
    ]
  },
  "pre_populate_buyer_email": "{{CUSTOMER CONTACT INFORMATION: EMAIL}}",
  "pre_populate_shipping_address": {
    "address_line_1": "{{SHIPPING ADDRESS, LINE 1}}",
    "address_line_2": "{{SHIPPING ADDRESS, LINE 2}}",
    "locality": "{{SHIPPING CITY/TOWNSHIP/ETC}}",
    "administrative_district_level_1": "{{SHIPPING STATE/PROVINCE/ETC}}",
    "postal_code": "{{SHIPPING POSTAL CODE}}",
    "country": "{{SHIPPING COUNTRY}}",
    "first_name": "{{CUSTOMER FIRST NAME}}",
    "last_name": "{{CUSTOMER LAST NAME}}"
  },
  "additional_recipients":[
    {
      "location_id":  "{{RECIPIENT_LOCATION_ID}}",
      "description":  "{{DESCRIPTION}}",
        "amount_money" : {
          "amount": {{SPLIT AMOUNT IN BASE MONETARY UNIT}},
          "currency": "{{CURRENCY USED}}"
      }
    }
  ]
}
"""
