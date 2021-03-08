get_All_User = "SELECT userid, age, city, contact_number, country, firstname, gender, lastname, mail_id, pincode, " \
                  "role, state, status, username, entity_id FROM smartweld.userdetails WHERE entity_id = %s"

user_update_query = "UPDATE smartweld.userdetails SET firstname = %s, lastname = %s, age = %s, gender = %s, mail_id = %s, " \
                    "contact_number = %s, city = %s, country = %s, state = %s, pincode = %s, role = %s, status = %s " \
                    "WHERE userid = %s and entity_id = %s"

user_delete_query = "DELETE FROM smartweld.userdetails WHERE userid =%s AND entity_id = %s;"

user_insert_query = "INSERT INTO smartweld.userdetails(userid, age, city, contact_number, country, firstname, gender, " \
                    "lastname, mail_id, password, pincode, role, state, status, username, entity_id) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

get_Selected_User = "SELECT * FROM smartweld.userdetails where entity_id = %s and userid = %s"