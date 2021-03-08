addNewNode_query =  "INSERT INTO smartweld.node_configuration(nodeaddr, gateway_mac_id, commission, entity_id) VALUES (%s, %s, %s, %s)"

updateNode_query =  "UPDATE smartweld.node_configuration SET gateway_mac_id = %s, commission = %s WHERE nodeaddr = %s and entity_id = %s"

getAllNodes_query = "SELECT distinct NC.nodeaddr as nodeid, NC.commission as commission " \
                    "FROM smartweld.gateway_configuration AS GC inner join smartweld.node_configuration AS NC " \
                    "on GC.gateway_macid = NC.gateway_mac_id Where GC.gateway_id = %s and NC.commission = 1 and NC.entity_id = %s"

getSelectedNode_query = "SELECT distinct * FROM smartweld.node_configuration WHERE nodeaddr = %s and entity_id = %s"

deleteNode_query = "UPDATE smartweld.node_configuration SET  commission= 0 WHERE nodeaddr = %s and entity_id = %s"