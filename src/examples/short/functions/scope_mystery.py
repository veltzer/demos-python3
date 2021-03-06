"""
Question: what does this function output ?

Answer: exception.

If you remove the remark over 'global g' then
the 'g' variable is the same all over the program.

If you leave the remark over 'global g' then 'g'
inside 'my_mistery_function' is referenced before
it is assigned and you get an exception indicating
that.
"""


# noinspection PyUnboundLocalVariable
def my_mystery_function():
    # global g
    print(g)
    if True:
        g += 17
    print(g)


g = 4
# noinspection PyBroadException
try:
    my_mystery_function()
except:
    print('yes, got an exception')
print(g)
