machineInput_query = "SELECT json_agg(json_build_object('machineid',machineid, 'ts',ts, 'cycle_time',cycle_time, " \
                     "'produced',produced, 'rejected',rejected)) FROM smartweld.machine_input where entity_id = %s"

insert_MachineInput_query = "INSERT INTO smartweld.machine_input(machineid, cycle_time, produced, rejected, ts, entity_id) " \
                            "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT(machineid)  DO UPDATE SET " \
                            "cycle_time = EXCLUDED.cycle_time, produced = EXCLUDED.produced, rejected = EXCLUDED.rejected"


reportConfig_query = "SELECT json_build_object('welder_daily_available',welder_daily_available, " \
                     "'weld_power_consume',weld_power_consume, 'power_rate_unit',power_rate_unit, " \
                     "'idle_power_consume',idle_power_consume, 'daily_labour_rate',daily_labour_rate, " \
                     "'daily_shift_hour',daily_shift_hour) FROM smartweld.report_config"

updatereportConfig_query = "UPDATE smartweld.report_config SET welder_daily_available = %s, weld_power_consume = %s, " \
                           "power_rate_unit = %s, idle_power_consume = %s, daily_labour_rate = %s, daily_shift_hour = %s " \
                           "WHERE page_name='report' and entity_id = %s"

# insert_MachineInput_query = "INSERT INTO smartweld.machine_input(machineid, cycle_time, produced, rejected, ts, entity_id) " \
#                             "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT(machineid)  DO UPDATE SET " \
#                             "cycle_time = EXCLUDED.cycle_time, produced = EXCLUDED.produced, rejected = EXCLUDED.rejected"
