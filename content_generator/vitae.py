# Generate the vitae.json file used to populate the Vitae section of the website.

import pandas as pd
import re
from datetime import datetime
from collections import defaultdict
import json

# Publications

def create_publications(filepath):

    publications = pd.read_excel(filepath, sheetname='publications', endcoding='utf-8')
    publications = publications.fillna('')

    publication_store = defaultdict(list)
    for ix, pub in publications.iterrows():

        date = re.sub(r"([0123]?[0-9])(st|th|nd|rd)",r"\1", pub.date)
        date = datetime.strptime(date, '%d %B %Y')
        date = date.strftime('%Y')

        entry = {'title': pub.title,
                'authors': pub.authors,
                'arxiv': pub.arxiv,
                'abstract':pub.abstract,
                'date': date}
        if pub.link != '':
            entry['link'] = pub.link
        if pub.journal != '':
            entry['journal'] = pub.journal

        publication_store[pub.type].append(entry)
    
    return publication_store

def create_conferences(filepath):

    conferences = pd.read_excel(filepath, sheetname='conferences', endcoding='utf-8')
    conferences = conferences.fillna('')
    
    categories = [('invited', 'Invited Talks \& Posters'),
                  ('contributed', 'Contributed Talks \& Posters'),
                  ('attended', 'Attended'),
                  ('school', 'Schools')]
    
    conference_store = {}

    for key, subtitle in categories:
        data = conferences[conferences.type == key]
        collection  = []
        if len(data) > 0:
            for ix, conf in data.iterrows():
                
                if conf.include=='no': continue

                date = re.sub(r"([0123]?[0-9])(st|th|nd|rd)",r"\1", conf.date)
                date = datetime.strptime(date, '%d %B %Y')
                date = date.strftime('%b. %Y')

                if key in ['attended', 'school']:
                    contribution = 'Attendee'
                else:
                    contribution = "{} {}".format(conf.type.capitalize(), conf.style.capitalize()) 

                entry = {'title':conf.conference,
                        'location':conf.location,
                        'date':date,
                        'contribution': contribution,
                        }

                if conf.link != '':
                    entry['link'] = conf.link
                if (conf.presentation_title != '') & (conf.presentation_authors != ''):
                    entry['presentation_authors'] = conf.presentation_authors
                    entry['presentation_title'] = conf.presentation_title

                collection.append(entry)
        conference_store[key] = collection
    
    return conference_store

def create_teaching(filepath):

    teaching = pd.read_excel(filepath, sheetname='teaching', endcoding='utf-8')
    teaching = teaching.fillna('')

    teaching_store = []

    for ix, teach in teaching.sort_values(by='subtype').iterrows():
        if teach['type'] == 'supervision':
            entry = {
                'date': teach.short_date,
                'project_award': teach.project_award,
                'title': teach.title,
                'student': teach.student_name,
                'institution': teach.institution
            }

            teaching_store.append(entry)

    return teaching_store

def create_reviewing(filepath):

    reviewing = pd.read_excel(filepath, sheetname='journals', endcoding='utf-8')
    reviewing = reviewing.fillna('')

    review_store = []

    for ix, review in reviewing.iterrows():
        entry = {'name': review.journal_name,
                 'short_name': review.journal_shortname}
        review_store.append(entry)

    return review_store

if __name__ == "__main__":

    FILEPATH = "D:/Dropbox/Academics/CV/vitae.xlsx" # We can pass this as an argument later
    vitae = {'publications':create_publications(FILEPATH),
             'conferences':create_conferences(FILEPATH),
             'teaching':create_teaching(FILEPATH),
             'reviewing':create_reviewing(FILEPATH)}

    with open('../app/mod_home/static/vitae.json', 'w') as file:
        json.dump(vitae, file, sort_keys=True, indent=4)
    with open('../app/static/vitae.json', 'w') as file:
        json.dump(vitae, file, sort_keys=True, indent=4)