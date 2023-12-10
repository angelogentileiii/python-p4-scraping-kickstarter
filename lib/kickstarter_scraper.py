from bs4 import BeautifulSoup
import ipdb

## whole project selector
# kickstarter.select("li.project.grid_4")[0]

## project title selector
# project.select("h2.bbcard_name strong a")[0].text

## image selector
# project.select("div.project-thumbnail a img")[0]['src']

## description selector
# project.select("p.bbcard_blurb")[0].text

## location selector
# project.select("ul.project-meta a span.location-name")[0].text

## funding selector
# project.select("ul.project-stats li.first.funded strong")[0].text
# add .replace("%"."") to remove % sign

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()
    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        
        # selects the project title
        title = project.select("h2.bbcard_name strong a")[0].text
        
        # set a key in the dictionary to the project title
        # set the values for the title key to a dictionary of project info
        projects[title] = {
        'image_link': project.select("div.project-thumbnail a img")[0]["src"],
        'description': project.select("p.bbcard_blurb")[0].text,
        'location': project.select("ul.project-meta span.location-name")[0].text,
        'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
        }

    ipdb.set_trace()
   

    # return the projects dictionary
    return projects

projects = create_project_dict()
print(projects)
