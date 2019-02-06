import configparser

# Create Config object
config = configparser.ConfigParser()

# Creating key, value pair of information for section
config['book'] = {'Title': 'Island',
                  'Author': 'Aldous Huxley',
                  'Genre': 'Utopian'}
config['book']['rating'] = '4.5'  # Adding a key,value for existing section
config['book']['Genre'] = 'Utoipan Adeventure'  # Modifying an existing value for a key

config['author'] = {}  # initilizing a config section
author_info = config['author']  # mutating the config section
author_info['name'] = 'Aldous Huxley'  # initializing values for the param
author_info['born'] = '1920'  # initializing values for the param
author_info['place'] = 'United Kingdom'  # initializing values for the param

config['year'] = {}
config['year']['year'] = '1984'
config.remove_section('year')  # remove section
config.remove_option('book', 'Genre') # remove option

with open('book.cfg', 'w') as configfile:
    config.write(configfile)
