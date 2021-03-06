YArg
====

Insipiration:
-------------

Argparse_ is a great libary shipped with Python 2.7. 
It is powerful and highly configurable argument parser, 
I've been using it for a while, and I do like it and enjoy using it.

However, I also found it is a little bit difficult to use, 
and it could be ending up quite boaring to adding up arguments by calling argparse_ APIs.

After writing a couple scripts / app using argparse_, 
I belive that I found a *arguably* better and easier way to do it: YArg_.

YArg_ is a lib intended to make easier to create command-line app.

Highlights:
-----------
- No need to specify what arguments to add. YArg_ will try matching the right argument with you functions.

- YAML_ format arguments. Which means argument with types. Thanks to PyYAML_.

  - int
  - float
  - boolean
  - dictionary
  - Datetime
  
- Passing the argument as a YAML_ format file.
  
- Neat and simple API, easy to use -- Follows "conventional over configuration".

- Hiding the complexity of using argparse_.

.. _YAML: http://yaml.org
.. _PyYAML: http://pyyaml.org
.. _argparse: https://docs.python.org/2.7/library/argparse.html
.. _YArg: https://github.com/tly1980/yarg

Examples Usages
---------------
