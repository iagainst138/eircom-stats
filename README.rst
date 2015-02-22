eircom-stats
===============================================================================

Sample::

    user@box:~$ ./eircom-stats.py -p 555-5555555
    Account number: 
    Total downloads: 41972 MB (40.989 GB)
    Total uploads:   1796 MB (1.755 GB)
    Combined total:  43768 MB (42.744 GB)
    user@box:~$ 


Usage::

    user@box:~$ ./eircom-stats.py -h
    usage: eircom-stats.py [-h] -p PHONE_NUMBER [-a ACCOUNT_NUMBER] [-g]

    View your Eircom broadband usage on the cli.

    optional arguments:
      -h, --help            show this help message and exit
      -p PHONE_NUMBER, --phone-number PHONE_NUMBER
                            Phone number
      -a ACCOUNT_NUMBER, --account-number ACCOUNT_NUMBER
                            Account number
      -g, --graph-link      Show url to graph


