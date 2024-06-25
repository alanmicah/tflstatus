
def test_dict():
  dic = {}

  if not dic:
    print('Empty')
  
  if bool(dic):
    print('Not empty')       
  
  if not bool(dic):
    print('Emtpy')

  if len(dic) > 0:
    print('Not Empty')

def test_str(word):
  import re
  pattern = re.compile('[\W_]+') 
  print(pattern.sub('', word))
  print(re.sub(r'\W+', '', word))
def test_json():
  import json

  statusJson = open('data/dlr_status.json', 'r')
  eachStatus = json.load(statusJson)

  mapping = {
    'id': 'id'
  }

  for item in eachStatus:
    print(item['id'])
    # print(item.keys())
    for key in item.keys():
      print(key)

      # Mapping dictionary
      # for item in line_status:
      #   linedata = LineStatus()
      #   linedata.id = item['id']
      #   linedata.name = item['name']
      #   linedata.modeName = item['modeName']
      #   linedata.disruptions = item['disruptions']
      #   linedata.created = item['created']
      #   linedata.modified = item['modified']
      #   linedata.lineStatuses = item['lineStatuses']
      #   linedata.routeSections = item['routeSections']
      #   linedata.serviceTypes = item['serviceTypes']
      #   linedata.crowding = item['crowding']
      #   linedata.lastupdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      # mapping = {
      #   'id': 'id',
      #   'name': 'name',
      #   'modeName': 'modeName',
      #   'disruptions': 'disruptions',
      #   'created': 'created',
      #   'modified': 'modified',
      #   'lineStatuses': 'lineStatuses',
      #   'routeSections': 'routeSections',
      #   'serviceType': 'serviceType',
      #   'crowding': 'crowding',
      #   'lastupdate': 'lastupdate'
      # }
      # for item in line_status:
      #   linedata = LineStatus()
      #   # Map data to table columns here
      #   for column, key in mapping.items():
      #     if key is not None and key in item:
      #       setattr(linedata, column, item[key])
      #   linedata.lastupdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# -----Function calls-----#
# test_str('$type')
test_dict()