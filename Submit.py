import os
import os.path as path
import pygit2
import shutil
import random

class UtilFunctions:

    absPath = path.abspath(".")
    
    def loadConfig(self):
        '''
            Loads the file config.cof and returns a dictionary of RepoMetaData classes.
        '''
        repos = {}
        isDir = path.isdir(self.absPath + "/Config")
        if (not isDir):
            os.mkdir(self.absPath + "/Config")
        self.configFile = open(self.absPath + "/Config/config.cof")
        for line in self.configFile:
            data = line.split(":")
            repos[data[0]] = RepoMetaData(int(data[0]), data[1], data[2], data[3], data[4])
        return repos
    
    def selectRepositories(self, amount, repos):
        '''
            Selects n amount of keys at ramdom from the given dictionary.
        '''
        return random.sample(repos,amount)
    
    def initRepositories(self, repositoryIDs):
        '''
            Creates a Review folder in the current directory 
            and then creates a folder for each repository that 
            is specified in the repos dictionary.
        '''
        repositories = {}
        isDir = path.isdir(self.absPath + "/Review")
        if (not isDir):
            os.mkdir(self.absPath + "/Review")
        
        for currentID in repositoryIDs.keys():
            currentPath = self.absPath + "/Review/" + currentID
            isDir = path.isdir(currentPath)
            if (not isDir):
                os.mkdir(currentPath)
                repositories[currentID] = pygit2.clone_repository("git://"+repositoryIDs[currentID].getUrl(),currentPath)
                repositories[currentID].checkout(repositories[currentID].lookup_reference(repositoryIDs[currentID].getTag()))
            else:
                shutil.rmtree(currentPath)
                os.mkdir(currentPath)
                repositories[currentID] = pygit2.clone_repository("git://"+repositoryIDs[currentID].getUrl(),currentPath)
                repositories[currentID].checkout(repositories[currentID].lookup_reference(repositoryIDs[currentID].getTag()))

class RepoMetaData:
    IdNumber = 0 # aka student number
    Type = ""
    Url = ""
    Path = ""
    Tag = ""

    def __init__(self, IdNumber, Type, Url, Path, Tag):
        '''
            If a parameter is not in use assign the value _.
        '''
        self.IdNumber = IdNumber
        self.Type = Type
        self.Url = Url
        self.Path = Path
        if Tag == "_":
            self.Tag = "HEAD" 
        
        if (Type != 'url' and Type != 'path' ):
            raise Exception()

    def getType(self):
        '''
            Returns the Type of the repository. url, path or _.
            url if the repository is not the current computer.
            path if the repository is on the current computer.
            _ if the parameter is not used.
        '''
        return self.Type

    def getUrl(self):
        '''
            Returns the url of the repository. E.g. github.com/EvilClam/PythonCodeReview.git
        '''
        return self.Url

    def getPath(self):
        '''
            Returns the path of the local repository.
        '''
        return self.Path

    def getTag(self):
        '''
            returns the tag of the specified version.
            If tag parameter is not used the default value is HEAD.
        '''
        return self.Tag
