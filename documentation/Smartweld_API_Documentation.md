# Smartweld API Documentation

## Description for all API’s
- Login
- User management
- Gateway
- Welder
- Machine
- Home
- Report
- predictions
- Configurations
- Nodes
- Tickets
## INDEX
| **SNO** | **MODULE NAME**                                                                                                                                                               | **API NAME**                                                                                                                                                                                | **METHOD** | **URL**                                                                                |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------- |
| 1       | [login_management](#Login)           | [authentication](#Login)        | POST       | /user/authenticate                                                                     |
| 2       | [user_management](#User Management)  | [user_add](#User add)           | POST       | /users                                                                                 |
|         |                                                                                                                                                                               | [user_update](#User update)     | PUT        | /users                                                                                 |
|         |                                                                                                                                                                               | [user_read_all](#Read all users)     | GET        | /users                                                                                 |
|         |                                                                                                                                                                               | [Read single user](#Read single user)                                                                                                                                                                             | GET           |/users/username                                                                                        |
|         |                                                                                                                                                                               | [user_delete](#User delete)     | DELETE     | /users/username                                                                        |
| 3       | [gateway](#Gateway)                                                                                                                                                                       | [gateway_add](#Gateway add)                                                                                                                                                                                | POST       | /gateways                                                                              |
|         |                                                                                                                                                                               | [gateway_update](#Gateway update)                                                                                                                                                                             | PUT        | /gateways/gatewayid                                                                    |
|         |                                                                                                                                                                               | [gateway_delete](#Delete selected gateway)                                                                                                                                                                              | DELETE     | /gateways/gatewayid                                                                    |
|         |                                                                                                                                                                               | [read_all_gateways](#Gateway read all)                                                                                                                                                                           | GET        | /gateways                                                                              |
|         |                                                                                                                                                                               | [read_selected_gateway](#Read single gateway)                                                                                                                                                                 | GET        | /gateways/gatewayid                                                                    |
| 4       | [welder](#Welder) | [welder_add](#Welder add)       | POST       | /welder/                                                                               |
|         |                                                                                                                                                                               | [welder_update](#Welder update) | PUT        | /welder/                                                                               |
|         |                                                                                                                                                                               | [welder_read](#Welder read)     | GET        | /welder/                                                                               |
|         |                                                                                                                                                                               | [welder_delete](#Welder delete) | DELETE     | /welder/4                                                                              |
|         |                                                                                                                                                                               | [add_welder_machine_mapping](#Add welder machine mapping)                                                                                                                                                                  | POST       | welder/mapping/                                                                        |
|         |                                                                                                                                                                               | [update_welder_machine_mapping](#Update welder machine mapping)                                                                                                                                                               | UPDATE     | welder/mapping/                                                                        |
|         |                                                                                                                                                                               | [read_welder_machine_mapping](#Read welder machine mapping)                                                                                                                                                                 | GET        | welder/mapping/                                                                        |
|         |                                                                                                                                                                               | [delete_welder_machine_mapping](#Delete welder machine mapping)                                                                                                                                                               | DELETE     | welder/mapping/2                                                                       |
|         |                                                                                                                                                                               | [unmapped_welder_machine_mapping](#Unmapped welder machine mapping)                                                                                                                                                         | GET        | welder/unmapped/                                                                       |
| 5       | [machine](#Machine configuration)                                                                                                                                                                       | [get live data](#Get live data) | GET        | /machines/get-live-data/mahcineid                                                      |
|         |                                                                                                                                                                               | [get report data](#Get report data)                                                                                                                                                                             | GET        | /machines/getlivereport?machineid=123456&startdate=1612522001000&enddate=1613374247000 |
|         |                                                                                                                                                                               | [get all machines](#Read all machines)                                                                                                                                                                            | GET        | /machines                                                                              |
|         |                                                                                                                                                                               | [get selected machine details](#Read selected machine)                                                                                                                                                                | GET        | /machines/56324                                                                        |
|         |                                                                                                                                                                               | [update selected machine details](#Machine update)                                                                                                                                                             | PUT        | /machines/331177                                                                       |
|         |                                                                                                                                                                               | [delete selected machine details](#Machine delete)                                                                                                                                                             | DELETE     | /machines/54                                                                           |
|         |                                                                                                                                                                               | [add new machine](#Machine add)                                                                                                                                                                             | POST       | /machines                                                                              |
|         |                                                                                                                                                                               | [upgrade warranty by machine](#Upgrade warranty by machine)                                                                                                                                                                 | PUT        | /machines/warranty/221144                                                              |
|         |                                                                                                                                                                               | [get warranty by machine](#Get machine warranty)                                                                                                                                                                     | GET        | /machines/warranty/331177                                                              |
|         |                                                                                                                                                                               | [update selected machine configuration](#Update selected machine configuration)                                                                                                                                                       | PUT        | /machines/config/331177                                                                |
|         |                                                                                                                                                                               | [upgrade wirefeed by machine](#Update wirefeed)                                                                                                                                                                 | PUT        | /machines/wirefeed/331177                                                              |
|         |                                                                                                                                                                               | [get wirefeed machine details](#Get wirefeed)                                                                                                                                                                | GET        | /machines/wirefeed/331177                                                              |
| 6       | [home](#Home)                                                                                                                                                                          | [get home overview](#Get home overview)                                                                                                                                                                           | GET        | /home/                                                                                 |
|         |                                                                                                                                                                               | [total wirefeed left](#Total wirefeed left)                                                                                                                                                                         | GET        | /home/wirefeed                                                                         |
|         |                                                                                                                                                                               | [get hourly](#Get hourly)                                                                                                                                                                                  | GET        | /home/hourly                                                                           |
| 7       | [report](#Report)                                                                                                                                                                        | [get report](#Report read)                                                                                                                                                                                  | GET        | /reports                                                                               |
|         |                                                                                                                                                                               | [get power analysis](#Get Power Report)                                                                                                                                                                          | GET        | /reports/poweranalysis                                                                 |
|         |                                                                                                                                                                               | [get daily report](#Daily Report)                                                                                                                                                                            | GET        | /reports/machineid                                                                     |
| 8       | [predictions](#Predictions)                                                                                                                                                                   | [get warranty predictions](#Get warranty predictions)                                                                                                                                                                    | GET        | /predictions/warranty                                                                  |
|         |                                                                                                                                                                               | [get wirefeed predictions](#Get wirefeed predictions)                                                                                                                                                                    | GET        | /predictions/wirefeed                                                                  |
|         |                                                                                                                                                                               | [get all fault](#Get all faults)                                                                                                                                                                               | GET        | /predictions/fault                                                                     |
|         |                                                                                                                                                                               | [get fault by date](#Get fault by date)                                                                                                                                                                           | GET        | /predictions/fault/machineid                                                           |
| 9       | [Configurations](Configurations)                                                                                                                                                                | [get machine input](#Get machine input)                                                                                                                                                                           | GET        | /configurations/                                                                       |
|         |                                                                                                                                                                               | [add new machine input](#Add new machine input)                                                                                                                                                                       | POST       | /configurations/                                                                       |
|         |                                                                                                                                                                               | [get report configuration](#Get report configuration)                                                                                                                                                                           | GET        | /configurations/report/                                                                |
|         |                                                                                                                                                                               | [update report configuration](#Update report configuration)                                                                                                                                                                        | PUT        | /configurations/report                                                                 |
| 10      | [nodes](#Nodes)                                                                                                                                                                         | [get all nodes](#Get all nodes)                                                                                                                                                                               | GET        | /nodes/u101                                                                            |
|         |                                                                                                                                                                               | [get node by id](#Get selected node)                                                                                                                                                                              | GET        | /nodes/0x124b001be46202                                                                |
|         |                                                                                                                                                                               | [add new node](#Add new node)                                                                                                                                                                                | POST       | /nodes                                                                                 |
|         |                                                                                                                                                                               | [update node by id](#Update node by id)                                                                                                                                                                           | PUT        | /nodes/0x124b001be46202                                                                |
|         |                                                                                                                                                                               | [delete node](#Delete node)                                                                                                                                                                                 | DELETE     | /nodes/0x124b001be46200                                                                |
| 11      | [tickets](#Tickets)                                                                                                                                                                       | [add new ticket](#Add ticket)                                                                                                                                                                              | POST       | /tickets/                                                                              |
|         |                                                                                                                                                                               | [update selected tikcet details](#Update ticket details)                                                                                                                                                              | PUT        | /tickets/3                                                                             |
|         |                                                                                                                                                                               | [get all tickets](#Get all tickets)                                                                                                                                                                             | GET        | /tickets/getalltickets                                                                 |
|         |                                                                                                                                                                               | [get selected ticket details](#Get selected ticket)                                                                                                                                                                 | GET        | /tickets                                                                               |
|         |                                                                                                                                                                               | [get all live ticket details](#Get all live tickets)                                                                                                                                                                 | GET        | /tickets/getliveticket                                                                 |



## **Login<a name="Login"></a>**


    Method: POST
    URL: /login

**Parameters**

| **Field** | **Datatype** | **Description**     |
| --------- | ------------ | ------------------- |
| username  | String       | Registered username |
| password  | String       | Registered password |


**Success 200 OK**

| **Field** | **Datatype** | **Description**                                 |
| --------- | ------------ | ----------------------------------------------- |
| Token     | String       | If login successfull response will be jwt token |

**Response Example**


    {
        "userid": "admin",
        "role": 1,
        "status": true,
        "new token": {
            "token": "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyaWQiOiJhZG1pbiIsImZpcnN0bmFtZSI6ImFkbWluIiwibGFzdG5hbWUiOiJNIiwidXNlcm5hbWUiOiJhZG1pbiIsImFnZSI6MzAsImdlbmRlciI6Im1hbGUiLCJyb2xlIjoxLCJlbnRpdHlfaWQiOjEsInN0YXR1cyI6dHJ1ZSwicGVybWlzc2lvbiI6eyJyZWFkIjp0cnVlLCJjcmVhdGUiOnRydWUsInVwZGF0ZSI6dHJ1ZSwiZGVsZXRlIjp0cnVlLCJkb3dubG9hZCI6dHJ1ZSwidmlldyI6dHJ1ZX0sImV4cCI6MTYxMTgzOTUzNH0.F-gT73n0mLM_c0taydsmM_otxAd5HhvRmst9f9Zqt7s'"
        }
    }                                                                      

**Error**

| **Field**     | **Description**                | **Status**    |
| ------------- | ------------------------------ | ------------- |
| Unauthorized  | User is not registered with us | 403 Forbidden |
| Error         | Password is not correct        | 403 Forbidden |
| Request error | Wrong request error            |               |

**Error example**


    HTTP/1.1 403 Forbidden
    {
        "message": "Username is not registered with us"
    }


    HTTP/1.1 403 Forbidden
    {
        "message": "Password is not correct"
    }


    HTTP/1.1 403 Forbidden
    {
        "message": "Wrong Request Error"
    }
# User Management<a name="User Management"></a>

**User_mangement description:**


    User API's
    1. user_add
    2. user_update
    3. user_read_all
    4. user_delete
    5. single_user_read


## User add<a name="User add"></a>


    Method : POST
    URL: /users  

**Parameters**

| Field          | Datatype | Description        |
| -------------- | -------- | ------------------ |
| firstname      | String   | User first name    |
| lastname       | String   | User last name     |
| age            | Integer  | Age of user        |
| city           | String   | user city          |
| contact_number | Integer  | user phone number  |
| country        | String   | country            |
| gender         | String   | gender of user     |
| mail_id        | String   | user mail id       |
| username       | String   | username for login |
| password       | String   | password for login |
| pincode        | Integer  | pincode            |
| role           | Integer  | role               |
| state          | String   | state              |
| status         | Boolean  | status             |

**Parameters Example:**


    {
        "age":22,
        "city":"BGR",
        "contact_number":9632587410,
        "country":"India",
        "firstname":"vijaya",
        "gender":"female",
        "lastname":"durga",
        "mail_id":"vijaya123@gmail.com",
        "password":"vijaya@123",
        "pincode":72486,
        "role":1,
        "state":"Karnataka",
        "status":true,
        "username":"vijaya1"
    }
    

**Response:** Success 200 OK
 

    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## User update<a name="User update"></a>


    Method : PUT
    URL: /users/admin

**Parameters**

| **Field**      | **Datatype** | **Description**     |
| -------------- | ------------ | ------------------- |
| age            | Integer      | age of the user     |
| city           | String       | city of user        |
| contact_number | Integer      | user contact number |
| country        | String       | user country        |
| firstname      | String       | firstname if user   |
| gender         | String       | user gender         |
| lastname       | String       | lastname of user    |
| mail_id        | String       | user mail id        |
| pincode        | Integer      | user pincode        |
| role           | Integer      | role of user        |
| state          | String       | state of user       |
| status         | Boolean      | status of user      |
| username       | String       | username of user    |

**Parameters example:**


    {
        "age":23,
        "city":"BGR",
        "contact_number":9632587410,
        "country":"India",
        "firstname":"vijaya",
        "gender":"female",
        "lastname":"durga",
        "mail_id":"vijaya123@gmail.com",
        "pincode":72486,
        "role":1,
        "state":"Karnataka",
        "status":true,
        "username":"vijaya1"
    }
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Read all users<a name="Read all users"></a>


    Method : GET
    URL: /users

**Response:** Success 200 OK

| Field          | Datatype | Description               |
| -------------- | -------- | ------------------------- |
| userid         | String   | role of user              |
| age            | Integer  | age of user               |
| city           | String   | user city                 |
| contact_number | Integer  | user contact number       |
| country        | String   | user country              |
| firstname      | String   | firstname of user         |
| gender         | String   | user gender               |
| lastname       | String   | lastname of user          |
| mail id        | String   | mail id of  user          |
| picode         | Integer  | user pincode              |
| role           | Integer  | user role                 |
| state          | String   | user state                |
| status         | Boolean  | user active               |
| username       | String   | name of user              |
| entity_id      | Integer  | userid related to company |

**Response example:**


    [
        {
            "userid": "admin",
            "age": 30,
            "city": "Narsapur",
            "contact_number": 9632147850,
            "country": "India",
            "firstname": "admin",
            "gender": "male",
            "lastname": "M",
            "mail_id": "admin@gmail.com",
            "pincode": 462006,
            "role": 1,
            "state": "Karnataka",
            "status": true,
            "username": "admin",
            "entity_id": 1
        },
        {
            "userid": "admin",
            "age": 22,
            "city": "BGR",
            "contact_number": 9632587410,
            "country": "India",
            "firstname": "vijaya",
            "gender": "female",
            "lastname": "durga",
            "mail_id": "vijaya123@gmail.com",
            "pincode": 72486,
            "role": 1,
            "state": "Karnataka",
            "status": true,
            "username": "vijaya",
            "entity_id": 1
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Read single user<a name="Read single user"></a>


    Method : GET
    URL: /users/admin

**Response:** Success 200 OK

| Field          | Datatype | Description               |
| -------------- | -------- | ------------------------- |
| userid         | String   | role of user              |
| age            | Integer  | age of user               |
| city           | String   | user city                 |
| contact_number | Integer  | user contact number       |
| country        | String   | user country              |
| firstname      | String   | firstname of user         |
| gender         | String   | user gender               |
| lastname       | String   | lastname of user          |
| mail id        | String   | mail id of  user          |
| picode         | Integer  | user pincode              |
| role           | Integer  | user role                 |
| state          | String   | user state                |
| status         | Boolean  | user active               |
| username       | String   | name of user              |
| entity_id      | Integer  | userid related to company |

Response: Success 200 OK

| **Field** | **Description**                 |
| --------- | ------------------------------- |
| Success   | Retrive particular user details |

**Response example:**


    [
        {
            "username": "admin",
            "age": 22,
            "city": "BGR",
            "contact_number": 9632587410,
            "country": "India",
            "firstname": "vijaya",
            "lastname": "durga",
            "gender": "female",
            "mail_id": "vijaya123@gmail.com",
            "password": "admin@123",
            "pincode": 72486,
            "role": 1,
            "state": "Karnataka",
            "entity_id": 1,
            "userid": "admin",
            "status": true,
            "user_id": 1
        },
        {
            "username": "vijayadurga",
            "age": 22,
            "city": "BGR",
            "contact_number": 9632587410,
            "country": "India",
            "firstname": "vijaya",
            "lastname": "durga",
            "gender": "female",
            "mail_id": "vijaya123@gmail.com",
            "password": "vijaya@111",
            "pincode": 72486,
            "role": 1,
            "state": "Karnataka",
            "entity_id": 1,
            "userid": "admin",
            "status": true,
            "user_id": 6
        },
        {
            "username": "durga",
            "age": 22,
            "city": "BGR",
            "contact_number": 9632587410,
            "country": "India",
            "firstname": "vijaya",
            "lastname": "durga",
            "gender": "female",
            "mail_id": "vijaya123@gmail.com",
            "password": "vijaya@111",
            "pincode": 72486,
            "role": 1,
            "state": "Karnataka",
            "entity_id": 1,
            "userid": "admin",
            "status": true,
            "user_id": 7
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }
## User delete<a name="User delete"></a>


    Method: DELETE
    URL: /users/admin

**URL parameters:**

| **Field** | **Datatype** | **Description**     |
| --------- | ------------ | ------------------- |
| username  | String       | username for delete |

**Parameter Example:**


    /users/admin

**Response:** Success 200 OK


    Success 200 OK
    {
        "message": "Deleted Successfully"
    }

**Error:**

| Field        | Description                    | Status        |
| ------------ | ------------------------------ | ------------- |
| Permission   | If tokens get permission error | 403 Forbidden |
| Unauthorized | User not have read permission  | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    403 Forbidden
    {
      "message":"unauthorized"
    }


# Configurations<a name="Configurations"></a>
## Add new machine input<a name="Add new machine input"></a>


    Method : POST
    URL: /configurations/

**Parameters**

| Field      | Datatype | Description       |
| ---------- | -------- | ----------------- |
| cycle_time | String   | mac id of gateway |
| produced   | String   | id of gateway     |
| rejected   | Integer  | commission        |
| entity_id  | String   | user id           |

**Request body Example:**


   {
    "machineid":22222,
    "ts":1612789459000,
    "cycle_time":40,
    "produced":1000,
    "rejected":10
}
    
    

**Response:** Success 200 OK
 

    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## Get machine input<a name="Get machine input"></a>


    Method : GET
    URL: /configurations/

**Response:** Success 200 OK

| Field      | Datatype | Description        |
| ---------- | -------- | ------------------ |
| machineid  | Integer  | machine id         |
| ts         | Big int  | ts                 |
| cycle_time | Integer  | cycle time         |
| produced   | Integer  | number of produced |
| rejected   | Integer  | number of rejected |

**Response example:**


    [
        {
            "json_agg": [
                {
                    "machineid": 331177,
                    "ts": 1612778164000,
                    "cycle_time": 49,
                    "produced": 1200,
                    "rejected": 3
                },
                {
                    "machineid": 123456,
                    "ts": 1612778164000,
                    "cycle_time": 30,
                    "produced": 1200,
                    "rejected": 3
                }
            ]
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get report configuration<a name="Get report configuration"></a>


    Method : GET
    URL: /configurations/report/

**Response:** Success 200 OK

| Field                  | Datatype | Description            |
| ---------------------- | -------- | ---------------------- |
| welder_daily_available | Integer  | daily available welder |
| weld_power_consume     | Big int  | welder power consume   |
| power_rate_unit        | Integer  | power rate unit        |
| idle_power_consume     | Integer  | idle power consume     |
| daily_labour_rate      | Integer  | daily labour rate      |
| daily_shift_hour       | Integer  | daily shift hours      |

**Response example:**


    [
        {
            "json_build_object": {
                "welder_daily_available": 20,
                "weld_power_consume": 12,
                "power_rate_unit": 11,
                "idle_power_consume": 11,
                "daily_labour_rate": 444,
                "daily_shift_hour": 11
            }
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Update Report configuration<a name="Update report configuration"></a>


    Method : PUT
    URL: /configurations/report/

**Parameters**

| **Field**              | **Datatype** | **Description**        |
| ---------------------- | ------------ | ---------------------- |
| welder_daily_available | Integer      | daily available welder |
| weld_power_consume     | Big int      | welder power consume   |
| power_rate_unit        | Integer      | power rate unit        |
| idle_power_consume     | Integer      | idle power consume     |
| daily_labour_rate      | Integer      | daily labour rate      |
| daily_shift_hour       | Integer      | daily shift hours      |

**Parameters example:**


    {
        "welder_daily_available": 20,
        "weld_power_consume": 12,
        "power_rate_unit": 11,
        "idle_power_consume": 11,
        "daily_labour_rate": 444,
        "daily_shift_hour": 11
            
    }
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }
# Gateway<a name="Gateway"></a>
    gatewayAPI's
    1. gateway_add
    2. gateway_update
    3. gateway_read_all
    4. read_selected_gateway
    4. gateway_delete


## Gateway add<a name="Gateway add"></a>


    Method : POST
    URL: /gateways  

**Parameters**

| Field         | Datatype | Description       |
| ------------- | -------- | ----------------- |
| gateway_macid | String   | mac id of gateway |
| gateway_id    | String   | id of gateway     |
| commission    | Integer  | commission        |
| userid        | String   | user id           |

**Parameters Example:**


    {
        "gateway_macid":"04:a2:1d:5d:w4:15",
        "gateway_id":"u103",
        "commission":1,
        "userid":"admin"
    }
    

**Response:** Success 200 OK
 

    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## Gateway update<a name="Gateway update"></a>


    Method : PUT
    URL: /gateways/u103

**Parameters**

| **Field**     | **Datatype** | **Description** |
| ------------- | ------------ | --------------- |
| gateway_macid | String       | gateway mac id  |
| commission    | Integer      | commission      |
| userid        | String       | user id         |

**Parameters example:**


    {
        "gateway_macid":"04:a3:16:b0:ec:12",
        "commission":1,
        "userid":"admin"
    }
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Gateway read all<a name="Gateway read all"></a>


    Method : GET
    URL: /gateways

**Response:** Success 200 OK

| Field      | Datatype | Description |
| ---------- | -------- | ----------- |
| gateway_id | String   | gateway id  |
| commission | Integer  | commission  |

**Response example:**


    [
        {
            "gateway_id": "u101",
            "commission": 1
        },
        {
            "gateway_id": "u102",
            "commission": 1
        },
        {
            "gateway_id": "u103",
            "commission": 1
        },
        {
            "gateway_id": "u104",
            "commission": 1
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Read single gateway<a name="Read single gateway"></a>


    Method : GET
    URL: /gateways/u102

**Response:** Success 200 OK

| Field      | Datatype | Description |
| ---------- | -------- | ----------- |
| gateway_id | String   | gateway id  |

Response: Success 200 OK

| **Field** | **Description**                 |
| --------- | ------------------------------- |
| Success   | Retrive particular user details |

**Response example:**


    [
        {
            "gateway_macid": "04:a2:1d:5d:w4:15"
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Delete selected gateway<a name="Delete selected gateway"></a>


    Method: DELETE
    URL: /gateways/u103

**URL parameters:**

| **Field**  | **Datatype** | **Description**       |
| ---------- | ------------ | --------------------- |
| gateway_id | String       | gateway id for delete |

**Parameter Example:**


    /gateways/u103

**Response:** Success 200 OK


    Success 200 OK
    {
        "message": "Deleted Successfully"
    }

**Error:**

| Field        | Description                    | Status        |
| ------------ | ------------------------------ | ------------- |
| Permission   | If tokens get permission error | 403 Forbidden |
| Unauthorized | User not have read permission  | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    403 Forbidden
    {
      "message":"unauthorized"
    }
# Welder<a name="Welder"></a>


    Welder API's
    1. Welder_add
    2. Welder_update
    3. Welder_read
    4. Welder_delete
    5. add_welder_machine_mapping
    6. update_welder_machine_mapping
    7. delete_welder_machine_mapping
    8. unmapped_welder_machine_mapping
# Welder add<a name="Welder add"></a>


    Method: POST
    URL: /welder/

**Parameters:**

| Field       | Datatype | Description           |
| ----------- | -------- | --------------------- |
| firstname   | String   | firstname of welder   |
| lastname    | String   | lastname of welder    |
| age         | Integer  | age of welder         |
| phone       | Integer  | welder phone number   |
| proficiency | String   | proficiency of welder |
| gender      | String   | welder gender         |

**Parameters Example:**


    {
        "firstname":"ajay",
        "lastname":"m",
        "age":27,
        "phone":9876543560,
        "proficiency":"intermediate",
        "gender":"male"    
    }

**Response:** Success 200 OK


    Success 200 OK
    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**                | **Status**    |
| ------------ | ------------------------------ | ------------- |
| Unauthorized | User is not authorized         | 403 Forbidden |
| Permission   | If tokens get permission error | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


    403 Forbidden
    {
        "message": "'permission'"
    }


## Welder update<a name="Welder update"></a>


    Method: PUT
    URL: /welder/

**Parameters:**

| Field       | Datatype | Description         |
| ----------- | -------- | ------------------- |
| firstname   | String   | firstname of welder |
| lastname    | String   | lastname of welder  |
| age         | Integer  | age of weldere      |
| phone       | Integer  | welder phone number |
| proficiency | String   | welder proficiency  |
| gender      | String   | gender of welder    |
| id          | Integer  | Id of updating user |

**Parameters Example:**


    {
        "firstname":"syam",
        "lastname":"m",
        "age":40,
        "phone":9876543560,
        "proficiency":"intermediate",
        "gender":"female",
        "id":3
    }

**Response:** Success 200 OK

| **Field** | **Description**      |
| --------- | -------------------- |
| Success   | Updated successfully |

**Response Example**


    Success 200 OK
    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**                | **Status**    |
| ------------ | ------------------------------ | ------------- |
| Unauthorized | User is not authorized         | 403 Forbidden |
| Permission   | If tokens get permission error | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


    403 Forbidden
    {
        "message": "'permission'"
    }


## Welder read<a name="Welder read"></a>


    Method : GET
    URL: /welder/

**Response:** Success 200 OK

| Field       | Datatype | Description         |
| ----------- | -------- | ------------------- |
| firstname   | String   | firstname of welder |
| lastname    | String   | lastname of welder  |
| age         | Integer  | age of weldere      |
| phone       | Integer  | welder phone number |
| proficiency | String   | welder proficiency  |
| gender      | String   | gender of welder    |
| id          | Integer  | Id of updating user |

**Response example:**


    [
        {
            "firstname": "vijaya",
            "lastname": "durga",
            "age": 21,
            "phone": 9632154780,
            "proficiency": "intermediate",
            "gender": "female",
            "id": 1
        },
        {
            "firstname": "syam",
            "lastname": "m",
            "age": 25,
            "phone": 9876543560,
            "proficiency": "intermediate",
            "gender": "male",
            "id": 2
        }
    ]

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Permission   | User is not authorized | 403 Forbidden |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## Welder delete<a name="Welder delete"></a>


    Method: DELETE
    URL: /welder/2

**URL parameters:**

| **Field** | **Datatype** | **Description** |
| --------- | ------------ | --------------- |
| id        | Integer      | id for delete   |

**Parameter Example:**


    /welder/2

**Response:** Success 200 OK

| **Field** | **Description**      |
| --------- | -------------------- |
| Success   | Deleted Successfully |

**Response Example:**


    Success 200 OK
    {
        "message": "Deleted Successfully"
    }

**Error:**

| Field        | Description                    | Status        |
| ------------ | ------------------------------ | ------------- |
| Permission   | If tokens get permission error | 403 Forbidden |
| Unauthorized | User not have read permission  | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    403 Forbidden
    {
      "message":"unauthorized"
    }


## Add welder machine mapping<a name="Add welder machine mapping"></a>


    Method: POST
    URL: /welder/mapping/

**Parameters:**

| Field     | Datatype | Description |
| --------- | -------- | ----------- |
| machineid | Integer  | machineid   |
| welderid  | integer  | welderid    |

**Parameters Example:**


    {
        "machineid":331177,
        "welderid":3
    }

**Response:** Success 200 OK


    Success 200 OK
    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**                | **Status**    |
| ------------ | ------------------------------ | ------------- |
| Unauthorized | User is not authorized         | 403 Forbidden |
| Permission   | If tokens get permission error | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


    403 Forbidden
    {
        "message": "'permission'"
    }


## Update welder machine mapping<a name="Update welder machine mapping"></a>


    Method: PUT
    URL: /welder/mapping/

**Parameters:**

| Field     | Datatype | Description |
| --------- | -------- | ----------- |
| machineid | Integer  | machine id  |
| welderid  | Integer  | welder id   |

**Parameters Example:**


    {
        "machineid":331177,
        "welderid":2
    }

**Response:** Success 200 OK

| **Field** | **Description**      |
| --------- | -------------------- |
| Success   | Updated successfully |

**Response Example**


    Success 200 OK
    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**                | **Status**    |
| ------------ | ------------------------------ | ------------- |
| Unauthorized | User is not authorized         | 403 Forbidden |
| Permission   | If tokens get permission error | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


    403 Forbidden
    {
        "message": "'permission'"
    }


## Read welder machine mapping<a name="Read welder machine mapping"></a>


    Method : GET
    URL: /welder/mapping/

**Response:** Success 200 OK

| Field           | Datatype | Description     |
| --------------- | -------- | --------------- |
| machineid       | Integer  | machine id      |
| welderid        | Integer  | welder id       |
| machine_tagname | String   | macine tag name |
| firstname       | String   | first name      |
| lastname        | String   | last name       |

**Response example:**


    [
        {
            "machineid": 1111,
            "welderid": 2,
            "machine_tagname": "L1M1",
            "firstname": "syam1",
            "lastname": "m"
        },
        {
            "machineid": 331177,
            "welderid": 2,
            "machine_tagname": "L4M4",
            "firstname": "syam1",
            "lastname": "m"
        },
        {
            "machineid": 1111,
            "welderid": 3,
            "machine_tagname": "L1M1",
            "firstname": null,
            "lastname": null
        }
    ]

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Permission   | User is not authorized | 403 Forbidden |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"


## Delete welder machine mapping<a name="Delete welder machine mapping"></a>


    Method: DELETE
    URL: /welder/mapping/2

**URL parameters:**

| **Field** | **Datatype** | **Description**      |
| --------- | ------------ | -------------------- |
| welderid  | Integer      | welder id for delete |

**Parameter Example:**


    /welder/2

**Response:** Success 200 OK

| **Field** | **Description**      |
| --------- | -------------------- |
| Success   | Deleted Successfully |

**Response Example:**


    Success 200 OK
    {
        "message": "Deleted Successfully"
    }

**Error:**

| Field        | Description                    | Status        |
| ------------ | ------------------------------ | ------------- |
| Permission   | If tokens get permission error | 403 Forbidden |
| Unauthorized | User not have read permission  | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    403 Forbidden
    {
      "message":"unauthorized"
    }

## Unmapped welder machine mapping<a name="Unmapped welder machine mapping"></a>


    Method : GET
    URL: welder/unmapped/

**Response:** Success 200 OK

| Field   | Datatype | Description |
| ------- | -------- | ----------- |
| welder  | Integer  | welder      |
| machine | Integer  | machine     |

**Response example:**


    {
        "welder": [],
        "machine": []
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Permission   | User is not authorized | 403 Forbidden |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
# Machine configuration<a name="Machine configuration"></a>
## Machine add<a name="Machine add"></a>


    Method : POST
    URL: /machines 

**Parameters**

| Field               | Datatype | Description             |
| ------------------- | -------- | ----------------------- |
| machineid           | Integer  | Machine id              |
| buyer_company       | String   | buyer company name      |
| city                | String   | user city               |
| country             | String   | country                 |
| date_of_manufacture | Big int  | date of manufacture     |
| latitude            | Integer  | latitude value          |
| longitude           | Integer  | longitude value         |
| model               | String   | model of machine        |
| pincode             | Integer  | pincode                 |
| saledate            | Big int  | sale date               |
| sensor_nodeid       | String   | node id of sensor       |
| state               | String   | state of user           |
| userid              | String   | user role               |
| opvolt              | Integer  | opvolt                  |
| jobid               | Integer  | job id                  |
| minthreshold        | Integer  | minimum threshold value |
| maxthreshold        | Integer  | maximum threshold value |
| min_current_time    | Integer  | minimum current time    |
| max_current_time    | Integer  | maximum current time    |
| current_max_range   | Integer  | maximum current range   |
| min_voltage         | Integer  | minimum voltage value   |
| max_voltage         | Integer  | maximum voltage value   |
| min_wirefeed        | Integer  | minimum wirefeed value  |
| max_wirefeed        | Integer  | maximum wirefeed value  |
| min_gasflow         | Integer  | minimum gas flow        |
| max_gasflow         | Integer  | maximum gas flow        |
| jobcreated          | Big int  | job created time        |

**Parameters Example:**


    {
        "machineid":221144,
        "buyer_company":"IRM",
         "city":"BGR",
        "country":"India",
        "latitude":66.2,
        "longitude":77.2,
         "model":"LM21",
        "pincode":5342100,
        "saledate":1612364244000,
        "sensor_nodeid":"0x124b001a52cfd3",
        "state":"Karnataka",
        "userid":"manager",
        "machine_tagname":"L4M4",
        "sensornode_id":"12",
        "jobid":2,
        "opvolt":10,
        "minthreshold":300,
        "maxthreshold":500,
        "min_current_time":500,
        "max_current_time":600,
        "current_max_range":450,
        "min_voltage":18,
        "max_voltage":24,
        "min_wirefeed":2,
        "max_wirefeed":5,
        "min_gasflow":23,
        "max_gasflow":34
    }
    
    

**Response:** Success 200 OK
 

    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## Machine update<a name="Machine update"></a>


    Method : PUT
    URL: /machines/machineid

**Parameters**

| Field               | Datatype | Description             |
| ------------------- | -------- | ----------------------- |
| buyer_company       | String   | buyer company name      |
| city                | String   | user city               |
| country             | String   | country                 |
| date_of_manufacture | Big int  | date of manufacture     |
| latitude            | Integer  | latitude value          |
| longitude           | Integer  | longitude value         |
| model               | String   | model of machine        |
| pincode             | Integer  | pincode                 |
| saledate            | Big int  | sale date               |
| sensor_nodeid       | String   | node id of sensor       |
| state               | String   | state of user           |
| userid              | String   | user role               |
| jobid               | Integer  | job id                  |
| minthreshold        | Integer  | minimum threshold value |
| maxthreshold        | Integer  | maximum threshold value |
| min_current_time    | Integer  | minimum current time    |
| max_current_time    | Integer  | maximum current time    |
| current_max_range   | Integer  | maximum current range   |
| min_voltage         | Integer  | minimum voltage value   |
| max_voltage         | Integer  | maximum voltage value   |
| min_wirefeed        | Integer  | minimum wirefeed value  |
| max_wirefeed        | Integer  | maximum wirefeed value  |
| min_gasflow         | Integer  | minimum gas flow        |
| max_gasflow         | Integer  | maximum gas flow        |
| jobcreated          | Big int  | job created time        |

**Parameters example:**


    {
        "buyer_company":"HS",
         "city":"BGR",
        "country":"India",
        "date_of_manufacture":1612255697000,
        "latitude":66.2,
        "longitude":77.2,
         "model":"LM21",
        "pincode":5342100,
        "saledate":1612171287000,
        "sensor_nodeid":"0x124b001a52cfd3",
        "state":"Karnataka",
        "userid":"manager",
        "jobid":2,
        "minthreshold":300,
        "maxthreshold":500,
        "min_current_time":500,
        "max_current_time":600,
        "current_max_range":450,
        "min_voltage":20,
        "max_voltage":30,
        "min_wirefeed":2,
        "max_wirefeed":5,
        "min_gasflow":23,
        "max_gasflow":34,
        "jobcreated":1612255697000
    }
    
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Read all machines<a name="Read all machines"></a>


    Method : GET
    URL: /machines

**Response:** Success 200 OK

| Field             | Datatype | Description           |
| ----------------- | -------- | --------------------- |
| id                | Integer  | unique id             |
| machineid         | Integer  | machine id            |
| gateway_id        | String   | gateway unique id     |
| gatewaymac_id     | String   | gateway mac id        |
| sensornode_id     | String   | sensor id             |
| node_mac_id       | String   | node mac address      |
| machine_model     | String   | machine model         |
| min_current       | Integer  | minimum current       |
| max_current       | Integer  | maximum current       |
| max_current_range | Integer  | maximum xurrent range |
| min_voltage       | Integer  | minimum voltage       |
| max_voltage       | Integer  | maximum voltage       |
| min_wirefeed      | Integer  | minimum wirefeed      |
| max_wirefeed      | Integer  | maximum wirefeed      |
| min_gasflow       | Integer  | minimum gasflow       |
| max_gasflow       | Integer  | maximum gasflow       |

**Response example:**


    [
        {
            "id": 1,
            "machineid": 123456,
            "gateway_id": "u102",
            "gatewaymac_id": "04:a2:1d:5d:w4:41",
            "sensornode_id": "12",
            "node_mac_id": "04:a2:1d:5d:w4:41",
            "machine_model": "L2M5",
            "min_current": 500,
            "max_current": 600,
            "max_current_range": 450.0,
            "min_voltage": 18.0,
            "max_voltage": 24.0,
            "min_wirefeed": 2.0,
            "max_wirefeed": 5.0,
            "min_gasflow": 23.0,
            "max_gasflow": 34.0
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Read selected machine<a name="Read selected machine"></a>


    Method : GET
    URL: /machines/10102

**Response:** Success 200 OK

| Field               | Datatype | Description             |
| ------------------- | -------- | ----------------------- |
| machineid           | Integer  | unique machineid        |
| buyer_company       | String   | buyer company name      |
| city                | String   | user city               |
| country             | String   | country                 |
| date_of_manufacture | Big int  | date of manufacture     |
| latitude            | Integer  | latitude value          |
| longitude           | Integer  | longitude value         |
| model               | String   | model of machine        |
| pincode             | Integer  | pincode                 |
| saledate            | Big int  | sale date               |
| sensor_nodeid       | String   | node id of sensor       |
| state               | String   | state of user           |
| userid              | String   | user role               |
| jobid               | Integer  | job id                  |
| minthreshold        | Integer  | minimum threshold value |
| maxthreshold        | Integer  | maximum threshold value |
| min_current_time    | Integer  | minimum current time    |
| max_current_time    | Integer  | maximum current time    |
| current_max_range   | Integer  | maximum current range   |
| min_voltage         | Integer  | minimum voltage value   |
| max_voltage         | Integer  | maximum voltage value   |
| min_wirefeed        | Integer  | minimum wirefeed value  |
| max_wirefeed        | Integer  | maximum wirefeed value  |
| min_gasflow         | Integer  | minimum gas flow        |
| max_gasflow         | Integer  | maximum gas flow        |
| jobcreated          | Big int  | job created time        |
| load                | Integer  | load                    |
| noload              | Integer  | noload                  |
| wiresize            | Integer  | wiresize                |

**Response example:**


    [
        {
            "machineid": 10102,
            "buyer_company": "IRM",
            "city": "BGR",
            "country": "India",
            "latitude": 66.2,
            "longitude": 77.2,
            "model": "LM21",
            "pincode": 5342100,
            "sensor_nodeid": "0x124b001a52cfd3",
            "state": "Karnataka",
            "userid": "manager",
            "machine_tagname": "L4M4",
            "date_of_manufacture": 1613449660602,
            "saledate": 1612364244000,
            "entity_id": 1,
            "jobid": 2,
            "opvolt": 10.0,
            "minthreshold": 300.0,
            "maxthreshold": 500.0,
            "min_current_time": 500,
            "max_current_time": 600,
            "min_gasflow": 23.0,
            "max_gasflow": 34.0,
            "min_wirefeed": 2.0,
            "max_wirefeed": 5.0,
            "min_voltage": 18.0,
            "max_voltage": 24.0,
            "current_max_range": 450.0,
            "jobcreated": 1613449663016,
            "load": 5,
            "noload": 5,
            "wiresize": 10
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }
## Machine delete<a name="Machine delete"></a>


    Method: DELETE
    URL: /machines/machineid

**URL parameters:**

| **Field** | **Datatype** | **Description**      |
| --------- | ------------ | -------------------- |
| machineid | Integer      | machineid for delete |

**Parameter Example:**


    /machines/554456

**Response:** Success 200 OK


    Success 200 OK
    {
        "message": "Deleted Successfully"
    }

**Error:**

| Field        | Description                    | Status        |
| ------------ | ------------------------------ | ------------- |
| Permission   | If tokens get permission error | 403 Forbidden |
| Unauthorized | User not have read permission  | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    403 Forbidden
    {
      "message":"unauthorized"
    }


## Get live data<a name="Get live data"></a>


    Method : GET
    URL: machines/get-live-data/56324

**Response:** Success 200 OK

| Field        | Datatype | Description     |
| ------------ | -------- | --------------- |
| gasflow      | Real     | gas flow        |
| jobid        | Integer  | job id          |
| latitude     | Real     | latitude value  |
| longitude    | Real     | longitude value |
| mac_address  | String   | mac address     |
| node_id      | String   | node id         |
| status       | Integer  | status          |
| voltage      | Real     | voltage         |
| current      | Real     | current         |
| digital_1    | Integer  | digital value 1 |
| digital_2    | Integer  | digital value 2 |
| feedrate     | Real     | feed rate       |
| machineid    | Integer  | machine id      |
| timeinstance | Big int  | time instance   |
| node_address | String   | node address    |
| entity_id    | Integer  | entity id       |

**Response example:**


    [
        {
            "gasflow": 33.9,
            "jobid": 1,
            "latitude": 12.34,
            "longitude": 77.63,
            "mac_address": "04:a3:16:b0:ec:13",
            "node_id": "0x124b001be21029",
            "status": 2,
            "voltage": 85.0,
            "current": 39.0,
            "digital_1": 1,
            "digital_2": 1,
            "feedrate": 3.38,
            "machineid": 56324,
            "timeinstance": 1610348425807,
            "node_address": "0x124b001be21029",
            "entity_id": 1
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Upgrade warranty by machine<a name="Upgrade warranty by machine"></a>


    Method : PUT
    URL: /machines/warranty/221144

**Parameters**

| Field      | Datatype | Description |
| ---------- | -------- | ----------- |
| expirydate | Big int  | expiry date |

**Parameters example:**


    {
        "expirydate": 1612765872000
    }
    
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Get machine warranty<a name="Get machine warranty"></a>


    Method : GET
    URL: /machines/warranty/331177

**Response:** Success 200 OK

| Field      | Datatype | Description |
| ---------- | -------- | ----------- |
| machine id | Integer  | unique id   |
| sale date  | Big int  | sale dtae   |
| expirydate | Big int  | expiry date |

**Response example:**


    [
        {
            "machineid": 331177,
            "saledate": 1612259791625,
            "expirydate": 1613123791653
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get wirefeed<a name="Get wirefeed"></a>


    Method : GET
    URL: /machines/wirefeed/331177

**Response:** Success 200 OK

| Field        | Datatype | Description       |
| ------------ | -------- | ----------------- |
| machine id   | Integer  | unique id         |
| timeleft     | Real     | time left         |
| initialstock | Real     | initial stock     |
| stockleft    | Real     | stock left        |
| lastupdated  | Big int  | last updated time |
| entity_id    | Integer  | entity id         |

**Response example:**


    [
        {
            "machineid": 331177,
            "timeleft": 45.0,
            "initialstock": 600.0,
            "stockleft": 600.0,
            "lastupdated": 1613108200000,
            "entity_id": 1
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Update selected machine configuration<a name="Update selected machine configuration"></a>


    Method : PUT
    URL: /machines/config/331177

**Parameters**

| Field             | Datatype | Description           |
| ----------------- | -------- | --------------------- |
| jobid             | Integer  | job id                |
| minthreshold      | Integer  | minimum threshold     |
| maxthreshold      | Integer  | maximum threshold     |
| machine_model     | String   | machine model         |
| min_current_time  | Integer  | minimum current       |
| max_current_time  | Integer  | maximum current       |
| max_current_range | Integer  | maximum xurrent range |
| min_voltage       | Integer  | minimum voltage       |
| max_voltage       | Integer  | maximum voltage       |
| min_wirefeed      | Integer  | minimum wirefeed      |
| max_wirefeed      | Integer  | maximum wirefeed      |
| min_gasflow       | Integer  | minimum gasflow       |
| max_gasflow       | Integer  | maximum gasflow       |
| joncreated        | Big int  | job created time      |

**Parameters example:**


    {
          "jobid":3,
        "minthreshold":350,
        "maxthreshold":500,
        "min_current_time":500,
        "max_current_time":600,
        "current_max_range":450,
        "min_voltage":20,
        "max_voltage":30,
        "min_wirefeed":2,
        "max_wirefeed":5,
        "min_gasflow":23,
        "max_gasflow":34,
        "jobcreated":1612255697000
    }
    
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Update wirefeed<a name="Update wirefeed"></a>


    Method : PUT
    URL: /machines/wirefeed/331177

**Parameters**

| Field        | Datatype | Description         |
| ------------ | -------- | ------------------- |
| initialstock | Integer  | initial stock value |
| lastupdated  | Big int  | last updated time   |

**Parameters example:**


    {
        "initialstock":700,
        "lastupdated":1612273397000
    }
    
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Get report data<a name="Get report data"></a>


    Method : GET
    URL: /machines/getlivereport?machineid=123456&startdate=1612522001000&enddate=1613374247000

**Response:** Success 200 OK

| Field               | Datatype | Description          |
| ------------------- | -------- | -------------------- |
| machine id          | Integer  | unique id            |
| recordtimeinstance  | Bigint   | record timeinstance  |
| weldduration        | Numeric  | weld duration        |
| jobcount            | Numeric  | jobcount             |
| onduration          | Numeric  | onduration           |
| goodweld            | Numeric  | goodweld             |
| utilization         | Numeric  | utilization          |
| totaljob            | Numeric  | total job            |
| goodjob             | Numeric  | good job             |
| badjob              | Numeric  | bad job              |
| overallweldduration | Numeric  | overall weldduration |
| overallonduration   | Numeric  | overall onduration   |

**Response example:**


    [
        {
            "machineid": 123456,
            "recordtimeinstance": 1612523801000,
            "weldduration": "0.00",
            "jobcount": "0.00",
            "onduration": "0.00",
            "goodweld": "0.00",
            "utilization": "0.00",
            "quality": "0",
            "totaljob": "0.00",
            "goodjob": "0.00",
            "badjob": "0.00",
            "overallweldduration": "0",
            "overallonduration": "3"
        },
        {
            "machineid": 123456,
            "recordtimeinstance": 1613372447000,
            "weldduration": "0.00",
            "jobcount": "0.00",
            "onduration": "0.00",
            "goodweld": "0.00",
            "utilization": "0.00",
            "quality": "0",
            "totaljob": "0.00",
            "goodjob": "0.00",
            "badjob": "0.00",
            "overallweldduration": "0",
            "overallonduration": "3"
        },
        {
            "machineid": 123456,
            "recordtimeinstance": 1613376047000,
            "weldduration": "0.00",
            "jobcount": "0.00",
            "onduration": "0.00",
            "goodweld": "0.00",
            "utilization": "0.00",
            "quality": "0",
            "totaljob": "0.00",
            "goodjob": "0.00",
            "badjob": "0.00",
            "overallweldduration": "0",
            "overallonduration": "3"
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }
# Home<a name="Home"></a>
## Total wirefeed left<a name="Total wirefeed left"></a>


    Method : GET
    URL: /home/wirefeed

**Response:** Success 200 OK

| Field         | Datatype | Description    |
| ------------- | -------- | -------------- |
| totalwirefeed | Integer  | total wirefeed |

**Response example:**


    [
        {
            "totalwirefeed": 600.0
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get home overview<a name="Get home overview"></a>


    Method : GET
    URL: /home/

**Response:** Success 200 OK

| Field                  | Datatype         | Description            |
| ---------------------- | ---------------- | ---------------------- |
| weldduration           | double precision | weld duration          |
| powerduration          | double precision | duration of power      |
| idleduration           | double precision | idle duration          |
| availability           | double precision | availability           |
| performance            | double precision | performance            |
| quality                | double precision | quality                |
| total                  | double precision | total                  |
| poweron                | double precision | poweron                |
| weldon                 | double precision | weldon                 |
| idealpower             | double precision | idealpower             |
| weldpower              | double precision | weldpower              |
| manpowerproductivity   | double precision | manpowerproductivity   |
| daily_shift_hour       | double precision | daily shift hours      |
| power_rate_unit        | double precision | unit of power          |
| welder_daily_available | double precision | welder daily available |
| daily_labour_rate      | double precision | daily labour rate      |
| weld_power_consume     | double precision | weld power consume     |
| idle_power_consume     | double precision | idle power consume     |

**Response example:**


    {
        "overview": [
            {
                "result": {
                    "weldduration": 5302,
                    "powerduration": 36991,
                    "idleduration": 31689,
                    "oee": 4.7998238022,
                    "availability": 1,
                    "performance": 74.34,
                    "quality": 77.51,
                    "total": 4,
                    "poweron": 1,
                    "weldon": 1,
                    "idealpower": 9.5,
                    "weldpower": 16.2,
                    "manpowerproductivity": null,
                    "config": {
                        "daily_shift_hrs": 11,
                        "power_market_rate": 11,
                        "welder_daily_available_hrs": 20,
                        "daily_labour_rate": 444,
                        "Weld_power_consume": 12,
                        "idle_power_consume": 11
                    },
                    "status": [
                        {
                            "machineid": 56324,
                            "status": 2
                        }
                    ]
                }
            }
        ],
        "status": [
            {
                "poweron": 1,
                "weldon": 0,
                "total": 1
            }
        ]
    }

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get hourly<a name="Get hourly"></a>


    Method : GET
    URL: /home/hourly

**Response:** Success 200 OK

| **Field**    | **Datatype** | **Description** |
| ------------ | ------------ | --------------- |
| weldduration | Integer      | weld duration   |
| idleduration | Integer      | idle duration   |
| onduration   | Integer      | on duration     |
| ts           | Big int      | ts              |

**Response example:**


    [
        {
            "result": {
                "ts": [
                    1613372446800,
                    1613376046800
                ],
                "idealduration": [
                    1,
                    2
                ],
                "weldduration": [
                    0,
                    0
                ],
                "onduration": [
                    1,
                    2
                ]
            }
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }
# Report<a name="Report"></a>
## Report read<a name="Report read"></a>


    Method : GET
    URL: /reports

**Response:** Success 200 OK

| Field                        | Datatype         | Description                  |
| ---------------------------- | ---------------- | ---------------------------- |
| ts                           | Bigint           | ts                           |
| produced                     | Integer          | produced                     |
| rejected                     | Integer          | rejected                     |
| total_weldduration           | double precision | total weldduration           |
| total_onduration             | double precision | total onduration             |
| total_idle_duration          | double precision | total idle duration          |
| sum_total_loss               | double precision | sum total loss               |
| total_availability           | double precision | total availability           |
| total_oee                    | double precision | total oee                    |
| total_quality                | double precision | total quality                |
| total_performance            | double precision | total performance            |
| total_weld_power_consumed    | double precision | total weld power consumed    |
| total_man_power_productivity | double precision | total man power productivity |
| daily_labour_rate            | double precision | daily labour rate            |
| weld_power_consume           | double precision | weld power consume           |
| idle_power_consume           | double precision | idle power consume           |
| machineid                    | double precision | machineid                    |

**Response example:**


    {
        "jobs": {
            "jobs": [
                {
                    "ts": 1612778164000,
                    "produced": 2400,
                    "rejected": 6,
                    "good": 2394
                }
            ]
        },
        "daywise": {
            "daywise": [
                {
                    "ts": 1612935631000,
                    "weldduration": 833,
                    "onduration": 125198,
                    "idle_duration": 574.46,
                    "man_power_productivity": 0,
                    "loss_productivity": 100,
                    "weld_power_consumed": 550,
                    "power_loss_idle_unit": 1124.46,
                    "power_consumption_work": 0,
                    "power_consumption_idle": 2,
                    "monitory_loss": 100,
                    "loss_man_power_productivity": 0,
                    "total_loss": 50,
                    "availability": 20,
                    "oee": 22,
                    "quality": 0,
                    "performance": 0
                },
                {
                    "ts": 1612938009000,
                    "weldduration": 833,
                    "onduration": 125198,
                    "idle_duration": 574.46,
                    "man_power_productivity": 0,
                    "loss_productivity": 100,
                    "weld_power_consumed": 550,
                    "power_loss_idle_unit": 1124.46,
                    "power_consumption_work": 0,
                    "power_consumption_idle": 2,
                    "monitory_loss": 100,
                    "loss_man_power_productivity": 0,
                    "total_loss": 50,
                    "availability": 20,
                    "oee": 22,
                    "quality": 0,
                    "performance": 0
                }
            ]
        },
        "sum": {
            "sum": {
                "total_weldduration": 1666,
                "total_onduration": 250396,
                "total_idle_duration": 1148.92,
                "sum_total_loss": 100,
                "total_aval": 20,
                "tota_oee": 0,
                "total_quality": 0,
                "total_performance": 0,
                "total_weld_power_consumed": 1100,
                "total_idle_power_consumed": 2248.92
            }
        }
    }

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Daily Report<a name="Daily Report"></a> 


    Method : GET
    URL: /reports/machineid

**Response example:** 200 OK


    {
        "jobs": {
            "jobs": [
                {
                    "machineid": 123456,
                    "ts": 1612778164000,
                    "cycle_time": 30,
                    "produced": 1200,
                    "rejected": 3,
                    "good": 1197
                }
            ]
        },
        "daywise": {
            "daywise": [
                {
                    "machineid": 123456,
                    "ts": 1612862624000,
                    "weldduration": 11703,
                    "onduration": 81178,
                    "idle_duration": 71860,
                    "man_power_productivity": 29.59,
                    "loss_productivity": 70.41,
                    "weld_power_consumed": 48.6,
                    "power_loss_idle_unit": 20.06,
                    "power_consumption_work": 70.78,
                    "power_consumption_idle": 29.22,
                    "monitory_loss": 321.02,
                    "loss_man_power_productivity": 387.28,
                    "total_loss": 708.3,
                    "availability": 25,
                    "oee": 20,
                    "quality": 5,
                    "performance": 50
                }
            ]
        },
        "sum": {
            "sum": {
                "total_weldduration": 11703,
                "total_onduration": 81178,
                "total_idle_duration": 71860,
                "sum_total_loss": 708.3,
                "total_aval": 25,
                "tota_oee": 0.625,
                "total_quality": 5,
                "total_performance": 50,
                "total_weld_power_consumed": 48.6,
                "total_idle_power_consumed": 20.06,
                "total_man_power_productivity": 29.59
            }
        }
    }

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get Power Report<a name="Get Power Report"></a>
    Method : GET
    URL: /reports/poweranalysis?startdate=1613374247000&enddate=1613374247000&machineid=10102

**Response:** Success 200 OK

| Field              | Datatype | Description          |
| ------------------ | -------- | -------------------- |
| machineid          | Integer  | machineid            |
| recordtimeinstance | Bigint   | record timeinstance  |
| weldduration       | numeric  | weld duration        |
| onduration         | numeric  | on duration          |
| idealpowerconsumed | numeric  | ideal power consumed |
| weldpowerconsumed  | numeric  | weld power consumed  |

**Response example:**


    {
        "daywise": [
            {
                "machineid": 10102,
                "recordtimeinstance": 1613376043200.0,
                "weldduration": "0.00",
                "onduration": "0.00",
                "idealpowerconsumed": "0.00",
                "weldpowerconsumed": "0.00"
            }
        ]
    }

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }
# Predictions<a name="Predictions"></a>
## Get warranty predictions<a name="Get warranty predictions"></a>


    Method : GET
    URL: /predictions/warranty

**Response:** Success 200 OK

| Field           | Datatype         | Description       |
| --------------- | ---------------- | ----------------- |
| machineid       | Integer          | unique machine id |
| cause           | String           | type of cause     |
| expires         | double precision | expires           |
| category        | String           | warranty category |
| entity_id       | Integer          | entity id         |
| machine_tagname | String           | machine tag name  |

**Response example:**


    [
        {
            "machineid": 56324,
            "cause": "usage",
            "expires": 142.0,
            "category": "Under Warranty",
            "entity_id": 1,
            "machine_tagname": "L1M2"
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get wirefeed predictions<a name="Get wirefeed predictions"></a>


    Method : GET
    URL: /predictions/wirefeed

**Response:** Success 200 OK

| Field           | Datatype | Description             |
| --------------- | -------- | ----------------------- |
| machineid       | Integer  | unique machine id       |
| timeleft        | Real     | time left               |
| initialstock    | Real     | number of initial stock |
| stockleft       | Real     | number of stock left    |
| lastupdated     | Big int  | last updated date       |
| entity_id       | Integer  | entity id               |
| machine_tagname | String   | machine tag name        |

**Response example:**


    [
        {
            "machineid": 331177,
            "timeleft": 45.0,
            "initialstock": 600.0,
            "stockleft": 600.0,
            "lastupdated": 1613108200000,
            "entity_id": 1,
            "machine_tagname": "L4M4"
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get all faults<a name="Get all faults"></a>


    Method : GET
    URL: /predictions/fault

**Response:** Success 200 OK

| **Field**     | **Datatype** | **Description**   |
| ------------- | ------------ | ----------------- |
| machineid     | Integer      | unique machine id |
| error_details | String       | type of error     |
| instances     | Integer      | instances         |
| entity_id     | Integer      | entity id         |
| maxerror      | Integer      | maximum error     |

**Response example:**


    [
        {
            "machineid": 56324,
            "error_details": "Water Pressure",
            "instances": 6,
            "entity_id": 1,
            "maxerror": 6
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


## Get fault by date<a name="Get fault by date"></a>


    Method : GET
    URL: /predictions/fault/331177

**Response:** Success 200 OK

| **Field**       | **Datatype** | **Description**   |
| --------------- | ------------ | ----------------- |
| machineid       | Integer      | unique machine id |
| error_details   | String       | type of error     |
| instances       | Integer      | instances         |
| entity_id       | Integer      | entity_id         |
| datetime        | Bigint       | datetime          |
| machine_tagname | String       | machine tag name  |

**Response example:**


    [
        {
            "machineid": 331177,
            "error_details": "Water Pressure",
            "instances": 2,
            "entity_id": 1,
            "datetime": 1612355477000,
            "machine_tagname": "L4M4"
        }
    ]
    

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


# Nodes<a name="Nodes"></a>
## Add new node<a name="Add new node"></a>
    Method : POST
    URL: /nodes

**Parameters**

| Field          | Datatype | Description     |
| -------------- | -------- | --------------- |
| nodeaddr       | String   | node address    |
| gateway_mac_id | String   | gate way mac id |
| commission     | Integer  | commission      |

**Parameters Example:**


    {
        "nodeaddr":"0x124b001be46202",
        "gateway_mac_id":"04:a3:16:b0:ec:10", 
        "commission":1
    }
    
    

**Response:** Success 200 OK
 

    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## Get all nodes<a name="Get all nodes"></a>
    Method : GET
    URL: /nodes/u101

**Response:** Success 200 OK

| **Field**  | **Datatype** | **Description** |
| ---------- | ------------ | --------------- |
| nodeid     | String       | node id         |
| commission | Integer      | commission      |

**Response example:**


    [
        {
            "nodeid": "0x124b001be46200",
            "commission": 1
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"


## Get selected node<a name="Get selected node"></a>


    Method : GET
    URL: /nodes/0x124b001be46202

**Response:** Success 200 OK

| **Field**      | **Datatype** | **Description** |
| -------------- | ------------ | --------------- |
| nodeaddr       | String       | node address    |
| gateway_mac_id | String       | gateway mac id  |
| commission     | Integer      | commission      |
| entity_id      | Integer      | entity id       |

**Response example:**


    [
        {
            "nodeaddr": "0x124b001be46202",
            "gateway_mac_id": "04:a3:16:b0:ec:10",
            "commission": 1,
            "entity_id": 1
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"


## Update node by id<a name="Update node by id"></a>


    Method : PUT
    URL: /nodes/0x124b001be46202

**Parameters**

| Field          | Datatype | Description     |
| -------------- | -------- | --------------- |
| gateway_mac_id | String   | gate way mac id |
| commission     | Integer  | commission      |

**Parameters example:**


    {
        "gateway_mac_id":"04:a3:16:b0:ec:30", 
        "commission":1
    }
    
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Delete node<a name="Delete node"></a>


    Method: DELETE
    URL: /nodes/0x124b001be46200

**URL parameters:**

| **Field** | **Datatype** | **Description**     |
| --------- | ------------ | ------------------- |
| nodeaddr  | String       | nodeaddr for delete |

**Parameter Example:**


    /nodes/0x124b001be46200

**Response:** Success 200 OK


    Success 200 OK
    {
        "message": "Deleted Successfully"
    }

**Error:**

| Field        | Description                    | Status        |
| ------------ | ------------------------------ | ------------- |
| Permission   | If tokens get permission error | 403 Forbidden |
| Unauthorized | User not have read permission  | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"
    }


    403 Forbidden
    {
      "message":"unauthorized"
    }


# Tickets<a name="Tickets"></a>
## Add ticket<a name="Add ticket"></a>


    Method : POST
    URL: /tickets/

**Parameters**

| Field         | Datatype | Description   |
| ------------- | -------- | ------------- |
| machineid     | Integer  | machine id    |
| cause         | String   | type of cause |
| remark        | String   | remark        |
| severity      | Integer  | severity      |
| ticket_status | String   | ticket status |
| closed_date   | Bigint   | closed date   |
| reported_date | Bigint   | reported date |

**Parameters Example:**


    {
        "machineid":123456,
        "cause":"Motor",
        "remark":"Vibration",
        "severity": 1,
        "ticket_status":"In Progress",
        "closed_date":1612419870000,
        "reported_date":1612419870000
    }
    
    
    

**Response:** Success 200 OK
 

    {
        "message": "Inserted Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |

**Error example:**


    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }


## Update ticket details<a name="Update ticket details"></a>


    Method : PUT
    URL: /tickets/3

**Parameters**

| Field         | Datatype | Description   |
| ------------- | -------- | ------------- |
| machineid     | Integer  | machine id    |
| cause         | String   | type of cause |
| remark        | String   | remark        |
| severity      | Integer  | severity      |
| ticket_status | String   | ticket status |
| closed_date   | Bigint   | closed date   |
| reported_date | Bigint   | reported date |

**Parameters example:**


    {
        "machineid":123456,
        "cause":"Motor",
        "remark":"still heating",
        "severity": 2,
        "ticket_status":"In Progress",
        "closed_date":1612419870000,
        "reported_date":1612419870000
    }
    

**Response:** Success 200 OK


    {
        "message": "Updated Successfully"
    }

**Error:**

| **Field**    | **Description**        | **Status**    |
| ------------ | ---------------------- | ------------- |
| Unauthorized | User is not authorized | 403 Forbidden |
| Pemission    | If token expires       | 403 Forbidden |

**Error example:**
Unauthorized

    HTTP/1.1 403 Forbidden
    {
      "message":"unauthorized"
    }

Permission

    HTTP/1.1 403 Forbidden
    {
        "message": "'permission'"
    }


## Get selected ticket<a name="Get selected ticket"></a>


    Method : GET
    URL: /tickets/?startdate=1612419870000&enddate=1612419870000&machineid=123456&severity=2

**Response:** Success 200 OK

| **Field**     | **Datatype** | **Description** |
| ------------- | ------------ | --------------- |
| severity      | Integer      | severity        |
| open          | Integer      | open            |
| resolved      | Integer      | resolved        |
| inprogress    | Integer      | inprogress      |
| total         | Integer      | total           |
| machineid     | Integer      | machineid       |
| ticketid      | Integer      | ticketid        |
| cause         | String       | cause           |
| closed_date   | Integer      | closed_date     |
| remark        | String       | remark          |
| reported_date | Integer      | reported_date   |
| ticket_status | String       | ticket_status   |
| userid        | String       | userid          |

**Response example:**


    {
        "status": [
            {
                "severity": 1,
                "open": 0,
                "resolved": 0,
                "inprogress": 1,
                "total": 1
            }
        ],
        "severity": [
            {
                "machineid": 123456,
                "ticketid": 3,
                "cause": "Motor",
                "closed_date": 1612419870000,
                "remark": "still heating",
                "reported_date": 1612419870000,
                "severity": 2,
                "ticket_status": "In Progress",
                "userid": "admin"
            }
        ]
    }

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"


## Get all tickets<a name="Get all tickets"></a>


    Method : GET
    URL: /tickets/getticket?startdate=1612419870000&enddate=1612419870000

**Response:** Success 200 OK

| **Field**  | **Datatype** |
| ---------- | ------------ |
| low        | Integer      |
| medium     | Integer      |
| high       | Integer      |
| critical   | Integer      |
| motor      | Integer      |
| wirefeed   | Integer      |
| voltage    | Integer      |
| current    | Integer      |
| others     | Integer      |
| open       | Integer      |
| resolved   | Integer      |
| inprogress | Integer      |
| total      | Integer      |

**Response example:**


    [
        {
            "low": 2,
            "medium": 1,
            "high": 0,
            "critical": 0,
            "motor": 3,
            "wirefeed": 0,
            "voltage": 0,
            "current": 0,
            "overheat": 0,
            "others": 0,
            "open": 0,
            "resolved": 0,
            "inprogress": 3,
            "total": 3
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"


## Get all live tickets<a name="Get all live tickets"></a>


    Method : GET
    URL: /tickets/getliveticket

**Response:** Success 200 OK

| **Field**  | **Datatype** | **Description** |
| ---------- | ------------ | --------------- |
| low        | Integer      | low             |
| medium     | Integer      | medium          |
| high       | Integer      | high            |
| critical   | Integer      | critical        |
| motor      | Integer      | motor           |
| wirefeed   | Integer      | wirefeed        |
| voltage    | Integer      | voltage         |
| current    | Integer      | current         |
| overheat   | Integer      | overheat        |
| others     | Integer      | others          |
| open       | Integer      | open            |
| resolved   | Integer      | resolved        |
| inprogress | Integer      | inprogress      |
| total      | Integer      | total           |

**Response example:**


    [
        {
            "low": 2,
            "medium": 1,
            "high": 0,
            "critical": 0,
            "motor": 3,
            "wirefeed": 0,
            "voltage": 0,
            "current": 0,
            "overheat": 0,
            "others": 0,
            "open": 0,
            "resolved": 0,
            "inprogress": 3,
            "total": 3
        }
    ]

**Error:**

| **Field**  | **Description**        | **Status**    |
| ---------- | ---------------------- | ------------- |
| Permission | User is not authorized | 403 Forbidden |

**Error example:**


    403 Forbidden
    {
        "message": "'permission'"

