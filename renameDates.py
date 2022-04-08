import shutil, os, re

date_pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """,re.VERBOSE)

for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)
    
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euro_filename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir,amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    #shutil.move(amer_filename, euro_filename) # uncoment after testing
    
