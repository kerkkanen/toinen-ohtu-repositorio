from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        tomls = toml.loads(content, _dict=dict)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(tomls['tool']['poetry']['name'], tomls['tool']['poetry']['description'], tomls['tool']['poetry']['dependencies'], tomls['tool']['poetry']['dev-dependencies'])
