# Job Finding Helpers
This package provides an easy way of parsing job offers (with user-specific settings) from several well-recognized 
job-offering portals in Slovakia and sending them via e-mail. 

Currently, it supports the following portals:
1. profesia.sk
2. kariera.sk

This package is developed by [Zoltan Galaz](http://zoltan.galaz.eu/) who created it for his wife to make it easier 
for her to go over the job offers during she was searching for a new job. For more information, please contact the 
author at <zoltan@galaz.eu>.

* * * * * * * * *

## Installation
```
git clone git@github.com:zgalaz/job-finding-helpers.git
cd job-find-helpers
python3 -m virtualenv .venv
source .venv/bin/activate
pip install .
```

## Structure
```
+---helpers
|   +---parsers
|   |   +---portals
|   |   |   base.py
|   |   |   kariera.py
|   |   |   profesia.py
|   |   +---websites
|   |   |   parser.py
|   |           
|   +---senders
|   |   |   data_formatter.py
|   |   |   email_builder.py
|   |   |   email_sender.py
|   |           
|   \---utils
|       |   logger.py
|
+---settings
|   |   email.json
```

## Use
The package provides the email.json settings file to configure all necessary information for th e-mail updates to 
work. The current implementation is limited to some job offer settings that my wife used. If needed, these can be 
updated/extended as needed.

# License
This project is licensed under the terms of the MIT license. For more details, see the **LICENSE** file.