import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScottishHighersGuidanceForum.settings')

import django
django.setup()

from higherguidanceforum.models import Subject, Link

def populate():

    #Each subject needs to have a link to its subject page on the SQA
    account_links = [ {"title": "SQA Higher Accounting Resources", "url": "https://www.sqa.org.uk/sqa/47917.html"} ]
    admin_it_links = [ {"title": "SQA Higher Administration & IT Resources", "url":"https://www.sqa.org.uk/sqa/47918.html"}]
    art_design_links = [ {"title": "SQA Higher Art & Design Resources", "url":"https://www.sqa.org.uk/sqa/47892.html"}]
    biology_links = [ {"title": "SQA Higher Biology Resources", "url":"https://www.sqa.org.uk/sqa/47912.html"}]
    bus_man_links = [ {"title": "SQA Higher Business Management Resources", "url":"https://www.sqa.org.uk/sqa/47919.html" }]
    care_links = [ {"title": "SQA Higher Care Resources", "url":"https://www.sqa.org.uk/sqa/47897.html" }]
    cantonese_links = [ {"title": "SQA Higher Cantonese Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]
    chemistry_links = [ {"title": "SQA Higher Chemistry Resources", "url":"https://www.sqa.org.uk/sqa/47913.html"}]
    child_dev_links = [ {"title": "SQA Higher Childcare & Development Resources", "url":"https://www.sqa.org.uk/sqa/47898.html"}]
    classical_links = [ {"title": "SQA Higher Classical Studies Resources", "url":"https://www.sqa.org.uk/sqa/47921.html"}]
    comp_sci_links = [{"title":"SQA Higher Computing Science Resources", "url":"https://www.sqa.org.uk/sqa/56924.html"}]
    dance_links = [{"title":"SQA Higher Dance Resources", "url":"https://www.sqa.org.uk/sqa/47893.html"}]
    design_man_links = [{"title":"SQA Higher Design & Manufacture Resources", "url":"https://www.sqa.org.uk/sqa/47927.html"}]
    drama_links = [{"title":"SQA Higher Drama Resources", "url":"https://www.sqa.org.uk/sqa/47894.html"}]
    esol_links = [{"title":"SQA Higher ESOL Resources", "url":"https://www.sqa.org.uk/sqa/47905.html"}]
    economics_links = [{"title":"SQA Higher Economics Resources", "url":"https://www.sqa.org.uk/sqa/47920.html"}]
    engineering_links = [{"title":"SQA Higher Engineering Science Resources", "url":"https://www.sqa.org.uk/sqa/47928.html"}]
    english_links = [{"title":"SQA Higher English Resources", "url":"https://www.sqa.org.uk/sqa/47904.html"}]
    enviro_sci_links = [{"title":"SQA Higher Environmental Science Resources", "url":"https://www.sqa.org.uk/sqa/47914.html"}]
    fashion_textile_links = [{"title":"SQA Higher Fashion & Textile Technology Resources", "url":"https://www.sqa.org.uk/sqa/56940.html"}]
    french_links = [ {"title": "SQA Higher French Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]
    gaelic_links = [{"title": "SQA Higher Gaelic (Learners) Resources", "url":"https://www.sqa.org.uk/sqa/56916.html"}]
    gaidhlig_links = [{"title": "SQA Higher Gàidhlig Resources", "url":"https://www.sqa.org.uk/sqa/45675.html"}]
    german_links = [ {"title": "SQA Higher German Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]
    geography_links = [{"title":"SQA Higher Geography Resources", "url":"https://www.sqa.org.uk/sqa/47922.html"}]
    graph_comm_links = [{"title":"SQA Higher Graphic Communication Resources", "url":"https://www.sqa.org.uk/sqa/47929.html"}]
    health_food_tech_links = [{"title":"SQA Higher Health & Food Technology Resources", "url":"https://www.sqa.org.uk/sqa/47899.html"}]
    history_links = [{"title":"SQA Higher History Resources", "url":"https://www.sqa.org.uk/sqa/47923.html"}]
    human_bio_links = [{"title":"SQA Higher Human Biology Resources", "url":"https://www.sqa.org.uk/sqa/47915.html"}]
    italian_links = [ {"title": "SQA Higher Italian Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]
    latin_links = [{"title":"SQA Higher Latin Resources", "url":"https://www.sqa.org.uk/sqa/47907.html"}]
    mandarin_links = [ {"title": "SQA Higher Mandarin Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]
    maths_links = [{"title":"SQA Higher Mathematics Resources", "url":"https://www.sqa.org.uk/sqa/47910.html"}]
    media_links = [{"title":"SQA Higher Media Resources", "url":"https://www.sqa.org.uk/sqa/47908.html"}]
    mod_studies_links = [{"title":"SQA Higher Modern Studies Resources", "url":"https://www.sqa.org.uk/sqa/47924.html"}]
    music_links = [{"title":"SQA Higher Music Resources", "url":"https://www.sqa.org.uk/sqa/47895.html"}]
    music_tech_links = [{"title": "SQA Higher Music Technology Resources", "url":"https://www.sqa.org.uk/sqa/56951.html"}]
    philosophy_links = [{"title": "SQA Higher Philosophy Resources", "url":"https://www.sqa.org.uk/sqa/47900.html"}]
    photo_links = [{"title":"SQA Higher Photography Resources", "url":"https://www.sqa.org.uk/sqa/47896.html"}]
    pe_links = [{"title":"SQA Higher Physical Education Resources", "url":"https://www.sqa.org.uk/sqa/47901.html"}]
    physics_links = [{"title":"SQA Higher Physics Resources", "url":"https://www.sqa.org.uk/sqa/47916.html"}]
    politics_links = [{"title":"SQA Higher Politics Resources", "url":"https://www.sqa.org.uk/sqa/47925.html"}]
    psych_links = [{"title":"SQA Higher Psychology Resources", "url":"https://www.sqa.org.uk/sqa/47902.html"}]
    rmps_links = [{"title":"SQA Higher Religious, Moral & Philosophical Studies Resources","url":"https://www.sqa.org.uk/sqa/47911.html"}]
    sociology_links = [{"title":"SQA Higher Sociology Resources", "url":"https://www.sqa.org.uk/sqa/47903.html"}]
    spanish_links = [ {"title": "SQA Higher Spanish Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]
    urdu_links = [ {"title": "SQA Higher Urdu Resources", "url":"https://www.sqa.org.uk/sqa/47909.html"}]


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
            "Gàidhlig":{"links":gaidhlig_links}, "German":{"links":german_links},
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
            "Relgious, Moral & Philosophical Studies":{"link":rmps_links},
            "Sociology":{"links":sociology_links}, "Spanish":{"links":spanish_links},
            "Urdu":{"links":urdu_links},
        }

    for sub, sub_data in subs.item():

        s = add_sub(sub)

        for l in sub_data["links"]:
            add_link(s, l["title"], l["url"]


    #Print the categories added to the command line
    for s in Subject.objects.all():
        for l in Links.objects.filter(Subject=s):
            print("- {0} - {1}".format(str(s), str(l)))


def add_link(sub, title, url, views):
    l = Link.objects.get_or_create(subject=sub, title=title)[0]
    l.url - url
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