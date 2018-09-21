import urllib.request
import urllib.parse
import json
#location = input('Enter Location:')
#w = urllib.parse.urlencode({'sensor':'false', 'address':location})
#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#wholeurl = serviceurl + w
#print (wholeurl)
#content = urllib.request.urlopen(wholeurl).read()
content = '''
{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "杭州市",
               "short_name" : "杭州市",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "浙江省",
               "short_name" : "浙江省",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "中国",
               "short_name" : "CN",
               "types" : [ "country", "political" ]
            }
         ],
         "formatted_address" : "中国浙江省杭州市",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 30.5665161,
                  "lng" : 120.7219451
               },
               "southwest" : {
                  "lat" : 29.18875719999999,
                  "lng" : 118.3449334
               }
            },
            "location" : {
               "lat" : 30.274085,
               "lng" : 120.15507
            },
            "location_type" : "APPROXIMATE",
            "viewport" : {
               "northeast" : {
                  "lat" : 30.4743515,
                  "lng" : 120.4307556
               },
               "southwest" : {
                  "lat" : 30.0484295,
                  "lng" : 119.9130249
               }
            }
         },
         "place_id" : "ChIJmaqaQym2SzQROuhNgoPRv6c",
         "types" : [ "locality", "political" ]
      }
   ],
   "status" : "OK"
}
'''

info = json.loads(content)
k = info['results'][0]['geometry']['location']

print (k)
