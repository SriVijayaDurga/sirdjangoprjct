addTicket_query = "INSERT INTO smartweld.ticket_status_details(machineid, cause, remark, severity, ticket_status, userid, " \
                  "closed_date, reported_date, entity_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

updateTicket_query = "UPDATE smartweld.ticket_status_details SET cause = %s, remark = %s, severity = %s, " \
                     "ticket_status = %s, userid = %s, reported_date = %s, closed_date = %s WHERE machineid = %s and " \
                     "ticketid = %s and entity_id = %s"

getAllTicketsCalculated_query =  "SELECT (SELECT COUNT(severity) as low FROM smartweld.ticket_status_details WHERE  " \
                                 "userid = {userid} and severity = 1 and reported_date between {startdate} and {enddate}), " \
                                 "(SELECT COUNT(severity) as medium FROM smartweld.ticket_status_details WHERE userid = {userid} and " \
                                 "severity = 2 and reported_date between {startdate} and {enddate}), (SELECT COUNT(severity) as high " \
                                 "FROM smartweld.ticket_status_details WHERE userid = {userid} and severity = 3 and " \
                                 "reported_date between {startdate} and {enddate}), (SELECT COUNT(severity) as critical FROM " \
                                 "smartweld.ticket_status_details WHERE userid = {userid} and severity = 4 and reported_date " \
                                 "between {startdate} and {enddate}),(SELECT COUNT(cause) as motor FROM smartweld.ticket_status_details " \
                                 "WHERE userid = {userid} and cause = 'Motor' and reported_date between {startdate} and {enddate}), " \
                                 "(SELECT COUNT(cause) as wirefeed FROM smartweld.ticket_status_details WHERE userid = {userid} and " \
                                 "cause = 'Wire Feed' and reported_date between {startdate} and {enddate}),(SELECT COUNT(cause) as " \
                                 "voltage FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Voltage' and " \
                                 "reported_date between {startdate} and {enddate}),(SELECT COUNT(cause) as current FROM " \
                                 "smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Current' and reported_date " \
                                 "between {startdate} and {enddate}),(SELECT COUNT(cause) as overheat FROM " \
                                 "smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Over Heating' and " \
                                 "reported_date between {startdate} and {enddate}),(SELECT COUNT(cause) as others " \
                                 "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Others' and " \
                                 "reported_date between {startdate} and {enddate}),(SELECT COUNT(ticket_status) as " \
                                 "open FROM smartweld.ticket_status_details WHERE userid = {userid} and ticket_status = 'Open' " \
                                 "and reported_date between {startdate} and {enddate}),(SELECT COUNT(ticket_status) as resolved FROM " \
                                 "smartweld.ticket_status_details WHERE userid = {userid} and ticket_status = 'Resolved' and " \
                                 "reported_date between {startdate} and {enddate}),(SELECT COUNT(ticket_status) as " \
                                 "inprogress FROM smartweld.ticket_status_details WHERE userid = {userid} and " \
                                 "ticket_status = 'In Progress' and reported_date between {startdate} and {enddate}),Count(*) as total " \
                                 "FROM smartweld.ticket_status_details WHERE userid = {userid} and reported_date between " \
                                 "{startdate} and {enddate} and entity_id = {entity_id}"

