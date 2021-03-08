# TOKEN
AUTHORIZATION = 'authorization'
TOKEN_SLICED_LOCATION = 1

# REQUEST METHOD
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

# DATABASE KEY
CREDENTIAL_PATH = 'CREDENTIALPATH'
DEFAULT = 'default'
ENGINE = 'ENGINE'
OPTIONS = 'OPTIONS'
NAME = 'NAME'
USER = 'USER'
PASSWORD = 'PASSWORD'
HOST = 'HOST'
PORT = 'PORT'
SCHEMA = 'SCHEMA'

# MESSAGE
LOGGED_IN_SUCCESS = {"message": "logged in successfully"}
LOGGED_OUT_SUCCESS = {"message": "logged out successfully"}
LOGGED_OUT_FAILURE = {"message": "No user logged in"}
DEVICE_DELETE = {"message": "Device deleted successfully"}
DEVICE_ADDED = {"message": "Device added successfully"}
DEVICE_UPDATED = {"message": "Device updated successfully"}
WRONG_PASSWORD = 'Password is not correct'
USER_NOT_EXIST = 'Username is not registered with us'
SESSION_EXPIRY = 900

# CONFLICT ACTION
INSERTED = 'Insert'
UPDATED = 'Update'
DELETED = 'Delete'

# ACTION
ACTION = 'action'
LOGOUT = 'logout'
# DATABASE DEFAULT VALUE
FIRST_ELEMENT = 0
DEFAULT_VALUE = 1

# LOGIN REQUEST PAYLOAD
REQ_USERNAME = 'username'
REQ_PASSWORD = 'password'
DB_USER_ID = 'user_id'
DB_USER_AVAILABILITY_STATUS = 'user_availability'
DB_LOGIN_STATUS = 'user_login_status'

# login COLUMN KEYS
DB_COL_USER_ID = 'user_id'
DB_COL_USERNAME = "username"
DB_COL_F_NAME = 'first_name'
DB_COL_M_NAME = 'middle_name'
DB_COL_L_NAME = 'last_name'
DB_COL_AGE = 'age'
DB_COL_SEX = 'sex'
DB_COL_Email = 'email'
DB_COL_PHONE_NUMBER = 'phone_number'
DB_COL_ADDRESS = 'address'
DB_COL_MASTER = 'master'
DB_COL_ROLE = 'role'
DB_COL_USER_COMMISSION = 'usercommission'

# User_management
REQ_USERID = 'userid'
REQ_USER_NEW_ID = 'new_id'
REQ_USER_USERNAME = 'username'
REQ_USER_FIRST_NAME = 'firstname'
REQ_USER_LAST_NAME = 'lastname'
REQ_USER_AGE = 'age'
REQ_USER_GENDER = 'gender'
REQ_USER_MAILID = 'mail_id'
REQ_USER_CONTACT_NUMBER = 'contact_number'
REQ_USER_CITY = 'city'
REQ_USER_COUNTRY = 'country'
REQ_USER_STATE = 'state'
REQ_USER_PINCODE = 'pincode'
REQ_USER_ROLE = 'role'
REQ_USER_STATUS = 'status'
REQ_USER_ENTITY_ID = 'entity_id'
REQ_USER_PASSWORD = 'password'



# welder_management
REQ_WELDER_ID = 'id'
REQ_WELDER_FIRSTNAME = 'firstname'
REQ_WELDER_LASTNAME = 'lastname'
REQ_WELDER_AGE = 'age'
REQ_WELDER_PHONE = 'phone'
REQ_WELDER_PROFICIENCY = 'proficiency'
REQ_WELDER_GENDER = 'gender'

# machine
REQ_MACHINE_ID = 'id'
REQ_MACHINEID = 'machineid'
REQ_MACHINE_BUYER_COMPANY = 'buyer_company'
REQ_MACHINE_CITY = 'city'
REQ_MACHINE_COUNTRY = 'country'
REQ_MACHINE_LATITUDE = 'latitude'
REQ_MACHINE_LONGITUDE = 'longitude'
REQ_MACHINE_MODEL = 'model'
REQ_MACHINE_PINCODE = 'pincode'
REQ_MACHINE_SALEDATE = 'saledate'
REQ_MACHINE_SENSOR_NODEID = 'sensor_nodeid'
REQ_MACHINE_STATE = 'state'
REQ_MACHINE_USERID = 'userid'
REQ_MACHINE_TAG_NAME = 'machine_tagname'
REQ_MACHINE_DATE_OF_MANUFACTURE = 'date_of_manufacture'
REQ_MACHINE_ENTITY_ID = 'entity_id'

