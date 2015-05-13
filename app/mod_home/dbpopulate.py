from app import db
from app.mod_home.models import Publications, Conferences

def populate_db():

    publications = [
        {
            "title": "To Be Written",
            "authors": "Andrew Mellor",
            "date": "1st September 2014",
            "abstract": "Abstract",
            "image": "network300x300.png",
            "link": "http://www.google.com",
            "arxiv": "http://arxiv.org/"
        }
    ]
    
    conferences = [
        {
            "title": "European Conference of Complex Systems",
            "location": "Lucca, Italy",
            "date": "22nd - 26th September 2014",
            "abstract": "Major international conference and event in the area of complex systems and interdisciplinary science in general",
            "image": "eccs14.jpg",
            "link": "http://www.eccs14.eu/index.php"
        },
        {
            "title": "Complex Networks Thematic School",
            "location": "Les Houches, France",
            "date": "7th - 18th April 2014",
            "abstract": "The school aims at giving a solid fundamental background to Master and PhD students and young researchers working with or on complex networks, by introducing the main concepts and tools that are useful in this field. The school will introduce the concepts and tools of graph theory, statistical physics, statistical analysis, modeling, and visualization used in the field of complex networks.",
            "image": "leshouches.jpg",
            "link": "http://leshouches2014.weebly.com/"
        },
        {
            "title": "Big Data and Social Media Workshop",
            "location": "Edinburgh, UK",
            "date": "28th November 2013",
            "abstract": "The event brings together people in commerce, government and academia, covering technical issues (data, collection, algorithms, high performance computing) and implications for marketing, healthcare, social sciences and the study of human interaction (questions of interest, limitations, pitfalls). ",
            "image": "edinburgh.jpg",
            "link": "http://icms.org.uk/workshops/bigdata2"
        }
    ]
    
    for pub in publications:
        x = Publications(**pub)
        db.session.add(x)
    
    for conf in conferences:
        x = Conferences(**conf)
        db.session.add(x)
    
    db.session.commit()

if __name__=='__main__':
    popluate_db()
    