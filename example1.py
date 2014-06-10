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


app = yarg.App()

@app.action('haha')
def fun1(a, b, c='c'):
    logging.info("%s, %s, %s", a, b, c)
    logging.debug("%s - %s - %s", a, b, c)

@app.action
def fun2(*a):
    print sum(a)

if __name__ == '__main__':
    app.main()
