addNewGateway_query = "INSERT INTO smartweld.gateway_configuration(gateway_macid, gateway_id, commission, userid, entity_id) " \
                      "VALUES (%s, %s, %s, %s, %s)"

updateGateway_query = "UPDATE smartweld.gateway_configuration SET gateway_macid = %s, commission = %s, userid = %s " \
                      "WHERE gateway_id = %s and entity_id = %s"

getAllGateways_query = "SELECT distinct gateway_id, commission FROM smartweld.gateway_configuration AS GC inner join " \
                       "smartweld.userdetails AS U on GC.userid = U.userid " \
                       "Where U.userid = %s and GC.commission = 1 and GC.entity_id = %s "

getSelectedGateway_query = "SELECT distinct gateway_macid FROM smartweld.gateway_configuration AS GC inner join " \
                           "smartweld.userdetails AS U on GC.userid = U.userid Where U.userid = %s and GC.gateway_id = %s " \
                           "and GC.entity_id = %s"

deleteGateway_query = "UPDATE smartweld.gateway_configuration SET commission = 0 WHERE gateway_id = %s and entity_id = %s"
