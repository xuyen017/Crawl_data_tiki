
from configparser import ConfigParser
def read_db_config(filename='db_config.ini', section='postgresql'):
    # Create a parser object
    parser =  ConfigParser()
    # read  the config file
    parser.read(filename)

    db={}

    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]]= item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section,filename))
    return db
