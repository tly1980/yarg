#!/usr/bin/env python
import yarg
import logging


def fun1(a, b, c='c'):
    logging.info("%s, %s, %s", a, b, c)
    logging.debug("%s - %s - %s", a, b, c)

def fun2(*a):
    print sum(a)



if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
    m = yarg.Main({'fun1': fun1, 'fun2': fun2})
    m.main()