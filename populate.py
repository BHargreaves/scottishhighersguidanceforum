import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScottishHighersGuidanceForum.settings')

import django
django.setup()

from higherguidanceforum.models import Subject, Link



def populate():

    #Each subject needs to have a link to its subject page on the SQA
    account_links = [ {"title": "SQA Higher Accounting Resources", "url": "https://www.sqa.org.uk/sqa/47917.html", "views":0},
                    {"title": "SQA Higher Accounting Course Specification", "url": "https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_Accounting.pdf", "views":0}]

    admin_it_links = [ {"title": "SQA Higher Administration & IT Resources", "url":"https://www.sqa.org.uk/sqa/47918.html", "views":0},
                     {"title": "SQA Higher Administration & IT Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_AdministrationandIT.pdf", "views":0}]

    art_design_links = [ {"title": "SQA Higher Art & Design Resources", "url":"https://www.sqa.org.uk/sqa/47892.html", "views":0},
                       {"title": "SQA Higher Art & Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_ExpressiveArts_ArtandDesign.pdf", "views":0}]

    biology_links = [ {"title": "SQA Higher Biology Resources", "url":"https://www.sqa.org.uk/sqa/47912.html", "views":0},
                    {"title": "SQA Higher Biology Specification", "url":"https://www.sqa.org.uk/files/nq/CourseSpecHBiology15_16.pdf", "views":0}]

    bus_man_links = [ {"title": "SQA Higher Business Management Resources", "url":"https://www.sqa.org.uk/sqa/47919.html", "views":0 },
                    {"title": "SQA Higher Business Management Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_BusinessManagement.pdf", "views":0}]

    care_links = [ {"title": "SQA Higher Care Resources", "url":"https://www.sqa.org.uk/sqa/47897.html", "views":0 },
                 {"title": "SQA Higher Specifiation", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_HealthandWellbeing_Care.pdf", "views":0}]

    cantonese_links = [ {"title": "SQA Higher Cantonese Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                      {"title": "SQA Higher Cantonese Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]

    chemistry_links = [ {"title": "SQA Higher Chemistry Resources", "url":"https://www.sqa.org.uk/sqa/47913.html", "views":0},
                      {"title": "SQA Higher Chemistry Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Sciences_Chemistry.pdf", "views":0}]

    child_dev_links = [ {"title": "SQA Higher Childcare & Development Resources", "url":"https://www.sqa.org.uk/sqa/47898.html", "views":0},
                      {"title": "SQA Higher Childcare & Development Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_HealthandWellbeing_ChildcareandDevelopment.pdf", "views":0}]

    classical_links = [ {"title": "SQA Higher Classical Studies Resources", "url":"https://www.sqa.org.uk/sqa/47921.html", "views":0},
                      {"title": "SQA Higher Classical Studies Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_ClassicalStudies.pdf", "views":0}]

    comp_sci_links = [ {"title":"SQA Higher Computing Science Resources", "url":"https://www.sqa.org.uk/sqa/56924.html", "views":0},
                     {"title":"SQA Higher Computing Science Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Technologies_ComputingScience.pdf", "views":0}]

    dance_links = [{"title":"SQA Higher Dance Resources", "url":"https://www.sqa.org.uk/sqa/47893.html", "views":0},
                    {"title":"SQA Higher Dance Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_ExpressiveArts_Dance.pdf", "views":0}]

    design_man_links = [{"title":"SQA Higher Design & Manufacture Resources", "url":"https://www.sqa.org.uk/sqa/47927.html", "views":0},
                        {"title":"SQA Higher Design & Manufacture Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Technologies_DesignandManufacture.pdf", "views":0}]

    drama_links = [{"title":"SQA Higher Drama Resources", "url":"https://www.sqa.org.uk/sqa/47894.html", "views":0},
                    {"title":"SQA Higher Drama Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_ExpressiveArts_Drama.pdf", "views":0}]

    esol_links = [{"title":"SQA Higher ESOL Resources", "url":"https://www.sqa.org.uk/sqa/47905.html", "views":0},
                    {"title":"SQA Higher ESOL Spcification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Languages_ESOL.pdf", "views":0}]

    economics_links = [{"title":"SQA Higher Economics Resources", "url":"https://www.sqa.org.uk/sqa/47920.html", "views":0},
                        {"title":"SQA Higher Economics Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_Economics.pdf", "views":0}]

    engineering_links = [{"title":"SQA Higher Engineering Science Resources", "url":"https://www.sqa.org.uk/sqa/47928.html", "views":0},
                        {"title":"SQA Higher Engineering Science Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Technologies_EngineeringScience.pdf", "views":0}]

    english_links = [{"title":"SQA Higher English Resources", "url":"https://www.sqa.org.uk/sqa/47904.html", "views":0},
                    {"title":"SQA Higher English Specification", "url":"https://www.sqa.org.uk/sqa/files_ccc/CourseSpecHEnglish.pdf", "views":0}]

    enviro_sci_links = [{"title":"SQA Higher Environmental Science Resources", "url":"https://www.sqa.org.uk/sqa/47914.html", "views":0},
                        {"title":"SQA Higher Environmental Science Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Sciences_EnvironmentalScience.pdf", "views":0}]


    fashion_textile_links = [{"title":"SQA Higher Fashion & Textile Technology Resources", "url":"https://www.sqa.org.uk/sqa/56940.html", "views":0},
                            {"title":"SQA Higher Fashion & Textile Technology Specification", "url":"https://www.sqa.org.uk/files/nq/CourseSpecHFashionTextileTech15_16.pdf", "views":0}]

    french_links = [ {"title": "SQA Higher French Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                   {"title": "SQA Higher French Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]

    gaelic_links = [{"title": "SQA Higher Gaelic (Learners) Resources", "url":"https://www.sqa.org.uk/sqa/56916.html", "views":0},
                    {"title": "SQA Higher Gaelic (Learners) Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpec_Higher_Languages_GaelicLearners.pdf", "views":0}]

    gaidhlig_links = [{"title": "SQA Higher Gaidhlig Resources", "url":"https://www.sqa.org.uk/sqa/45675.html", "views":0},
                    {"title": "SQA Higher Gaidhlig Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Languages_Gaidhlig.pdf", "views":0}]

    german_links = [ {"title": "SQA Higher German Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                   {"title": "SQA Higher German Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]

    geography_links = [{"title":"SQA Higher Geography Resources", "url":"https://www.sqa.org.uk/sqa/47922.html", "views":0},
                        {"title":"SQA Higher Geography Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_SocialStudies_Geography.pdf", "views":0}]

    graph_comm_links = [{"title":"SQA Higher Graphic Communication Resources", "url":"https://www.sqa.org.uk/sqa/47929.html", "views":0},
                        {"title":"SQA Higher Graphic Communication Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Technologies_GraphicCommunication.pdf", "views":0}]

    health_food_tech_links = [{"title":"SQA Higher Health & Food Technology Resources", "url":"https://www.sqa.org.uk/sqa/47899.html", "views":0},
                            {"title":"SQA Higher Health & Food Technology Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_HealthandWellbeing_HealthFoodTechnology.pdf", "views":0}]

    history_links = [{"title":"SQA Higher History Resources", "url":"https://www.sqa.org.uk/sqa/47923.html", "views":0},
                    {"title":"SQA Higher History Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_History.pdf", "views":0}]

    human_bio_links = [{"title":"SQA Higher Human Biology Resources", "url":"https://www.sqa.org.uk/sqa/47915.html", "views":0},
                        {"title":"SQA Higher Human Biology Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Sciences_HumanBiology.pdf", "views":0}]

    italian_links = [ {"title": "SQA Higher Italian Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                    {"title": "SQA Higher Italian Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]

    latin_links = [{"title":"SQA Higher Latin Resources", "url":"https://www.sqa.org.uk/sqa/47907.html", "views":0},
                    {"title":"SQA Higher Latin Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Languages_Latin.pdf", "views":0}]

    mandarin_links = [ {"title": "SQA Higher Mandarin Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                     {"title": "SQA Higher Mandarin Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]

    maths_links = [{"title":"SQA Higher Mathematics Resources", "url":"https://www.sqa.org.uk/sqa/47910.html", "views":0},
                    {"title":"SQA Higher Mathematics Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_Mathematics_Mathematics.pdf", "views":0}]

    media_links = [{"title":"SQA Higher Media Resources", "url":"https://www.sqa.org.uk/sqa/47908.html", "views":0},
                    {"title":"SQA Higher Media Specification", "url":"https://www.sqa.org.uk/files/nq/CourseSpecHMedia15_16.pdf", "views":0}]

    mod_studies_links = [{"title":"SQA Higher Modern Studies Resources", "url":"https://www.sqa.org.uk/sqa/47924.html", "views":0},
                        {"title":"SQA Higher Modern Studies Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_SocialStudies_ModernStudies.pdf", "views":0}]

    music_links = [{"title":"SQA Higher Music Resources", "url":"https://www.sqa.org.uk/sqa/47895.html", "views":0},
                    {"title":"SQA Higher Music Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_ExpressiveArts_Music.pdf", "views":0}]

    music_tech_links = [{"title": "SQA Higher Music Technology Resources", "url":"https://www.sqa.org.uk/sqa/56951.html", "views":0},
                        {"title": "SQA Higher Music Technology Specification", "url":"https://www.sqa.org.uk/files/nq/CourseSpecHMusicTech15_16.pdf", "views":0}]

    philosophy_links = [{"title": "SQA Higher Philosophy Resources", "url":"https://www.sqa.org.uk/sqa/47900.html", "views":0},
                        {"title": "SQA Higher Philosophy Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_HealthandWellbeing_Philosophy.pdf", "views":0}]

    photo_links = [{"title":"SQA Higher Photography Resources", "url":"https://www.sqa.org.uk/sqa/47896.html", "views":0},
                    {"title":"SQA Higher Photography Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_ExpressiveArts_Photography.pdf", "views":0}]

    pe_links = [{"title":"SQA Higher Physical Education Resources", "url":"https://www.sqa.org.uk/sqa/47901.html", "views":0},
                {"title":"SQA Higher Physical Education Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_HealthandWellbeing_PhysicalEducation.pdf", "views":0}]

    physics_links = [{"title":"SQA Higher Physics Resources", "url":"https://www.sqa.org.uk/sqa/47916.html", "views":0},
                    {"title":"SQA Higher Physics Specification", "url":"https://www.sqa.org.uk/files/nq/CourseSpecHPhysics15_16.pdf", "views":0}]

    politics_links = [{"title":"SQA Higher Politics Resources", "url":"https://www.sqa.org.uk/sqa/47925.html", "views":0},
                    {"title":"SQA Higher Politics Specification", "url":"http://www.sqa.org.uk/files/nq/CourseSpecHPolitics15_16.pdf", "views":0}]

    psych_links = [{"title":"SQA Higher Psychology Resources", "url":"https://www.sqa.org.uk/sqa/47902.html", "views":0},
                    {"title":"SQA Higher Psychology Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_HealthandWellbeing_Psychology.pdf", "views":0}]

    rmps_links = [{"title":"SQA Higher Religious, Moral & Philosophical Studies Resources","url":"https://www.sqa.org.uk/sqa/47911.html", "views":0},
                {"title":"SQA Higher Religious, Moral & Philosophical Studies Specification","url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_RMPS_ReligiousMoralandPhilosophicalStudies.pdf", "views":0}]

    sociology_links = [{"title":"SQA Higher Sociology Resources", "url":"https://www.sqa.org.uk/sqa/47903.html", "views":0},
                        {"title":"SQA Higher Sociology Specification", "url":"https://www.sqa.org.uk/files/nq/CfE_CourseSpecification_Higher_HealthandWellbeing_Sociology.pdf", "views":0}]

    spanish_links = [ {"title": "SQA Higher Spanish Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                    {"title": "SQA Higher Spanish Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]

    urdu_links = [ {"title": "SQA Higher Urdu Resources", "url":"https://www.sqa.org.uk/sqa/47909.html", "views":0},
                 {"title": "SQA Higher Urdu Specification", "url":"https://www.sqa.org.uk/files_ccc/CfE_CourseSpecification_Higher_Languages_ModernLanguages.pdf", "views":0}]


    #Name each Subject, and point it to their links
    subs = { "Accounting": {"links": account_links, "questions":None}, "Administration & IT": {"links": admin_it_links, "questions":None},
            "Art & Design": {"links": art_design_links, "questions":None}, "Biology": {"links": biology_links, "questions":None},
            "Business Management": {"links":bus_man_links, "questions":None}, "Care": {"links":care_links, "questions":None},
            "Cantonese":{"links":cantonese_links, "questions":None}, "Chemistry":{"links":chemistry_links, "questions":None},
            "Childcare & Development":{"links":child_dev_links, "questions":None},
            "Classical Studies":{"links":classical_links, "questions":None}, "Computing Science":{"links":comp_sci_links, "questions":None},
            "Dance":{"links":dance_links, "questions":None}, "Design & Manufacture":{"links":design_man_links, "questions":None},
            "Drama":{"links":drama_links, "questions":None}, "ESOL":{"links":esol_links, "questions":None},
            "Economics":{"links":economics_links, "questions":None}, "Engineering Science":{"links":engineering_links, "questions":None},
            "English":{"links":english_links, "questions":None}, "Enviromental Science":{"links":enviro_sci_links, "questions":None},
            "Fashion & Textile Technology":{"links":fashion_textile_links, "questions":None},
            "French":{"links":french_links, "questions":None}, "Gaelic (Leaners)":{"links":gaelic_links, "questions":None},
            "Gaidhlig":{"links":gaidhlig_links, "questions":None}, "German":{"links":german_links, "questions":None},
            "Geography":{"links":geography_links, "questions":None}, "Graphic Communication":{"links":graph_comm_links, "questions":None},
            "Health & Food Technology":{"links":health_food_tech_links, "questions":None},
            "History":{"links":history_links, "questions":None}, "Human Biology":{"links":human_bio_links, "questions":None},
            "Italian":{"links":italian_links, "questions":None}, "Latin":{"links":latin_links, "questions":None},
            "Mandarin":{"links":mandarin_links, "questions":None}, "Mathematics":{"links":maths_links, "questions":None},
            "Media":{"links":media_links, "questions":None}, "Modern Studies":{"links":mod_studies_links, "questions":None},
            "Music":{"links":music_links, "questions":None}, "Music Technology":{"links":music_tech_links, "questions":None},
            "Philosophy":{"links":philosophy_links, "questions":None}, "Photography":{"links":photo_links, "questions":None},
            "Physical Education":{"links":pe_links, "questions":None}, "Physics":{"links":physics_links, "questions":None},
            "Politics":{"links":politics_links, "questions":None}, "Psychology":{"links":psych_links, "questions":None},
            "Religious, Moral & Philosophical Studies":{"links":rmps_links, "questions":None},
            "Sociology":{"links":sociology_links, "questions":None}, "Spanish":{"links":spanish_links, "questions":None},
            "Urdu":{"links":urdu_links, "questions":None},
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