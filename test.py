import googlemaps

google_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key='
api_key = 'AIzaSyBnSI5louf-p4SxBGhonqHgL_NYpztZro4'

gmaps = googlemaps.Client(key='AIzaSyBnSI5louf-p4SxBGhonqHgL_NYpztZro4')
consulta = gmaps.distance_matrix('london', 'manchester')

for x in consulta:
    destination_city = consulta['destination_addresses'][0].split(",")[0]
    print('')


