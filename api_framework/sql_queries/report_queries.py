report_job_query = "SELECT * FROM smartweld.machine_input WHERE ts between %s and %s and machineid = %s"

report_sum_query = "SELECT SUM(weldduration) AS Total_weldduration, SUM(onduration) AS Total_onduration, " \
                   "SUM(idle_duration) AS total_idle_duration, SUM(total_loss) AS sum_total_loss, " \
                   "SUM(availability) AS total_availability, SUM(oee) AS total_oee, SUM(quality) AS total_quality, " \
                   "SUM(performance) AS total_performance, SUM(weld_power_consumed) AS total_weld_power_consumed, " \
                   "SUM(man_power_productivity) AS total_man_power_productivity FROM smartweld.daily_report " \
                   "WHERE ts between %s and %s and machineid = %s"

report_daywise_query = "SELECT * FROM smartweld.daily_report WHERE ts between %s and %s and machineid = %s"

report_config_query = "SELECT welder_daily_available, weld_power_consume, power_rate_unit, idle_power_consume, " \
                      "daily_labour_rate, daily_shift_hour FROM smartweld.report_config"

getDailyRecordssum_query = "SELECT json_build_object('sum', json_build_object('total_weldduration',T2.total_weldduration," \
                           "'total_onduration',T2.total_onduration,'total_idle_duration',T2.total_idle_duration, " \
                           "'sum_total_loss',T2.sum_total_loss,'total_aval',T2.total_aval,'tota_oee',T2.tota_oee, " \
                           "'total_quality',T2.total_quality,'total_performance',T2.total_performance,'total_weld_power_consumed', " \
                           "T2.total_weld_power_consumed, 'total_idle_power_consumed', T2.total_idle_power_consumed, " \
                           "'total_man_power_productivity', T2.total_man_power_productivity)) from " \
                           "(SELECT machineid ,sum(weldduration) as total_weldduration, sum(onduration) as total_onduration, " \
                           "sum(idle_duration) as total_idle_duration, sum(total_loss) as sum_total_loss , avg(availability) as total_aval, " \
                           "(avg(availability)*avg(quality)* avg(performance))/10000 as tota_oee, avg(quality) as total_quality, " \
                           "avg(performance) as total_performance, sum(weld_power_consumed) as total_weld_power_consumed, " \
                           "sum(power_loss_idle_unit) as total_idle_power_consumed , avg(man_power_productivity) as " \
                           "total_man_power_productivity FROM smartweld.daily_report WHERE ts between %s and %s and machineid= %s " \
                           "group by machineid)T2"

getDailyRecordsProduced_query = "SELECT json_build_object('jobs', json_agg( json_build_object ('machineid',T1.machineid, " \
                                "'ts',T1.ts, 'cycle_time',T1.cycle_time,'produced',T1.produced, 'rejected',T1.rejected, " \
                                "'good',T1.produced-T1.rejected))) from (select * FROM smartweld.machine_input " \
                                "WHERE ts between %s and %s and machineid = %s order by ts asc)T1"

getDailyRecordsPerMachines_query = "SELECT json_build_object('daywise', json_agg(json_build_object('machineid',T1.machineid, " \
                                   "'ts',T1.ts,'weldduration',T1.weldduration,'onduration',T1.onduration, " \
                                   "'idle_duration',T1.idle_duration, 'man_power_productivity',T1.man_power_productivity, " \
                                   "'loss_productivity',T1.loss_productivity,'idle_duration',T1.idle_duration, " \
                                   "'weld_power_consumed',T1.weld_power_consumed, 'power_loss_idle_unit',T1.power_loss_idle_unit, " \
                                   "'power_consumption_work',T1.power_consumption_work, 'power_consumption_idle', " \
                                   "T1.power_consumption_idle, 'monitory_loss',T1.monitory_loss ,'loss_man_power_productivity', " \
                                   "T1.loss_man_power_productivity,'total_loss',T1.total_loss, 'availability',T1.availability," \
                                   "'oee',T1.oee,'quality',T1.quality,'performance',T1.performance))) from " \
                                   "(SELECT *  FROM smartweld.daily_report WHERE ts between %s and %s and machineid= %s order by ts asc)T1"

