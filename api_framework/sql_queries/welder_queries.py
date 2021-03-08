welder_read_query = "SELECT * FROM smartweld.welderdetails"

getWelderMachineMapping_query =  "SELECT MC.machineid, MW.welderid, MC.machine_tagname, " \
                                 "W.firstname, W.lastname FROM smartweld.machine_welder AS MW left join " \
                                 "smartweld.machine_configuration AS MC on MW.machineid = MC.machineid " \
                                 "left join smartweld.welderdetails AS W on MW.welderid = W.id WHERE MC.entity_id = %s"

welder_insert_query = "INSERT INTO smartweld.welderdetails (firstname, lastname, age, phone, proficiency, gender, entity_id) " \
                      "VALUES(%s, %s, %s, %s, %s, %s, %s)"

welder_update_query = "UPDATE smartweld.welderdetails SET firstname = %s, lastname = %s, age = %s, phone = %s, " \
                      "proficiency = %s, gender = %s WHERE id = %s and entity_id = %s"

modifyWelderMachineMapping_query = "UPDATE smartweld.machine_welder SET welderid = %s WHERE machineid = %s and entity_id = %s"

welder_delete_query = "DELETE FROM smartweld.welderdetails WHERE id =%s and entity_id = %s;"

welderMappingDelete_query = "DELETE FROM smartweld.machine_welder Where welderid = %s and entity_id = %s"

welder_machine_mapping_add_query = "INSERT INTO smartweld.machine_welder(machineid, welderid, entity_id) VALUES (%s, %s, %s);"

getUnMappedWelder_query = "select WD.id , WD.firstname, WD.lastname from smartweld.welderdetails WD left join " \
                          "smartweld.machine_welder MW ON WD.id = MW.welderid WHERE MW.welderid IS NULL and WD.entity_id = %s"

getUnMappedMachine_query = "select MC.machineid, MC.machine_tagname from smartweld.machine_configuration MC left join " \
                           "smartweld.machine_welder MW ON MC.machineid = MW.machineid WHERE MW.machineid  IS NULL and MC.entity_id = %s"