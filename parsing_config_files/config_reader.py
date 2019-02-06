import configparser

# Create Config object
config = configparser.ConfigParser()
config.read('config.cfg')

print(config.sections())   #get all sections
print('dev' in config)    #check for existence of sections
print(config['dev']['server'])  #get the value fora key in section

#Print all keys
print('\nAll the prod keys')
for keys in config['prod']:
    print(keys)
print("")

#use get to return values
test_server=config['test']
prod_server=config['prod']
dev_server=config['dev']
print(test_server.get('uid'))
print(test_server.get('os')) #Returns None if the key does not exist
print(test_server.get('os','redhat')) #specify default value if the return is None
print(prod_server.get('uid','karbon')) #default values have precedence over fallback values

