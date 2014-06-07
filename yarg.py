import argparse
import sys
import inspect
import logging
import logging.config
import os.path

import yaml

DEFAULT_LOG_YAML ="""
version: 1

disable_existing_loggers: False

formatters:
    simple:
        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        datefmt: "%Y-%m-%d %H:%M:%S"

handlers:
    console:
        class: logging.StreamHandler
        formatter: simple
        stream: ext://sys.stdout

root:
    level: INFO
    handlers: [console]
"""

def yaml_x(argstr):
    if argstr.startswith('./') or argstr.startswith('/'):
        with open(argstr, 'rb') as f:
            return yaml.load(f)

    return yaml.load(argstr)

class Main(object):
    def __init__(self, actions_map, parser=None, description='A kick-ass commandline app using yarg.'):
        self.actions_map = actions_map
        if not parser:
            self.parser = argparse.ArgumentParser(description=description)
        else:
            self.parser = parser

        self.parser.add_argument('action_or_args', nargs='+', type=str, default=[])

        self.parser.add_argument('-va', '--vargs', type=str)
        self.parser.add_argument('-ka', '--kwargs', type=str)
        self.parser.add_argument('-x', '--extends', nargs='+', type=str, default=[])

        self.parser.add_argument('-ll', '--loglevel', dest='loglevel', type=str, default=None)
        self.parser.add_argument('--logcfg', type=str, default='./log.yaml')

        self.parser.add_argument('-y', '--yield', '')


        self.ARGS = None

    def init_log(self):
        # logging.basicConfig(level=level, 
        #     format=self.ARGS.logformat, datefmt=self.ARGS.logdateformat)
        logcfg = {}
        logcfg = yaml_x(self.ARGS.logcfg) if os.path.isfile(self.ARGS.logcfg) else yaml_x(DEFAULT_LOG_YAML)
        logcfg.setdefault('version', 1)
        logging.config.dictConfig(logcfg)

        if self.ARGS.loglevel:
            level = getattr(logging, self.ARGS.loglevel.upper())
            logging.Logger.root.setLevel(level=level)

    def failed(self, message, exit_code=-1):
        print >> sys.stderr, message
        sys.exit(exit_code)

    def parse(self, lst=[]):

        if not lst:
            self.ARGS = self.parser.parse_args()
        else:
            self.ARGS = self.parser.parse_args(lst)

    def guess_args(self):
        action = self.ARGS.action_or_args[0]
        args = [yaml.load(a) for a in self.ARGS.action_or_args[1:]]

        the_kwargs =  yaml_x(self.ARGS.kwargs) if self.ARGS.kwargs else {}
        the_vargs = yaml_x(self.ARGS.vargs) if self.ARGS.vargs else []

        if not isinstance(the_vargs, list):
            self.failed("-va/--vargs has to be a LIST in yaml/json format")

        if not isinstance(the_kwargs, dict):
            self.failed("-ka/--kwargs has to be a DICTIONARY in yaml/json format")

        xkwargs = [yaml.load(kv) for kv in self.ARGS.extends]

        invalid_xkwargs = [x for x in xkwargs if not isinstance(x, dict)]

        if len(invalid_xkwargs):
            self.failed("""
                -x/-extends has to be DICTIONARY in yaml/json format. Namely, something like 'a: 123' or '{"a": 123}' """)

        [the_kwargs.update(**x) for x in xkwargs]

        return action, args + the_vargs, the_kwargs

    def print_available_actions(self):
        print "Here are the available actions:"
        print "================================="
        idx = 0
        for name, fun in self.actions_map:
            idx += 1
            print "%s. %s - %s " % (idx, name, inspect.getargspec(fun))

    def call_action(self):

        action, the_args, the_kwargs = self.guess_args()

        fun = self.actions_map.get(action)

        if not fun:
            msg = "%s cannot be found in action map. Please use -aa to see available actions."  % action
            self.failed(msg)

        actual_args = None
        try:
            actual_args = inspect.getcallargs(fun, *the_args, **the_kwargs)
        except Exception, e:
            self.failed("Argument conflicts: %s " % str(e))

        print "About to call [%s] using: %s " % (action, str(actual_args))

        return fun(*the_args, **the_kwargs)

    def main(self, args_list=[]):
        self.parse(args_list)
        self.init_log()
        return self.call_action()

