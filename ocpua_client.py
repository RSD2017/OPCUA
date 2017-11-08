import sys
import json
sys.path.insert(0, "..")


from opcua import Client,ua

data = {}

from flask import Flask, make_response
app = Flask(__name__)



@app.route('/')
def index():
    global root
    #try:


    #Now getting a variable node using its browse path
    modules = root.get_child(["0:Objects","4:PLC","6:Modules","6:::"])
    camera_trigger = modules.get_child(["6:Camera_A","6:Camera_trigger"]);
    for node in modules.get_children():
       nodeName = node.get_browse_name().Name
       data[nodeName.__str__()]  = [] 
       for var in node.get_children():
           if var.get_data_type_as_variant_type() == ua.VariantType.ExtensionObject:
               #print "struct..."
               pass
           else:
                data[nodeName.__str__()].append({var.get_browse_name().Name:var.get_value()})
                resp = make_response(json.dumps(data)) 
                resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    #finally:
     #   client.disconnect()


if __name__ == '__main__':
        client = Client("opc.tcp://192.168.1.80:4840")
        root = client.get_root_node()
        client.connect()

	app.run(debug=True, port=int("8080"), host='0.0.0.0')
