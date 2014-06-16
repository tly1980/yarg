#!/usr/bin/env python
import logging

import yarg

APP_BANNER = """
 _______   __  ___  ___  _________ _      _____ 
|  ___\ \ / / / _ \ |  \/  || ___ \ |    |  ___|
| |__  \ V / / /_\ \| .  . || |_/ / |    | |__  
|  __| /   \ |  _  || |\/| ||  __/| |    |  __| 
| |___/ /^\ \| | | || |  | || |   | |____| |___ 
\____/\/   \/\_| |_/\_|  |_/\_|   \_____/\____/ 

"""

APP_DESCRIPTION = "A kick example app what so ever."


def fun_min(*a):
    logging.info("about to find out the min number from: %s" % repr(a))
    logging.debug("Some debug message hopefully make senses to u.")
    print min(a)


def fun_sum(*a):
    print sum(a)

app = yarg.App(actions_map={'m': fun_min, 's': fun_sum}, default_action=fun_min)

if __name__ == '__main__':
    app.main()
