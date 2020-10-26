"""##### EXCEPTIONS AND ERRORS #####"""
######################################
"""
Define the error of empty content
"""
class EmptySelection(Exception):
    def __init__(self,message):
        super().__init__(self.message)