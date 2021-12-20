# package
import package

package.hello() # defined in package's __init__
package.hello2() # imported in package's __init__

# module in package
import package.module

package.module.hello()

from package import module

module.hello()

from package.module import hello as pmhello

pmhello()

# submodule in subpackage
import package.subpackage.submodule

package.subpackage.submodule.subhello()

from package import subpackage

subpackage.submodule.subhello()

from package.subpackage import submodule

submodule.subhello()

import package.subpackage.submodule as pss

pss.subhello()

from package.subpackage.submodule import subhello

subhello()

# import *
before = None
before  = set(dir())
from package.subpackage import *  # imports those in __all__ in subpackage's __init__

print(set(dir()) - before)

before  = set(dir())
from package.greeting import *  # imports all variables, functions, etc. from greeting

print(set(dir()) - before)
