from collections.abc import Iterable 
import json
import os
import sys
import getpass

from group import Group
from user import User


class Melonpan:      
    def __init__ (self, setupfile=None):
        self.username = getpass.getuser()
        self.groups = {}
        self.load_setup(setupfile)
        self.parse_setup()
        self.load_user_settings()

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
                self.usergroup = settings
                self.users = self.create_users(settings)
            
    def load_setup(self, setupfile):
        if not setupfile:
            libdir = os.path.dirname(__file__)
            setupfile = os.path.join(libdir, 'melonsetup.json')
        try:            
            with open(setupfile, 'r') as f:
                self.setup = json.load(f)
        except:
            sys.exit(f"Error loading setup file: {setupfile}")

    def load_user_settings(self):
        group = self.get_current_group_obj()
        self.attribs = group.attribs
        for name in self.attribs:       
            setattr(self, name, getattr(group, name))

    def get_current_group_name(self):
        try:
            self.groups[self.users[self.username].group]
            group_name = self.users[self.username].group
        except:
            group_name = 'prod'
        return group_name 

    def get_current_group_obj(self):
        group_name = self.get_current_group_name()
        return self.groups[group_name]

    def get_userlist(self):
        return list(self.users.keys())

    def show(self):
        print(f"usuario: {self.username}")
        print(f"grupo: {self.get_current_group_name()}")
        print(f"{self.attribs}")


def main():
    melon = Melonpan()
    print(melon.db)
    melon.show()
    #print(melon.users["narumi"].group)
    #print(melon.groups["dev"].db)
    
if __name__ == "__main__":
    main()

