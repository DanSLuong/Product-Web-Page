from __future__ import print_function

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.catalog_api import CatalogApi
from squareconnect.apis.locations_api import LocationsApi

# setup authorization
# squareconnect.configuration.access_token = 'sandbox-sq0atb-qx31rXzSRO7qdDYJcZXH0g'
squareconnect.configuration.access_token = 'sq0atp-Jnd1NosIJD8tzPhVbaDBlw'
# create an instance of the Location API class
# api_instance = LocationsApi()
api_instance = CatalogApi()

api_instances = []
api_instances2 = []
try:
    # ListLocations
    # api_response = api_instance.list_locations()
    # api_instances.append(api_response.locations)
    # List catalog list
    api_response = api_instance.list_catalog()
    api_instances.append(api_response.objects)
    i = 1
    for i in range(100):
          api_instances2.append(api_instances[0][i])

    # print (api_response)
except ApiException as e:
    print ('Exception when calling CatalogApi->list_catalog: %s\n' % e)

value = 2

print (api_instances[0][value].item_data)

print ('category ID:')
print (api_instances[0][value].item_data.category_id)
print ('Product Type:')
print (api_instances[0][value].item_data.product_type)
print ('Product ID:')
print (api_instances[0][value].item_data.variations[0].id)
print (api_instances[0][value].item_data.variations[0].item_variation_data.item_id)
print ('Product Description:')
print (api_instances[0][value].item_data.description)
print ('Image URL:')
print (api_instances[0][value].item_data.image_url)
print ('Product SKU:')
print (api_instances[0][value].item_data.variations[0].item_variation_data.sku)
print ('Product Name:')
print (api_instances[0][value].item_data.name)
print ('Product Cost:')
if api_instances[0][value].item_data.variations[0].item_variation_data.price_money:
      cost = float(api_instances[0][value].item_data.variations[0].item_variation_data.price_money.amount)
      print (cost/100)
else:
      print ('No set cost')
print ('Stock Count Alert')
print (api_instances[0][value].item_data.variations[0].item_variation_data.inventory_alert_type)



"""
# Setup authorization.
squareconnect.configuration.access_token = sqdemo-CiVzYW5kYm94LXNxMGF0Yi12ZzNfbEZVTjUxbWRsZWZTUGpEVmxBEhtDQkFTRUxPV1pLY0xSY0w2N2N4OHFqaThBLVU=



api = squareconnect.apis.catalog_api.CatalogApi()

# Retrieve a single object by its id, along with related objects.
response = api.retrieve_catalog_object(object_id='W62UWFY35CWMYGVWK6TWJDNI', include_related_objects=True)



####################################################################


api = squareconnect.apis.catalog_api.CatalogApi()

# Search for all Items with name prefix "tea".
body = SearchCatalogObjectsRequest(
  object_types=[
    "ITEM"
  ],
  query=CatalogQuery(
    prefix_query=CatalogQueryPrefix(
      attribute_name='name',
      attribute_prefix='tea'
    )
  ),
  limit=100
)

# Retrieve the first page of the response.
# Additional pages may be retrieved using the response cursor.
response = api.search_catalog_objects(body)
print(response)



####################################################################

api = squareconnect.apis.catalog_api.CatalogApi()

# Create a new item and/or reconfigure an existing item
item_cocoa = CatalogObject(
  type='ITEM',
  id='#Cocoa',
  item_data=CatalogItem(
    name='Cocoa',
    description='Hot chocolate',
    abbreviation='Ch'
  )
)

# Initialize request body.
# Set a unique idempotency key for each request.
body = UpsertCatalogObjectRequest(
  idempotency_key='af3d1afc-7212-4300-b463-0bfc5314a5ae',
  object=item_cocoa
)

# Upsert the catalog item
response = api.upsert_catalog_object(body)
"""