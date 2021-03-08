getOverview_query = "SELECT json_build_object('weldduration', weldduration, 'powerduration', powerduration, " \
                    "'idleduration', idleduration, 'oee', oee, 'availability', availability, 'performance', " \
                    "performance , 'quality', quality, 'total', total, 'poweron', poweron, 'weldon', weldon, " \
                    "'idealpower',idealpower,'weldpower',weldpower, 'manpowerproductivity', " \
                    "( SELECT json_agg(json_build_object('machineid',machineid, 'value',man_power_productivity)) " \
                    "FROM smartweld.daily_report  WHERE ts = %s - 86400000), " \
                    "'config', ( SELECT json_build_object( 'daily_shift_hrs', daily_shift_hour, " \
                    "'power_market_rate', power_rate_unit, 'welder_daily_available_hrs', welder_daily_available,  " \
                    "'daily_labour_rate', daily_labour_rate, 'Weld_power_consume', weld_power_consume , " \
                    "'idle_power_consume', idle_power_consume) FROM smartweld.report_config ) , " \
                    "'status',(SELECT json_agg(json_build_object('machineid',machineid,'status', status))  " \
                    "FROM smartweld.livestream)) result FROM smartweld.home"

getMachinesStatus_query = "SELECT DISTINCT(T.*) FROM (Select (SELECT COUNT(*) as poweron FROM smartweld.livestream " \
                          "WHERE status in (2,1)), (SELECT COUNT(*) as weldon FROM smartweld.livestream WHERE status = 1), " \
                          "(SELECT COUNT(*) as total FROM smartweld.livestream) FROM smartweld.livestream ) T"

getwirefeed_query = "SELECT SUM(stockleft) as totalwirefeed FROM smartweld.userprediction inner join " \
                    "smartweld.machine_configuration on userprediction.machineid = machine_configuration.machineid " \
                    "where machine_configuration.userid = %s and machine_configuration.entity_id = %s"

getHourly_query = "SELECT json_build_object('ts',json_agg(T.ts),'idealduration',json_agg(T.idealduration), " \
                  "'weldduration',json_agg(T.weldduration),'onduration',json_agg(T.onduration)) result " \
                  "FROM (select (SUM(onduration) -  SUM(weldduration) ) as idealduration , " \
                  "SUM(weldduration) as weldduration , SUM(onduration)  as onduration, " \
                  "extract(epoch from date_trunc('hours', to_timestamp(w.timeinstance))) + 1800000 as ts from " \
                  "smartweld.weld_analysis_calculation as w where entity_id = %s and timeinstance between " \
                  "%s + 3600000  and %s group by " \
                  "extract(epoch from date_trunc('hours', to_timestamp(w.timeinstance)))order by " \
                  "extract(epoch from date_trunc('hours', to_timestamp(w.timeinstance))) ASC) T"
