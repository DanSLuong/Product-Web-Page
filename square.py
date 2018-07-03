from __future__ import print_function

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.catalog_api import CatalogApi
from squareconnect.apis.locations_api import LocationsApi

# setup authorization
squareconnect.configuration.access_token = 'access token goes here'
# create an instance of the Location API class
# api_instance = LocationsApi()
api_instance = CatalogApi()


def __getitem__(self, index):
    return self.api_response.objects[index]


def __setitem__(self, index):
    self.api_response.objects[index] = value


api_instances = []
api_instances2 = []
try:
    # ListLocations
    # api_response = api_instance.list_locations()
    # print (api_response.locations)
    # api_instances.append(api_response.locations)
    # List catalog list
    api_response = api_instance.list_catalog()
    api_instances.append(api_response.objects)
    # print (api_instances[0][90])

except ApiException as e:
    print ('Exception when calling CatalogApi->list_catalog: %s\n' % e)

# Pull product values
value = 1
count = 1
squaredata = []
squaredata2 = {}
while value<len(api_instances[0]):
      if api_instances[0][value].item_data:
            if api_instances[0][value].item_data.variations[0].item_variation_data.sku:
                cost = float(
                        api_instances[0][value].item_data.variations[0].item_variation_data.price_money.amount)
                """
                squaredata.append([{'name': api_instances[0][value].item_data.name},
                                  {'description': api_instances[0][value].item_data.description},
                                  {'category_id': api_instances[0][value].item_data.category_id},
                                  {'product_type': api_instances[0][value].item_data.product_type},
                                  {'product_id': api_instances[0][value].item_data.variations[0].id},
                                  {'other_id': api_instances[0][value].item_data.variations[0].item_variation_data.item_id},
                                  {'image_url': api_instances[0][value].item_data.image_url},
                                  {'product_sku': api_instances[0][value].item_data.variations[0].item_variation_data.sku},
                                  {'cost': cost/100},
                                  {'stock_count_alert': api_instances[0][value].item_data.variations[0].item_variation_data.inventory_alert_type}])
                """
                squaredata.append([api_instances[0][value].item_data.name,
                                  api_instances[0][value].item_data.description,
                                  api_instances[0][value].item_data.category_id,
                                  api_instances[0][value].item_data.product_type,
                                  api_instances[0][value].item_data.variations[0].id,
                                  api_instances[0][value].item_data.variations[0].item_variation_data.item_id,
                                  api_instances[0][value].item_data.image_url,
                                  api_instances[0][value].item_data.variations[0].item_variation_data.sku,
                                  cost/100,
                                  api_instances[0][value].item_data.variations[0].item_variation_data.inventory_alert_type])
                
                squaredata2 = {'name': api_instances[0][value].item_data.name,
                                  'description': api_instances[0][value].item_data.description,
                                  'category_id': api_instances[0][value].item_data.category_id,
                                  'product_type': api_instances[0][value].item_data.product_type,
                                  'product_id': api_instances[0][value].item_data.variations[0].id,
                                  'other_id': api_instances[0][value].item_data.variations[0].item_variation_data.item_id,
                                  'image_url': api_instances[0][value].item_data.image_url,
                                  'product_sku': api_instances[0][value].item_data.variations[0].item_variation_data.sku,
                                  'cost': cost/100,
                                  'stock_count_alert': api_instances[0][value].item_data.variations[0].item_variation_data.inventory_alert_type}
      value+=1
i = 0
j = 0
for i in range(len(squaredata)):
      for j in range(len(squaredata[i])):
            print (squaredata[i][j])      
      print ('---------------------------------------------------------------------------------------------------------------------')

#print (squaredata2['name'])
"""
# Setup authorization
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
