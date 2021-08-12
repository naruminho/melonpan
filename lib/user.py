class User:
    def validate_group(self, usergroup, groups):
        if not usergroup in groups:            
            sys.exit(f"{usergroup} is not a valid group.")

    def __init__ (self, username, usergroup, groups):
        self.validate_group(usergroup, groups)
        self.group = usergroup


