machine_insert_query = "INSERT INTO smartweld.machine_configuration(machineid, buyer_company, city, country, " \
                       "latitude, longitude, model, pincode, sensor_nodeid, state, userid, machine_tagname, " \
                       "date_of_manufacture, saledate, entity_id) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_MachineConfig_query = "INSERT INTO smartweld.job_configuration(machineid, jobid, opvolt, minthreshold, " \
                             "maxthreshold, min_current_time, max_current_time, min_gasflow, max_gasflow, min_wirefeed, " \
                             "max_wirefeed, min_voltage, max_voltage, current_max_range, jobcreated, entity_id,load, noload, wiresize) " \
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_warrantydetails_query =  "INSERT into smartweld.machine_waranty_details(machineid,startdate,expirydate, entity_id) " \
                                "VALUES (%s, %s, %s, %s)"

machine_update_query =  "UPDATE smartweld.machine_configuration SET  buyer_company = %s, city = %s, country = %s, " \
                        "date_of_manufacture = %s, latitude = %s, longitude = %s, model = %s, pincode = %s, saledate = %s, " \
                        "sensor_nodeid = %s, state = %s, userid = %s WHERE machineid= %s and entity_id = %s"

updateMachineConfig_query =  "UPDATE smartweld.job_configuration SET  min_gasflow = %s, max_gasflow = %s, min_wirefeed = %s, " \
                             "max_wirefeed = %s, min_voltage = %s , max_voltage = %s, minthreshold = %s, maxthreshold = %s, " \
                             "jobcreated = %s, min_current_time = %s, max_current_time = %s, jobid = %s, " \
                             "current_max_range = %s Where machineid = %s and entity_id = %s"


machine_delete_query = "DELETE FROM smartweld.machine_configuration WHERE machineid =%s and entity_id = %s;"

liveData_query = "SELECT * from smartweld.livestream as L Where L.machineid = %s and L.entity_id = %s "

getAllMachines = "SELECT * FROM smartweld.machine_configuration inner join smartweld.node_configuration on machine_configuration.sensor_nodeid = node_configuration.nodeaddr " \
                 "inner join smartweld.gateway_configuration on node_configuration.gateway_mac_id = gateway_configuration.gateway_macid " \
                 "inner join smartweld.job_configuration on job_configuration.machineid = machine_configuration.machineid " \
                 "where machine_configuration.userid =%s and machine_configuration.entity_id = %s order by machine_configuration.machineid desc"

getSelectedMachine_query = "SELECT * FROM smartweld.machine_configuration left join smartweld.job_configuration " \
                     "on job_configuration.machineid = machine_configuration.machineid " \
                     "Where machine_configuration.machineid = %s and machine_configuration.entity_id = %s"

countwarrantydetails_query = "SELECT COUNT(*) as total, (SELECT COUNT(*) as underwarranty " \
                             "from smartweld.machine_waranty_details " \
                             "WHERE (expirydate >= NOW() and expirydate >= (NOW() + interval '120 hours'))), " \
                             "(SELECT COUNT(*) as expired  from smartweld.machine_waranty_details WHERE expirydate < NOW()), " \
                             "(SELECT COUNT(*) as renewal from smartweld.machine_waranty_details WHERE " \
                             "(expirydate < (NOW() + interval '120 hours') and expirydate > NOW())) " \
                             "FROM smartweld.machine_waranty_details"

upgrade_warranty_query =  "UPDATE smartweld.machine_waranty_details SET expirydate = %s WHERE machineid = %s and entity_id = %s"

getwarranty_query = "select machineid, startdate as saledate, expirydate from smartweld.machine_waranty_details " \
               "WHERE machineid = %s and entity_id = %s"

getwirefeed_query = "SELECT machineid, timeleft, initialstock, stockleft, lastupdated, entity_id " \
                    "FROM smartweld.userprediction WHERE machineid = %s and entity_id = %s"

stockupgrade_query = "UPDATE smartweld.userprediction SET initialstock = %s, lastupdated = %s WHERE machineid = %s and " \
                     "entity_id = %s"