sample = "SELECT (SELECT COUNT(severity) as low FROM smartweld.ticket_status_details WHERE " \
"userid = 'admin' and severity = 1 and reported_date between 1612419870000 and 1612419870000), " \
"(SELECT COUNT(severity) as medium FROM smartweld.ticket_status_details WHERE userid = 'admin' and " \
"severity = 2 and reported_date between 1612419870000 and 1612419870000), (SELECT COUNT(severity) as high " \
"FROM smartweld.ticket_status_details WHERE userid = 'admin' and severity = 3 and " \
"reported_date between 1612419870000 and 1612419870000), (SELECT COUNT(severity) as critical FROM " \
"smartweld.ticket_status_details WHERE userid = 'admin' and severity = 4 and reported_date " \
"between 1612419870000 and 1612419870000),(SELECT COUNT(cause) as motor FROM smartweld.ticket_status_details " \
"WHERE userid = 'admin' and cause = 'Motor' and reported_date between 1612419870000 and 1612419870000), " \
"(SELECT COUNT(cause) as wirefeed FROM smartweld.ticket_status_details WHERE userid = 'admin' and " \
"cause = 'Wire Feed' and reported_date between 1612419870000 and 1612419870000),(SELECT COUNT(cause) as " \
"voltage FROM smartweld.ticket_status_details WHERE userid = 'admin' and cause = 'Voltage' and " \
"reported_date between 1612419870000 and 1612419870000),(SELECT COUNT(cause) as current FROM " \
"smartweld.ticket_status_details WHERE userid = 'admin' and cause = 'Current' and reported_date " \
"between 1612419870000 and 1612419870000),(SELECT COUNT(cause) as overheat FROM smartweld.ticket_status_details " \
"WHERE userid = 'admin' and cause = 'Over Heating' and reported_date between 1612419870000 and 1612419870000), " \
"(SELECT COUNT(cause) as others FROM smartweld.ticket_status_details WHERE userid = 'admin' and " \
"cause = 'Others' and reported_date between 1612419870000 and 1612419870000),(SELECT COUNT(ticket_status) as " \
"open FROM smartweld.ticket_status_details WHERE userid = 'admin' and ticket_status = 'Open' and " \
"reported_date between 1612419870000 and 1612419870000),(SELECT COUNT(ticket_status) as resolved FROM " \
"smartweld.ticket_status_details WHERE userid = 'admin' and ticket_status = 'Resolved' and " \
"reported_date between 1612419870000 and 1612419870000),(SELECT COUNT(ticket_status) as inprogress FROM " \
"smartweld.ticket_status_details WHERE userid = 'admin' and ticket_status = 'In Progress' and " \
"reported_date between 1612419870000 and 1612419870000),Count(*) as total FROM smartweld.ticket_status_details WHERE " \
"userid = 'admin' and reported_date between 1612419870000 and 1612419870000"

getTickets_query = "SELECT (SELECT COUNT(severity) as severity FROM smartweld.ticket_status_details WHERE machineid = {machineid} and " \
                   "severity = {severity} and userid = {userid} and  reported_date between {startdate} and {enddate}),(SELECT COUNT(ticket_status) as " \
                   "open FROM smartweld.ticket_status_details WHERE machineid = {machineid} and severity = {severity} and userid = {userid} and " \
                   "ticket_status = 'Open' and reported_date between {startdate} and {enddate}),(SELECT COUNT(ticket_status) as resolved " \
                   "FROM smartweld.ticket_status_details WHERE machineid = {machineid} and severity = {severity} and userid = {userid} and " \
                   "ticket_status = 'Resolved' and reported_date between {startdate} and {enddate}),(SELECT COUNT(ticket_status) as " \
                   "inprogress FROM smartweld.ticket_status_details WHERE machineid = {machineid} and severity = {severity} and userid = {userid} and " \
                   "ticket_status = 'In Progress' and reported_date between {startdate} and {enddate}),Count(*) as total FROM " \
                   "smartweld.ticket_status_details WHERE machineid = {machineid} and severity = {severity} and entity_id = {entity_id} and userid = {userid} and reported_date " \
                   "between {startdate} and {enddate}"

getTicketsbyallparams_query = "SELECT machineid, ticketid, cause, closed_date, remark, reported_date, severity, " \
                              "ticket_status, userid FROM smartweld.ticket_status_details where machineid = %s and " \
                              "severity = %s and reported_date between %s and %s and userid = %s"

getAllTicketwoDT_query = "SELECT (SELECT COUNT(severity) as low FROM smartweld.ticket_status_details WHERE userid = {userid} and " \
                         "severity = 1),(SELECT COUNT(severity) as medium FROM smartweld.ticket_status_details WHERE " \
                         "userid = {userid} and severity = 2), (SELECT COUNT(severity) as high FROM smartweld.ticket_status_details " \
                         "WHERE userid = {userid} and severity = 3), (SELECT COUNT(severity) as critical " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and severity = 4),(SELECT COUNT(cause) as motor " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Motor'),(SELECT COUNT(cause) as wirefeed " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Wire Feed'),(SELECT COUNT(cause) as voltage " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Voltage'),(SELECT COUNT(cause) as current " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Current'),(SELECT COUNT(cause) as overheat " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Over Heating' ),(SELECT COUNT(cause) as others " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and cause = 'Others'),(SELECT COUNT(ticket_status) as open " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and ticket_status = 'Open'),(SELECT COUNT(ticket_status) as resolved " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and ticket_status = 'Resolved'),(SELECT COUNT(ticket_status) as inprogress " \
                         "FROM smartweld.ticket_status_details WHERE userid = {userid} and ticket_status = 'In Progress'),Count(*) as total FROM smartweld.ticket_status_details " \
                         "WHERE userid = {userid} and entity_id = {entity_id}"