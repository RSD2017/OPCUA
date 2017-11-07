import sys
sys.path.insert(0, "..")


from opcua import Client


if __name__ == "__main__":

    client = Client("opc.tcp://192.168.1.80:4840")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
#        print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
#        print("Children of root are: ", root.get_children())

        # get a specific node knowing its node id
        #var = client.get_node(ua.NodeId(1002, 2))
#        var = client.get_node("0:Root,0:Objects,4:PLC,6:Modules,6:::,6:Camera_A,6:Camera_trigger")
#        print(var)
        #var.get_data_value() # get value of node as a DataValue object
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        modules = root.get_child(["0:Objects","4:PLC","6:Modules","6:::"])
        camera_trigger = modules.get_child(["6:Camera_A","6:Camera_trigger"]);
#        myvar = myvar.get_child(["6:Modules"])
#        myvar = myvar.get_child(["6:::"])
#        myvar = myvar.get_child(["6:::"])

#        obj = root.get_child(["0:Objects", "2:MyObject"])
#        print("Camera_trigger is", camera_trigger.get_value())

    finally:
        client.disconnect()
