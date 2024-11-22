from contextlib import contextmanager as context_manager
from .only_fcmf import fcmf
from .func_tool import wraps

'''
# `theRye.py`

## ===== imported_resource =====

 - context_manager
 - fcmf
 - wraps

## ===== LAMBDAS & VAR FIELD =====

`mfn = mlbs_fake_namespace = mlbs = meaning_less_block_syntaxer`
iti = is_typ_is(x, typ) = the value of "type(x) is typ"
`Nothing = None`
`ad = asserter_deco`
`c_ = catcher`
'''

iti = is_typ_is = lambda x, typ : type(x) is typ
Nothing = None

def docset(docstring : str):
    '''
    # `@docset(docstring : str)`

    ## *ACTUALLY*

    return `docset_decorater_part(func)`
    '''
    def docset_decorater_part(func):
        '''
        # `docset_decorater_part(func)` what return value of `docset(docstring : str)`
        
        ## *ACTUALLY*
        
        func.__doc__ = docstring
        '''
        func.__doc__ = docstring
        return func
    return docset_decorater_part

@context_manager
def meaning_less_block_syntaxer(*value):
    '''
    # meaning_less_block_syntaxer(*value)

    ## using example)
    ```
    with meaning_less_block_syntaxer[TupleStyleSyntax but it's actually funcion's *value] as ["THE" tuple]:
        MEANING LESS BLOCK THAT MAEDED
    ```
    '''
    yield value

mfn = mlbs_fake_namespace = mlbs = meaning_less_block_syntaxer

with mfn(   *(   "__mode __throws __func __errtyp __err".split()   )   ) as _Excepter__slots__: #>w< :p [ https://youtu.be/_rzBcGXXzuI ]
    _Excepter_PyFunction__doc__ = "see self.__doc__"
    _Excepter_method = docset(_Excepter_PyFunction__doc__)

    @_Excepter_method
    def _Excepter__init__(self, errtyp, err):
        self.__mode = None
        self.__throws = False
        self.__func = None
        self.__errtyp = errtyp
        self.__err = err
    
    @_Excepter_method
    def _Excepter__set_throws(self, *func, throws):
        if func: assert throws, "if throws then can input "
        if throws: self.__throws = func if len(func) else True

    @_Excepter_method
    def _Excepter__call__(self, *func, throws = Nothing):
        if self.__mode == None:
            self.__set_throws(*func, throws)
            if throws: self.__throws = func if len(func) else True
        elif self.__mode:
            self.__set_throws(*func, throws)
            if throws:
                self.__throws = (*self.__throws, *func) if self.__throws else func
        else:
            try:self.__func = func[0](self.__errtyp, self.__err)
            except IndexError as err: raise TypeError(f"it's a decorater. [{self}]")

    fcmf("Excepter")()(
            __slots__ = _Excepter__slots__,
            __init__ = _Excepter__init__,
            __call__ = _Excepter__call__,
            __set_throws = _Excepter__set_throws,
            is_throws = lambda self, x : x in self.__throws
    )

@context_manager
def catcher(*errtyp):
    '''
    # with catcher(*errtyp) as err-manager

    ## How2Use
    `err-manager()() #settings.`
    `if here can ErrTypValues; throws = True is be typed.`
    
    #### `@err-manager()() #settings.` err management
    
    ```
    @that deco
    def management funcion(err type):
        managements
    ```

    '''
    excepter = Excepter()
    try: yield excepter
    except (*errtyp) as err:
        try:excepter(filter((lambda typ : iti(err, typ)), errtyp)[0], err)
        except IndexError as err:
            if not excepter.is_throws("IndexError"): raise SystemError(err)

c_ = catcher

def asserter_deco(*func, throws = Nothing):
    '''
    # `asserter_deco(*func, throws = Nothing)` see return
    '''
    def asserter_deco2(*Func, Throws = Nothing):
        '''
        # `asserter_deco2(*Func, Throws = Nothing)` see return
        '''
        def asserter_deco3(ErrRaser):
            '''
            # `asserter_deco3(ErrRaser)` => `asserter_deco4(ErrRaser)`
            
            ## *ACTUALLY*
            ```
            @errman(*func, throws = throws)(*Func, throws = Throws)
            def ErrRaise(types = "ItsNotProcessing", errobj = "ItsWillInput"):
                    return ErrRaser(errobj)
            ```
            ed `with catcher(AssertionError) as errman:`
            '''
            @wraps(ErrRaser)
            @context_manager
            def asserter_deco4(ErrRaser, argv):
                with catcher(AssertionError) as errman:
                    @errman(*func, throws = throws)(*Func, throws = Throws)
                    @wraps(ErrRaser)
                    def ErrRaise(types = "ItsNotProcessing", errobj = "ItsWillInput"):
                        return ErrRaser(errobj)
                    yield argv
            return @wraps(ErrRaser)(lambda argv: asserter_deco4(ErrRaser, argv))
        return asserter_deco3
    return asserter_deco2

ad = asserter_deco
