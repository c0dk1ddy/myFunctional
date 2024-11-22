from .akakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakakak import *
from .func_tool import wraps
from .FicalPyVars import gs, global_set, msc, make_global_class, functional_class_making_function
from .only_fcmf import fcmf
from .theRye import catcher as catcher_in_theRye
from .theRye import asserter_deco, ad, mfn, mlbs_fake_namespace, mlbs, meaning_less_block_syntaxer, catcher, c_, docset, iti, is_type_is, context_manager

'''
## ===== imported resource =====

 - catcher_in_theRye
 - asserter_deco
 - ad
 - mfn
 - mlbs_fake_namespace
 - mlbs
 - meaning_less_block_syntaxer
 - catcher
 - c_
 - docset
 - iti
 - is_type_is
 - wraps
 - context_manager
 - fcmf
 - gs
 - global_set
 - msc
 - make_global_class
 - functional_class_making_function
 - akargver

## ===== LAMBDA & VAR FIELD =====

BoolyParker(x) = int(bool(x))
'''

fcmf("AssertionalTypeError")(TypeError)(
        #pass
)

def akargv_wide(func):
    '''
    # `@akargv_wide`
    > ```
    >  def func(argv):
    >      pass #src
    > ```
    > func's argv is akargver(*argv, **kargv)
    '''
    @wraps(func)
    def deco(*argv, **kargv):
        return func(akargver(*argv, **kargv))
    return deco

@asserter_deco(AssertionalTypeError, throws = True)()
def raiseAssertionalTypeError(err):
    '''
    nisiiwis(name is shows it, it works it should)
    '''
    raise AssertionalTypeError(str(err))

@akargv_wide
def aktlqkf(argv):
    '''
    akargv_wide raiseAssertionalTypeError function
    '''
    return raiseAssertionalTypeError(argv)

def forloop(loop_func):
    @wraps(loop_func)
    def loop(*arr):
        #with aktlqkf(arr, "arr is empty. check it first bro. to fast time-management") as msg:
        #    assert *msg
        #Not Not Use tlqkf!!!!!!!!!!! tlqkf alclsshadk vlfdydjqtsmseo dho dho zheldgka!!!!!!!!!!
        if arr: map(loop_func, arr)

def foreach(*arr):
    '''
    # foreach(*arr)
    see details by return value!
    '''
    def deco(block):
        '''
        # deco(block) by foreach(*arr)
        return lambda what work `forloop(block)(*arr)`
        '''
        @wraps(block)
        def wrapper():
            forloop(block)(*arr)
        return wrapper
    return deco

def forin(*arr):
    '''
    # forin(*arr)
    see details by return value!
    '''
    def deco(block):
        '''
        # deco(block) by forin(*arr)
        ACTUALLY) foreach(*arr)(block)()
        '''
        foreach(*arr)(block)()
    return deco

def crazy():
    '''
    infinity loop iterater by yield
    '''
    yield
    yield from crazy()

fcmf("CRAZY")()(
        __next__ = lambda self : 
)

BoolyParker = lambda x : int(bool(x))

@akargver
def fake_as_style_namespace(argv):
    '''
    # fake_as_style_namespace(namespace_name, suggest be empty, kargv namespace var field)

    ## acesss by NAMESP_as_VARNAME
    '''
    map(lambda kv :gs("_as_".join(argv[0][0], kv[0]), kv[1]), argv[1].items())
