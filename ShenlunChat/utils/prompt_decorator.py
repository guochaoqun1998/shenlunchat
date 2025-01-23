#@Author: guochaoqun  
#@Date: 2024-07-25 23:07:35  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-25 23:07:35 

def get_docstring(func):
    def wrapper(*args,**kwargs):
        lines = func.__doc__.splitlines()
        # Remove leading spaces and end spaces
        lines = [line.strip() for line in lines if line.strip() != '']
        return "\n".join(lines)
    wrapper.is_prompt_doc = True
    wrapper.__doc__ = func.__doc__
    return wrapper
    