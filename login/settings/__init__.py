from .base import *

# For local
from .production import *

# For production
try:
   from .local import *
except:
   pass