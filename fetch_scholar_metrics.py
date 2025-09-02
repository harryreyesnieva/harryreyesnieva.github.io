# # fetch_scholar_metrics.py
# import yaml
# from scholarly import scholarly
#
# # Your Google Scholar user ID
# SCHOLAR_ID = "L58_1hAAAAAJ"
#
# # Fetch profile
# profile = scholarly.search_author_id(SCHOLAR_ID)
# profile = scholarly.fill(profile, sections=['indices'])
#
# # Extract metrics
# metrics = {
#     'citations': profile.get('citedby', 0),
#     'h_index': profile.get('hindex', 0)
# }
#
# # Write to Jekyll _data folder
# with open('_data/scholar_metrics.yml', 'w') as f:
#     yaml.dump(metrics, f)
#
# print("Google Scholar metrics updated:", metrics)

from scholarly import scholarly
import yaml

author = scholarly.search_author_id('L58_1hAAAAAJ')
author_data = scholarly.fill(author)

metrics = {
    "citations": author_data['citedby'],
    "h_index": author_data['hindex']
}

with open("_data/scholar_metrics.yml", "w") as f:
    yaml.dump(metrics, f)
