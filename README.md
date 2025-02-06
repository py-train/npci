# NPCI Chennai Batch (Morn+Eve) Jan'25

Material for the morning and evening batches for NPCI, Chennai


## Structure

| Folder | Contents |
|--------|----------|
| `data/` | All data/files related to the examples and exercises in the course |
| `morn/` | All material (including notebooks) specific to the morning batch |
| `eve/`  | All material (including notebooks) specific to the evening batch |
| */`firstsite` | Django project created over the last few days for each batch |

The common material will continue to find its way into the top level folder
or sub-folders thereof.

## Django Project

We configured two database backends for this project:
1. The default sqlite3 flat-file DB
2. An AWS-deployed MySQL instance

The AWS-deployed instance might not continue to run forever. I'm sure you know how to changeover to the other one (or any other in fact): define a new section, with the relevant `ENGINE`, fill in credentials and connection details, and make as the "default".


    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "djangodb",
        "USER": "admin",
        "PASSWORD": "djangotestserver",
        "HOST": "demo.chscr40jxrsi.ap-south-1.rds.amazonaws.com",
        "PORT": 3306
    }


## Notes
- Feel free to contribute back if you have suggestions, corrections, additions. PR's are public right now.
-
