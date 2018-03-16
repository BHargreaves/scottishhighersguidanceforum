import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScottishHighersGuidanceForum.settings')

import django
django.setup()

from higherguidanceforum.models import Subject, Link

def populate():

    #Each subject needs to have a link to its subject page on the SQA
    account_links = [ {"title": "SQA Higher Accounting Resources", "url": "https://www.sqa.org.uk/sqa/47917.html", "views":0} ]
    admin_it_links = [ {"title": "SQA Higher Administration & IT Resources", "url":"https://www.sqa.org.uk/sqa/47918.html", "views":0}]
    art_design_links = [ {"title": "SQA Higher Art & Design Resources", "url":"https://www.sqa.org.uk/sqa/47892.html", "views":0}]
    biology_links = [ {"title": "SQA Higher Biology Resources", "url":"https://www.sqa.org.uk/sqa/47912.html", "views":0}]
    bus_man_links = [ {"title": "SQA Higher Business Management Resources", "url":"https://www.sqa.org.uk/sqa/47919.html", "views":0 }]
    care_links = [ {"title": "SQA Higher Care Resources", "url":"https://www.sqa.org.uk/sqa/47897.html", "views":0 }]
    cantonese_links = [ {"title": "SQA Higher Cantonese Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]
    chemistry_links = [ {"title": "SQA Higher Chemistry Resources", "url":"https://www.sqa.org.uk/sqa/47913.html", "views":0}]
    child_dev_links = [ {"title": "SQA Higher Childcare & Development Resources", "url":"https://www.sqa.org.uk/sqa/47898.html", "views":0}]
    classical_links = [ {"title": "SQA Higher Classical Studies Resources", "url":"https://www.sqa.org.uk/sqa/47921.html", "views":0}]
    comp_sci_links = [{"title":"SQA Higher Computing Science Resources", "url":"https://www.sqa.org.uk/sqa/56924.html", "views":0}]
    dance_links = [{"title":"SQA Higher Dance Resources", "url":"https://www.sqa.org.uk/sqa/47893.html", "views":0}]
    design_man_links = [{"title":"SQA Higher Design & Manufacture Resources", "url":"https://www.sqa.org.uk/sqa/47927.html", "views":0}]
    drama_links = [{"title":"SQA Higher Drama Resources", "url":"https://www.sqa.org.uk/sqa/47894.html", "views":0}]
    esol_links = [{"title":"SQA Higher ESOL Resources", "url":"https://www.sqa.org.uk/sqa/47905.html", "views":0}]
    economics_links = [{"title":"SQA Higher Economics Resources", "url":"https://www.sqa.org.uk/sqa/47920.html", "views":0}]
    engineering_links = [{"title":"SQA Higher Engineering Science Resources", "url":"https://www.sqa.org.uk/sqa/47928.html", "views":0}]
    english_links = [{"title":"SQA Higher English Resources", "url":"https://www.sqa.org.uk/sqa/47904.html", "views":0}]
    enviro_sci_links = [{"title":"SQA Higher Environmental Science Resources", "url":"https://www.sqa.org.uk/sqa/47914.html", "views":0}]
    fashion_textile_links = [{"title":"SQA Higher Fashion & Textile Technology Resources", "url":"https://www.sqa.org.uk/sqa/56940.html", "views":0}]
    french_links = [ {"title": "SQA Higher French Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]
    gaelic_links = [{"title": "SQA Higher Gaelic (Learners) Resources", "url":"https://www.sqa.org.uk/sqa/56916.html", "views":0}]
    gaidhlig_links = [{"title": "SQA Higher Gaidhlig Resources", "url":"https://www.sqa.org.uk/sqa/45675.html", "views":0}]
    german_links = [ {"title": "SQA Higher German Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]
    geography_links = [{"title":"SQA Higher Geography Resources", "url":"https://www.sqa.org.uk/sqa/47922.html", "views":0}]
    graph_comm_links = [{"title":"SQA Higher Graphic Communication Resources", "url":"https://www.sqa.org.uk/sqa/47929.html", "views":0}]
    health_food_tech_links = [{"title":"SQA Higher Health & Food Technology Resources", "url":"https://www.sqa.org.uk/sqa/47899.html", "views":0}]
    history_links = [{"title":"SQA Higher History Resources", "url":"https://www.sqa.org.uk/sqa/47923.html", "views":0}]
    human_bio_links = [{"title":"SQA Higher Human Biology Resources", "url":"https://www.sqa.org.uk/sqa/47915.html", "views":0}]
    italian_links = [ {"title": "SQA Higher Italian Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]
    latin_links = [{"title":"SQA Higher Latin Resources", "url":"https://www.sqa.org.uk/sqa/47907.html", "views":0}]
    mandarin_links = [ {"title": "SQA Higher Mandarin Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]
    maths_links = [{"title":"SQA Higher Mathematics Resources", "url":"https://www.sqa.org.uk/sqa/47910.html", "views":0}]
    media_links = [{"title":"SQA Higher Media Resources", "url":"https://www.sqa.org.uk/sqa/47908.html", "views":0}]
    mod_studies_links = [{"title":"SQA Higher Modern Studies Resources", "url":"https://www.sqa.org.uk/sqa/47924.html", "views":0}]
    music_links = [{"title":"SQA Higher Music Resources", "url":"https://www.sqa.org.uk/sqa/47895.html", "views":0}]
    music_tech_links = [{"title": "SQA Higher Music Technology Resources", "url":"https://www.sqa.org.uk/sqa/56951.html", "views":0}]
    philosophy_links = [{"title": "SQA Higher Philosophy Resources", "url":"https://www.sqa.org.uk/sqa/47900.html", "views":0}]
    photo_links = [{"title":"SQA Higher Photography Resources", "url":"https://www.sqa.org.uk/sqa/47896.html", "views":0}]
    pe_links = [{"title":"SQA Higher Physical Education Resources", "url":"https://www.sqa.org.uk/sqa/47901.html", "views":0}]
    physics_links = [{"title":"SQA Higher Physics Resources", "url":"https://www.sqa.org.uk/sqa/47916.html", "views":0}]
    politics_links = [{"title":"SQA Higher Politics Resources", "url":"https://www.sqa.org.uk/sqa/47925.html", "views":0}]
    psych_links = [{"title":"SQA Higher Psychology Resources", "url":"https://www.sqa.org.uk/sqa/47902.html", "views":0}]
    rmps_links = [{"title":"SQA Higher Religious, Moral & Philosophical Studies Resources","url":"https://www.sqa.org.uk/sqa/47911.html", "views":0}]
    sociology_links = [{"title":"SQA Higher Sociology Resources", "url":"https://www.sqa.org.uk/sqa/47903.html", "views":0}]
    spanish_links = [ {"title": "SQA Higher Spanish Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]
    urdu_links = [ {"title": "SQA Higher Urdu Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0}]


    #Name each Subject, and point it to their links
    subs = { "Accounting": {"links": account_links }, "Administration & IT": {"links": admin_it_links},
            "Art & Design": {"links": art_design_links}, "Biology": {"links": biology_links},
            "Business Management": {"links":bus_man_links}, "Care": {"links":care_links},
            "Cantonese":{"links":cantonese_links}, "Chemistry":{"links":chemistry_links},
            "Childcare & Development":{"links":child_dev_links},
            "Classical Studies":{"links":classical_links}, "Computing Science":{"links":comp_sci_links},
            "Dance":{"links":dance_links}, "Design & Manufacture":{"links":design_man_links},
            "Drama":{"links":drama_links}, "ESOL":{"links":esol_links},
            "Economics":{"links":economics_links}, "Engineering Science":{"links":engineering_links},
            "English":{"links":english_links}, "Enviromental Science":{"links":enviro_sci_links},
            "Fashion & Textile Technology":{"links":fashion_textile_links},
            "French":{"links":french_links}, "Gaelic (Leaners)":{"links":gaelic_links},
            "Gaidhlig":{"links":gaidhlig_links}, "German":{"links":german_links},
            "Geography":{"links":geography_links}, "Graphic Communication":{"links":graph_comm_links},
            "Health & Food Technology":{"links":health_food_tech_links},
            "History":{"links":history_links}, "Human Biology":{"links":human_bio_links},
            "Italian":{"links":italian_links}, "Latin":{"links":latin_links},
            "Mandarin":{"links":mandarin_links}, "Mathematics":{"links":maths_links},
            "Media":{"links":media_links}, "Modern Studies":{"links":mod_studies_links},
            "Music":{"links":music_links}, "Music Technology":{"links":music_tech_links},
            "Philosophy":{"links":philosophy_links}, "Photography":{"links":photo_links},
            "Physical Education":{"links":pe_links}, "Physics":{"links":physics_links},
            "Politics":{"links":politics_links}, "Psychology":{"links":psych_links},
            "Relgious, Moral & Philosophical Studies":{"links":rmps_links},
            "Sociology":{"links":sociology_links}, "Spanish":{"links":spanish_links},
            "Urdu":{"links":urdu_links},
        }

    for sub, sub_data in subs.items():

        s = add_sub(sub)

        for l in sub_data["links"]:

            add_link(s, l["title"], l["url"], l["views"] )


    #Print out the categories added
    for s in Subject.objects.all():
            for l in Link.objects.filter(category=s):
                print("- {0} - {1}".format(str(s), str(l)))

def add_link(sub, title, url, views):
    l = Link.objects.get_or_create(category=sub, title=title)[0]
    l.url = url
    l.views = views
    l.save()
    return l


def add_sub(name):
    s = Subject.objects.get_or_create(name=name)[0]
    s.save()
    return s


if __name__ == '__main__':
    print("Starting population script...")
    populate()