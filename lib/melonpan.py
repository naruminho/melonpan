from collections.abc import Iterable 
import json
import os
import sys
import getpass

from group import Group
from user import User


class Melonpan:      
    def get_groups(self):
        return list(self.groups.keys())

    def create_group(self, settings):
        group = Group(settings)
        return group

    def create_users(self, settings):
        users = {}        
        for user, group in settings.items():
            users[user] = User(user, group, self.get_groups())
        return users

    def parse_setup (self):
        self.groups = {}
        self.users = {}
        for key, settings in self.setup.items():
            if key != 'users':
                self.groups[key] = self.create_group(settings)
            else:
                self.users = self.create_users(settings)
            
    def load_setup(self):
        libdir = os.path.dirname(__file__)
        setupfile = os.path.join(libdir, 'setup.json')
        try:            
            with open(setupfile, 'r') as f:
                self.setup = json.load(f)
        except:
            sys.exit(f"Error loading setup file: {setupfile}")

    def load_user_settings(self):
        try:
            group = self.groups[self.users[self.username].group]
        except:
            group = self.groups['prod'] # testar
        for name in group.attribs:            
            setattr(self, name, getattr(group, name))

    def __init__ (self):
        self.username = getpass.getuser()
        self.groups = {}
        self.load_setup()
        self.parse_setup()
        self.load_user_settings()

def main():
    melon = Melonpan()
    print(melon.db)
    #print(melon.users["narumi"].group)
    #print(melon.groups["dev"].db)
    
if __name__ == "__main__":
    main()

