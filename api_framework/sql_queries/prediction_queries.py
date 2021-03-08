warranty_query = "SELECT MP.*, MC.machine_tagname FROM smartweld.machine_prediction " \
                 "AS MP inner join smartweld.machine_configuration AS MC on MC.machineid = MP.machineid " \
                 "where MP.entity_id = %s"

wirefeed_query = "SELECT U.*, MC.machine_tagname FROM smartweld.userprediction AS U " \
                 "inner join smartweld.machine_configuration AS MC on MC.machineid = U.machineid " \
                 "WHERE MC.entity_id = %s"

getmaxerrorpermachine_query = "SELECT * FROM smartweld.max_error_analysis AS MA INNER JOIN (SELECT machineid, " \
                              "MAX(instances) AS Maxerror FROM smartweld.max_error_analysis " \
                              "GROUP BY machineid)test on MA.machineid = test.machineid and " \
                              "MA.instances = test.Maxerror WHERE entity_id = %s "

getmaxfaultbydays_query = "SELECT error_analysis_by_day.*, MC.machine_tagname FROM smartweld.error_analysis_by_day " \
                          "inner join smartweld.machine_configuration AS MC " \
                          "on MC.machineid = error_analysis_by_day.machineid WHERE error_analysis_by_day.machineid = %s " \
                          "and MC.entity_id = %s and error_analysis_by_day.datetime between %s and %s"