#############myqdb_logo_query.py##############
import numpy
import pandas
import yan_image_embedding

logo_index_df = pandas.read_json(	
	path_or_buf = 'myqdb_logo_index.json',
	orient = 'records',
	lines = True)

def query_by_logo_photo(
	query_logo_file
	):
	query_logo_vector = numpy.array(
			yan_image_embedding.image_to_vector(query_logo_file)
			)
	########
	def calculat_dist(r):
		r['distance'] = numpy.linalg.norm(
			numpy.array(r['logo_embedding_vector']) 
			- query_logo_vector)
		return r
	logo_dist = logo_index_df.apply(calculat_dist, axis = 1)
	most_similar_logo = logo_dist.sort_values(
		'distance',
		 ascending = True).head(1)
	####
	most_similar_logo = most_similar_logo.to_dict(orient='records')[0]
	#####
	most_similar_logo['distance']
	most_similar_logo['logo_file_name']
	###
	return {"logo_file_name":most_similar_logo['logo_file_name'], 
		"distance":most_similar_logo['distance']}

'''

import myqdb_logo_query

query_logo_file = "/Downloads/myqdb_company_logo_file/4b27d91df5985313d068b86d5d7eedec.PNG"

print(myqdb_logo_query.query_by_logo_photo(query_logo_file))

'''

#############myqdb_logo_query.py##############
