import xml.etree.ElementTree as ET
from lxml import etree
from fastapi import FastAPI

test = etree.parse("exam.xml")

tree = ET.parse('exam.xml')
root = tree.getroot()
doc = ET.tostring(root, encoding='utf8').decode('utf8')

app = FastAPI()


# 1 - Fonction qui affiche tous les titres des projets des differents domaines d'activités 
@app.get("/projects_title")
def get_projects_title():
    data = [title.text for title in root.iter('title')]
    return {'Projects title':data}
        
# 2 - Fonction qui affiche les differents budgets d'un domaine donné en paramètre
@app.get("/budgets/{domain_name}")
def get_budgets(domain_name:str): 
    data = [budget.text for budget in root.findall('./domain/'+domain_name+'/project/budget')]
    return {'Budgets':data}
        
# 3 - Fonction qui affiche les differents titres des projets d'un domaine donné en paramètre
@app.get("/title/{domain_name}")
def get_title(domain_name:str): 
    data = [title.text for title in test.xpath('./domain/'+domain_name+'/project/title')]
    return {'Title' : data}





      
    

   