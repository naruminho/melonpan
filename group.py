class Group:
    """
    group class
    """
    def __init__ (self, settings):
        self.attribs = []
        for name, value in settings.items():
            self.attribs.append(name)
            setattr(self, name, value)