dailyRecordsPerMachines_query = "SELECT *,(SELECT CASE WHEN TRUNC(SUM(weldduration)/ NULLIF(SUM(onduration),0),2) IS " \
                                "NULL THEN 0 ELSE TRUNC((SUM(weldduration)/ NULLIF(SUM(onduration),0)),2) END as " \
                                "utilization FROM (SELECT SUM(weldduration) as weldduration , SUM(onduration) as " \
                                "onduration, SUM(quality) as goodweld FROM smartweld.weld_analysis_calculation Where " \
                                "machineid = {machineid} and timeinstance between {startdate} and {enddate} GROUP BY " \
                                "timeinstance) as utilization), " \
                                "(SELECT CASE WHEN TRUNC((SUM(goodweld)/NULLIF(SUM(weldduration),0)) * 100,2) IS NULL " \
                                "THEN 0 ELSE TRUNC((SUM(goodweld)/NULLIF(SUM(weldduration),0)) * 100,2) END as quality " \
                                "FROM (SELECT SUM(weldduration) as weldduration , SUM(onduration) as onduration, " \
                                "SUM(quality) as goodweld FROM smartweld.weld_analysis_calculation Where  machineid = {machineid} and " \
                                "timeinstance between {startdate} and {enddate} GROUP BY timeinstance ) as quality), " \
                                "(SELECT SUM(jobcount) as totaljob FROM (SELECT TRUNC(CAST(CAST(SUM(weldduration) AS " \
                                "FLOAT) AS numeric)/45,2)  as jobcount FROM smartweld.weld_analysis_calculation Where " \
                                "machineid = {machineid} and timeinstance between {startdate} and {enddate} GROUP BY timeinstance) as totaljob)," \
                                "(SELECT SUM(goodcount) as goodJob FROM " \
                                "(SELECT TRUNC(CAST(CAST(SUM(quality) AS FLOAT) AS numeric)/360,2)  as goodcount " \
                                "FROM smartweld.weld_analysis_calculation Where  machineid = {machineid} and timeinstance " \
                                "between {startdate} and {enddate}" \
                                "GROUP BY timeinstance) as goodJob),(SELECT (SUM(jobcount)-SUM(goodcount)) " \
                                "as badjob FROM (SELECT TRUNC(CAST(CAST(SUM(weldduration) AS FLOAT) AS numeric)/45,2) " \
                                "as jobcount,  TRUNC(CAST(CAST(SUM(quality) AS FLOAT) AS numeric)/360,2)  as goodcount " \
                                "FROM smartweld.weld_analysis_calculation Where  machineid = {machineid} and timeinstance " \
                                "between {startdate} and {enddate}" \
                                "GROUP BY timeinstance ) as badjob ),(SELECT  SUM(weldduration) as " \
                                "overallweldduration FROM (SELECT SUM(weldduration) as weldduration " \
                                "FROM smartweld.weld_analysis_calculation Where  machineid = {machineid} and timeinstance " \
                                "between {startdate} and {enddate}" \
                                "GROUP BY timeinstance ) as overallweldduration ), (SELECT  SUM(onduration) " \
                                "as overallonduration FROM (SELECT  SUM(onduration) as onduration " \
                                "FROM smartweld.weld_analysis_calculation Where  machineid = {machineid} and timeinstance " \
                                "between {startdate} and {enddate} " \
                                "GROUP BY  timeinstance) as overallonduration) FROM " \
                                "( SELECT (Select Distinct machineid from smartweld.weld_analysis_calculation where machineid = {machineid}), " \
                                "MAX(timeinstance) + 1800000 as recordtimeinstance, " \
                                "TRUNC(CAST(CAST(SUM(weldduration) AS FLOAT) AS numeric)/3600,2) as weldduration, " \
                                "TRUNC(CAST(CAST(SUM(weldduration) AS FLOAT) AS numeric)/45,2)  as jobcount, " \
                                "TRUNC(CAST(CAST(SUM(onduration)  AS FLOAT) AS numeric)/3600,2) as onduration, " \
                                "TRUNC(CAST(CAST(SUM(quality) AS FLOAT) AS numeric)/360,2) as goodweld FROM " \
                                "smartweld.weld_analysis_calculation Where  machineid = {machineid} and timeinstance between {startdate} and {enddate} " \
                                "GROUP BY timeinstance ) AS CALCULATED ORDER by recordtimeinstance asc"