# job configuration
REQ_JOB_MACHINEID = 'machineid'
REQ_JOBID = 'jobid'
REQ_JOB_OPVOLT = 'opvolt'
REQ_JOB_MINTHRESHOLD = 'minthreshold'
REQ_JOB_MAXTHRESHOLD = 'maxthreshold'
REQ_JOB_MIN_CURRENT_TIME = 'min_current_time'
REQ_JOB_MAX_CURRENT_TIME = 'max_current_time'
REQ_JOB_MIN_GASFLOW = 'min_gasflow'
REQ_JOB_MAX_GASFLOW = 'max_gasflow'
REQ_JOB_MIN_WIREFEED = 'min_wirefeed'
REQ_JOB_MAX_WIREFEED = 'max_wirefeed'
REQ_JOB_MIN_VOLTAGE = 'min_voltage'
REQ_JOB_MAX_VOLTAGE = 'max_voltage'
REQ_JOB_CURRENT_MAX_RANGE = 'current_max_range'
REQ_JOBCREATED = 'jobcreated'
REQ_JOB_LOAD = 'load'
REQ_JOB_NOLOAD = 'noload'
REQ_WIRESIZE = 'wiresize'

# machinewarantydetails
REQ_WARRANTY_MACHINEID = 'machineid'
REQ_WARRANTY_STARTDATE = 'startdate'
REQ_WARRANTY_EXPITYDATE = 'expirydate'

# user prediction
REQ_INITIAL_STOCK = 'initialstock'
REQ_LAST_UPDATED = 'lastupdated'
REQ_USERPRED_MACHINEID = 'machineid'


# welder_machine_mapping
REQ_WELDER_MACHINE_MAPPING_MACHINEID = 'machineid'
REQ_WELDER_MACHINE_MAPPING_WELDERID = 'welderid'



# node_configuration
REQ_NODEADDR = 'nodeaddr'
REQ_GATEWAYMAC_ID = 'gateway_mac_id'
REQ_NODE_COMMISSION = 'commission'

# ticket_status_details
REQ_TICKET_MACHINEID = 'machineid'
REQ_TICKET_CAUSE = 'cause'
REQ_TICKET_REMARK = 'remark'
REQ_TICKET_SEVERITY = 'severity'
REQ_TICKET_STATUS = 'ticket_status'
REQ_TICKET_CLOSED_DATE = 'closed_date'
REQ_TICKET_REPORTED_DATE = 'reported_date'
REQ_TICKET_ID = 'ticketid'

# report_config
REQ_REPORTCONFIG_WELDER_DAILY_AVAILABLE = 'welder_daily_available'
REQ_REPORTCONFIG_WELDER_POWER_CONSUME = 'weld_power_consume'
REQ_REPORTCONFIG_POWER_RATE_UNIT = 'power_rate_unit'
REQ_REPORTCONFIG_IDLE_POWER_CONSUME = 'idle_power_consume'
REQ_REPORTCONFIG_DAILY_LABOUR_RATE = 'daily_labour_rate'
REQ_REPORTCONFIG_DAILY_SHIFT_HOUR = 'daily_shift_hour'
REQ_REPORTCONFIG_PAGENAME = 'page_name'

# gateway_configuration
REQ_GATEWAY_MAC_ID = 'gateway_macid'
REQ_GATEWAY_ID = 'gateway_id'
REQ_GATEWAY_COMMISSION = 'commission'
REQ_GATEWAY_USERID = 'userid'

# machine_input
REQ_MACHINE_INPUT_ID = 'machineid'
REQ_MACHINE_CYCLE_TIME = 'cycle_time'
REQ_MACHINE_PRODUCED = 'produced'
REQ_MACHINE_REJECTED = 'rejected'
REQ_MACHINE_TS = 'ts'











