from pprint import pprint
import json

def load_castle_json(json_filename):
    with open(json_filename) as json_file:
        try:
          data = json.load(json_file)
          return data
        except ValueError:
          print "ERROR: Syntax error in " + json_filename
          print "       Check commas, braces, brackets, quote marks, etc."
          print "       Note that in JSON, you must use \"key\" : value, "
          print "       rather than 'key' : value "
          
    
def listOfNonNegativeIntsOfLength10(alist):
    if type(alist)!=list:
      return False
    if len(alist)!=10:
      return False
    for x in alist:
      if x < 0:
        return False
    return True

def check_castle_json(data):
    errors = 0

    if type(data)!=dict:
      print "ERROR: castle data not valid"
      return False        

    if len(data.keys()) != 1 or len(data.values()) != 1:
      print "ERROR: castles data should contain one key, mapping to one dictionary"
      errors += 1

    name = data.keys()[0]
    if name==u'First_L':
      print "ERROR: You need to change 'First_L' to your first name, underscore, last initial"
      errors += 1

    expected_dates = [u'0823', u'0824', u'0825', u'0826', u'0827', u'0828', u'0829', u'0830', u'0831', u'0901']
    actual_dates = sorted(data.values()[0].keys())
    if str(expected_dates) != str(actual_dates):
      print "ERROR: expected dates were: " + str(expected_dates)
      print "       actual dates were: " + str(actual_dates)
      errors += 1
      
    for d in actual_dates:
      if not listOfNonNegativeIntsOfLength10(data[name][d]):
        print "ERROR: data for " + str(d) + " should be list of 10 non-neg ints"
        errors += 1
        continue

      realm = data[name][d]
      if sum(realm) > 100:
        print "ERROR: data for " + str(d) + " sums to " + str(sum(realm))
        print "       it must sum to less than 100"
        errors += 1
        
    return (errors == 0)


if __name__=="__main__":
    data = load_castle_json("castles.json")
    result = check_castle_json(data)

    if not result:
        print "Please these errors if you want to participate in the next round"
    else:
        print "Your castles look ok.  Here they are:"
        pprint(data)
    
