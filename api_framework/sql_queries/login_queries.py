check_username_exist_query = "SELECT * FROM smartweld.userdetails WHERE username = %s"

username_password_validations = "SELECT username,password FROM smartweld.userdetails " \
                                "WHERE username = %s and password = %s"

user_login_query = "SELECT UD.*, RM.* FROM smartweld.userdetails UD " \
                   "inner join smartweld.rolemaster RM " \
                   "ON UD.userid = RM.role_code " \
                   "WHERE UD.username = %s and UD.password = %s and " \
                   "RM.status = true"

# USER_LOGIN = "SELECT id, email, username,password FROM public.users where " \
#              "email = %s or username = %s"