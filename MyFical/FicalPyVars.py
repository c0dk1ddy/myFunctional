from .func_tool import wraps

'''
# FicalPyVars.py 

## ===== imported function =====
 - wraps

## ===== LAMBDA & VARS =====

gs = global_set(varname, value) = seting var [varname] as value at global scope.
msc = make_global_class(3 argument 4 get global_set's value's value what; type-function's arguments.) = the work it has to be.
_fga = _fxgxyz(f, g, x, y, z) = f(x, g(x, y, z))

'''

gs = global_set = globals().__getitem__
_fga = _fxgxyz = lambda f, g, x, y, z : f(x, g(x, y, z))
msc = make_global_class = lambda class_name, class_s__super__, class_s__dict__value : _fga(global_set, type, class_name, class_s__super__, class_s__dict__value)

def functional_class_making_function(*this_must_empty, class_name):
    '''
    # `functional_class_making_function(*this_must_empty, class_name)`

    must use like src :
    
    ## that src

    ```
    functional_class_making_function(class_name = CLASS_NAME_STRING)(the_1st_super_class, ..., the_nth_super_class)(
        the_1st_attribute_name = the_1st_attribute_value,
        ...
        the_nth_attribute_name = the_nth_attribute_value
    )
    ```
    '''
    def _inner_function_what_super_clas_get_part(*supers):
        '''
        # `_inner_function_what_super_clas_get_part(*supers)` A return value of `functional_class_making_function(*this_must_empty, class_name)`

        ## how 2 work?
        
        it works because of it returns that `_inner_function_what_a__dict__argument_get_part`
        '''
        def _inner_function_what_a__dict__argument_get_part(**value):
            '''
            # `_inner_function_what_a__dict__argument_get_part(**value)` A return value of `_inner_function_what_super_clas_get_part(*supers)`

            ## how 2 work?
            
             > because it returns `msc(class_name, supers, value)`
            '''
            msc(class_name, supers, value)
        return _inner_function_what_a__dict__argument_get_part
    return _inner_function_what_super_clas_get_part

def fcmf(c = None):
    '''
    # `fcmf(c = None)` == `functional_class_making_function(class_name = c)`
    '''
    return functional_class_making_function(class_name = c)
