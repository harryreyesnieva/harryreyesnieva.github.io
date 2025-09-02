from scholarly import scholarly, ProxyGenerator
import yaml
import sys

# Use free proxies to avoid Google Scholar blocking
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_pg(pg)

AUTHOR_ID = "L58_1hAAAAAJ"

try:
    author = scholarly.search_author_id(AUTHOR_ID)
    author_filled = scholarly.fill(author, sections=['basics'])

    metrics = {
        'citations': author_filled['citedby'],
        'h_index': author_filled['hindex']
    }

    with open('_data/scholar_metrics.yml', 'w') as f:
        yaml.dump(metrics, f)

    print(f"Fetched citations: {metrics['citations']}, h-index: {metrics['h_index']}")

except Exception as e:
    print("Error fetching scholar metrics:", e)
    sys.exit(1)
