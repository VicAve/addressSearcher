#*****************************************************
#*****************************************************
#       To find the address direction we will use: Google api
#       -Service = geocode
#       -output type = json
#       -parameter = address parsed with secure HTTP transfer
#*****************************************************
#*****************************************************
from urllib.request import urlopen
from urllib.parse import quote
import json

def checkAddress(to_search):
    #   The set of the address to search
    address = quote(to_search)
    result_set = []

    #   The configuration of the address
    service_API = 'geocode/'
    response_type = 'json?'
    params = 'address='
    url_API = 'https://maps.googleapis.com/maps/api/' + service_API + response_type +  params + address

    #   The request of the service to Google API
    url = urlopen(url_API)
    result_request = url.read().decode('utf-8')
    jsonString = json.JSONDecoder().decode(result_request)

    #   Starts to organize the resulset into manageable variables
    results = jsonString['results']
    if len(results) > 0:
        for result in results:
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            addr_reg = {'address': result['formatted_address'], 'lat': lat, 'lng': lng, 'reqAddr': True}
            result_set.append(addr_reg)
    else:
        print('No direction matches')
        result_set = None
    return result_set

# def checkAddresses(to_search):
#     with open('vsearch.log', 'r') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
#     return render_template('log.html',
#                            the_title='View Log',
#                            the_row_titles=titles,
#                            the_data=contents)
