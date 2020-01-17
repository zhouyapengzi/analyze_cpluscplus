import sre_compile
_regexp_compile_cache = {}


def match(pattern, s):
    """Matches the string with the pattern, caching the compiled regexp."""
    # The regexp compilation caching is inlined in both Match and Search for
    # performance reasons; factoring it out into a separate function turns out
    # to be noticeably expensive.
    if pattern not in _regexp_compile_cache:
        _regexp_compile_cache[pattern] = sre_compile.compile(pattern)
    return _regexp_compile_cache[pattern].match(s)

def function_declaration_in_file(cfile):
    regexp = r'(\w(\w|::|\*|\&|\s)*)\('  # decls * & space::name( ...

    fun_list = set()
    with open(cfile) as f:
        lines = f.readlines()
    for line in lines:
        match_result = match(regexp, line)
        if match_result:
            # If the name is all caps and underscores, figure it's a macro and
            # ignore it, unless it's TEST or TEST_F.
            function_name = match_result.group(1).split()[-1]
            fun_list.add(function_name)
            '''if function_name == 'TEST' or function_name == 'TEST_F' or ( not Match(r'[A-Z_]+$', function_name)):
                starting_func = True'''
    return fun_list
