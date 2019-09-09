# Generate the data.json file used to populate the Data section of the website.
import json

DATASETS = [{'name':'Annnotated Hypergraphs',
             'short_name': 'ah',
             'desc':'Annotated hypergraphs capturing nodes with different roles in higher-order interactions.',
             'citations':['ANNOTATED  HYPERGRAPHS:  NULL  MODELS  AND  APPLICATIONS, Chodrow P. & Mellor A. (2019)'],
             'data':[
                 {'name':'Enron Emails',
                  'short_name':'enron',
                  'src_link':'https://drive.google.com/open?id=1If5ogZnIZTiy3il8YZYRitGtUtpPb3xE',
                  'desc':'This consists of the core Enron emails from the archived <a href="https://www.cs.cmu.edu/~enron/">Enron email database</a> from William W. Cohen. Core email addresses are those with a valid Enron address. All other emails have been omitted. Here the node roles are <i>from</i>, <i>to</i>, and <i>cc</i> which capture the various fields in a typical email header (in this case BCC has been merged with CC). Note that a node may appear in an edge twice under multiple roles, for example sending a message to oneself.',
                  'nodes':112,
                  'edges':10504,
                  'edge_stubs':25847,
                  'roles':['from', 'to', 'cc'],
                  'metadata':['date'],
                  'edge_avg_degree':2.46,
                  'node_avg_degree':230.77,
                 },
                 {'name':'Stack Overflow Threads',
                  'short_name':'overflow-stack',
                  'src_link':'https://drive.google.com/open?id=1qr2sfZkwJuYufYqDHoE_II49XoR9i75V',
                  'nodes':22131,
                  'edges':4716,
                  'edge_stubs':28250,
                  'roles':['setter', 'answers', 'accepted'],
                  'metadata':['timestamp'],
                  'edge_avg_degree':5.99,
                  'node_avg_degree':1.27,
                 },
                 {'name':'Math Overflow Threads',
                  'short_name':'overflow-math',
                  'src_link':'https://drive.google.com/open?id=1RFBA50lhAAvvMfcWvp7NwszKjFCKcfG5',
                  'nodes':410,
                  'edges':154,
                  'edge_stubs':709,
                  'roles':['setter', 'answers', 'accepted'],
                  'metadata':['timestamp'],
                  'edge_avg_degree':4.60,
                  'node_avg_degree':1.73,
                 },
                 {'name':'MovieLens Credits',
                  'short_name':'movielens',
                  'src_link':'https://drive.google.com/open?id=1JXaUSD2-ZBLAX2ukggtD_6fY1sjSzw4k',
                  'nodes':112,
                  'edges':10504,
                  'edge_stubs':25847,
                  'roles':['from', 'to', 'cc'],
                  'metadata':['date'],
                  'edge_avg_degree':2.46,
                  'node_avg_degree':230.77,
                 },
                 {'name':'Scopus Multilayer Literature',
                  'short_name':'scopus-multilayer',
                  'src_link':'https://drive.google.com/open?id=1p6_oH6Q01OhMY0RSx-xNtawbPuRzXPBz',
                  'nodes':1722,
                  'edges':938,
                  'edge_stubs':3615,
                  'roles':['first', 'middle', 'last'],
                  'metadata':['citations', 'dtype', 'source', 'year'],
                  'edge_avg_degree':3.85,
                  'node_avg_degree':2.10,
                 },
                 {'name':'Twitter Keyword Search',
                  'short_name':'twitter',
                  'src_link':'https://drive.google.com/open?id=1EFmOSgoiExM9sjIVThEKq2lzwMg1AoUj',
                  'nodes':52294,
                  'edges':123158,
                  'edge_stubs':265815,
                  'roles':['source', 'target', 'retweeter', 'retweeted'],
                  'metadata':['time','type'],
                  'edge_avg_degree':2.16,
                  'node_avg_degree':5.08,
                 },
                # {'name':'DBLP Computer Science Bibliography',
                #   'short_name':'dblp',
                #   'src_link':'https://drive.google.com/open?id=1Npbpr6rk4dKI3jxxonR1Qt63Rd_RFmuC',
                #   'desc':'',
                #   'nodes':112,
                #   'edges':10504,
                #   'edge_stubs':25847,
                #   'roles':['from', 'to', 'cc'],
                #   'metadata':['date'],
                #   'edge_avg_degree':2.46,
                #   'node_avg_degree':230.77,
                #  }
             ]}]

def generate_links(dataset):
    """
    Generate links for data.
    """
    for data in dataset:
        for entry in data['data']:
            entry['link'] = data['short_name'] + '-' + entry['short_name']

if __name__ == "__main__":

    generate_links(DATASETS)

    with open('../app/mod_home/static/data.json', 'w') as file:
        json.dump(DATASETS, file, sort_keys=True, indent=4)
    with open('../app/static/data.json', 'w') as file:
        json.dump(DATASETS, file, sort_keys=True, indent=4)