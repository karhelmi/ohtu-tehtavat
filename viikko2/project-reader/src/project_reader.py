from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)
        name1 = parsed_content["tool"]["poetry"]["name"]
        description1 = parsed_content["tool"]["poetry"]["description"]
        dependencies1 = parsed_content["tool"]["poetry"]["dependencies"]
        list_dependencies1 = []
        for dep in dependencies1:
            list_dependencies1.append(dep)
        dev_dependencies1 = parsed_content["tool"]["poetry"]["dev-dependencies"]
        list_dev_dependencies1 = []
        for devdep in dev_dependencies1:
            list_dev_dependencies1.append(devdep)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name1, description1, list_dependencies1, dev_dependencies1)