dailypowerrecordpermachine_query = "Select * , TRUNC(CAST(((calculated.onduration - calculated.weldduration) * " \
                                   "(SELECT noload FROM smartweld.job_configuration where machineid = {machineid})) AS numeric),2) as " \
                                   "idealpowerconsumed, TRUNC(CAST((calculated.weldduration * (SELECT load FROM smartweld.job_configuration where machineid = {machineid})) " \
                                   "AS numeric),2)as weldpoweconsumed FROM (SELECT (Select Distinct machineid from smartweld.machine_configuration where machineid = {machineid} ), " \
                                   "extract(epoch from date_trunc('days',to_timestamp(MAX(w.timeinstance)))) + 1800000   as recordtimeinstance, TRUNC(CAST(CAST(SUM(weldduration) AS FLOAT) AS numeric)/3600,2) as " \
                                   "weldduration, TRUNC(CAST(CAST(SUM(onduration)  AS FLOAT) AS numeric)/3600,2) as onduration FROM smartweld.weld_analysis_calculation as w Where " \
                                   "machineid = {machineid} and timeinstance between {startdate} and {enddate} GROUP BY extract(epoch from date_trunc('days', to_timestamp(w.timeinstance)))) AS calculated"

getDailyRecordssumALL_query = "SELECT json_build_object('sum', json_build_object('total_weldduration',T2.total_weldduration, " \
                              "'total_onduration',T2.total_onduration,'total_idle_duration',T2.total_idle_duration, " \
                              "'sum_total_loss',T2.sum_total_loss,'total_aval',T2.total_aval,'tota_oee',T2.tota_oee, " \
                              "'total_quality',T2.total_quality,'total_performance',T2.total_performance,'total_weld_power_consumed', " \
                              "T2.total_weld_power_consumed, 'total_idle_power_consumed', T2.total_idle_power_consumed)) " \
                              "from (SELECT sum(weldduration) as total_weldduration, sum(onduration) as total_onduration ," \
                              "sum(idle_duration) as total_idle_duration, sum(total_loss) as sum_total_loss , avg(availability) as " \
                              "total_aval,( avg(availability)* avg(quality)*avg(performance))/10000 as tota_oee, avg(quality) as total_quality, " \
                              "avg(performance) as total_performance, sum(weld_power_consumed) as total_weld_power_consumed, " \
                              "sum(power_loss_idle_unit) as total_idle_power_consumed FROM smartweld.daily_report_all WHERE " \
                              "ts between %s and %s )T2"

getDailyRecordsProducedALL_query = "SELECT json_build_object('jobs', json_agg( json_build_object ('ts',T1.ts, 'produced',T1.produced, " \
                                   "'rejected',T1.rejected, 'good',T1.produced-T1.rejected))) from (select ts, sum(produced) as produced , " \
                                   "sum(rejected) as rejected FROM smartweld.machine_input WHERE ts between %s and %s group by ts order by ts asc)T1"

getDailyRecordsALL_query = "SELECT json_build_object('daywise', json_agg(json_build_object('ts',T1.ts,'weldduration', " \
                     "T1.weldduration,'onduration',T1.onduration,'idle_duration',T1.idle_duration, " \
                     "'man_power_productivity',T1.man_power_productivity,'loss_productivity',T1.loss_productivity, " \
                     "'idle_duration',T1.idle_duration,'weld_power_consumed',T1.weld_power_consumed, " \
                     "'power_loss_idle_unit',T1.power_loss_idle_unit,'power_consumption_work',T1.power_consumption_work, " \
                     "'power_consumption_idle',T1.power_consumption_idle, 'monitory_loss',T1.monitory_loss ," \
                     "'loss_man_power_productivity',T1.loss_man_power_productivity,'total_loss',T1.total_loss, " \
                     "'availability',T1.availability,'oee',T1.oee,'quality',T1.quality,'performance',T1.performance))) " \
                     "from (SELECT *  FROM smartweld.daily_report_all WHERE ts between %s and %s order by ts asc)T1"

hourlyPowerRecordPerMachine_query = "Select * , TRUNC(CAST(((calculated.onduration - calculated.weldduration) * " \
                                    "(SELECT noload FROM smartweld.job_configuration where machineid = {machineid})) AS numeric),2) as " \
                                    "idealpowerconsumed, TRUNC(CAST((calculated.weldduration * (SELECT load " \
                                    "FROM smartweld.job_configuration where machineid = {machineid})) AS numeric),2)as " \
                                    "weldpowerconsumed FROM (SELECT (Select Distinct machineid from " \
                                    "smartweld.machine_configuration where machineid = {machineid} ), " \
                                    "extract(epoch from date_trunc('hours',to_timestamp(MAX(w.timeinstance)))) + 1800000 as " \
                                    "recordtimeinstance, TRUNC(CAST(CAST(SUM(weldduration) AS FLOAT) AS numeric)/3600,2) as " \
                                    "weldduration, TRUNC(CAST(CAST(SUM(onduration) AS FLOAT) AS numeric)/3600,2) as " \
                                    "onduration FROM smartweld.weld_analysis_calculation as w Where  machineid = {machineid} " \
                                    "and timeinstance between {startdate} and {enddate} GROUP BY " \
                                    "extract(epoch from date_trunc('hours', to_timestamp(w.timeinstance)))) AS calculated"