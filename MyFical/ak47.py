def akargv(*argv, **kargv):
    '''
    # akargv(*argv, **kargv) => (argv, kargv)
    # akargv(*argv) => argv
    # akargv(**kargv) => kargv
    # akargv() => (,)
    '''
    r = (argv, kargv)
    p, q = map(bool, r)
    if p and q:
        return r
    elif p:
        return argv
    elif q:
        return kargv
    else:
        return (, )
