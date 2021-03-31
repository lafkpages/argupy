from argupy import *

argupy = Args()

# define the argument --name as a string value
argupy.setarg('--name', STR, 'programmer', '-n') # defaults to 'programmer'. short name is -n

# greet the person
print('Greetings,', argupy.arg('--name')) # get the value of the original --name


'''
Try it!

Run:
+-------------------------------------+
| python3 greet.py --name "Elon Musk" |
+-------------------------------------+

And the output will be:
+-------------------------------------+
| Greetings, Elon Musk                |
+-------------------------------------+

If you just run:
+-------------------------------------+
| python3 greet.py                    |
+-------------------------------------+

The output will be:
+-------------------------------------+
| Greetings, programmer               |
+-------------------------------------+
'''