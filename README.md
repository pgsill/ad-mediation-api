# **Ad Mediation API - Proof of Concept**

## About

This API receives applications and networks and a score value that is the relation between them, this score is used to mediate and return an ordered list of one applcation networks ordered by the score.

## How to run this project

Inside the folder deploy you have a sample environment file, modify it to your preferences or keep the defaults.

Inside the `docker-compose.yml` file you have the environment variables and ports configurations, modify it to your preferences or keep the defauls

**Note that the application will run on `http://localhost:5000` by default** 

You need to have `docker` and `docker-compose` installed.

After that while inside the folder where the **`docker-compose.yml`** file is, run :

 ```
 docker-compose up --build -d 
 ```
 
 and in a couple of seconds the application will be up and running.

You can also run without the **`-d`** argument to see the logs :
```
docker-compose up --build
```
 

To test it go to **`http://localhost:5000`**

To stop it run the command 

```
docker-compose down
```

If the application was started with the **`-d`** command or press **Ctrl+C** if not. then
```
docker-compose down
```


**Note that you have to be inside the folder where the `docker-compose.yml` file is**

**The default config file adds some sample data. If you do not want that just set `POPULATE_SAMPLE`** to **`False`** inside the default env file inside the deploy folder.

# **The main endpoints**

### **GET**

### **`/api/app/<app_id>/mediate`**

### **Returns a mediated list ordered by score**

```json
[
  {
    "id": "c507127e-6254-47ac-80ce-779b05b679f8",
    "name": "Ad Network 02",
    "code": "ADN02",
    "endpoint": "http://adn02.com/ads",
    "score": 7.1
  },
  {
    "id": "56d21d8c-0fed-4be3-882f-13db20c15149",
    "name": "Ad Network 03",
    "code": "ADN03",
    "endpoint": "http://adn03.com/ads",
    "score": 6.4
  },
  {
    "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
    "name": "Ad Network 01",
    "code": "ADN01",
    "endpoint": "http://adn01.com/ads",
    "score": 2.6
  }
]
```

### **PUT**

### `/api/app/<app_id>/networks`

### **Updates the scores of the supplies list of networks from the application with the supplied ID**

```json
{
    "ad_networks": [
        {
            "id": "c507127e-6254-47ac-80ce-779b05b679f8",
            "score": 3.5
        },
               {
            "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
            "score": 1.7
        }
    ]
}
```



# Endpoints

## Application Endpoint
+ **GET**


**`/api/app`**

Returns all the applications

```json
[
  {
    "id": "7ff0c93a-71c3-4553-8893-52160a4ae91b",
    "name": "Application 02",
    "code": "APP02",
    "adNetworks": [
      {
        "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
        "name": "Ad Network 01",
        "code": "ADN01",
        "endpoint": "http://adn01.com/ads",
        "score": 0
      }
    ]
  },
  {
    "id": "855f8ef3-85f8-4bee-aff8-ae8a9bc24100",
    "name": "Application 01",
    "code": "APP01",
    "adNetworks": [
      {
        "id": "c507127e-6254-47ac-80ce-779b05b679f8",
        "name": "Ad Network 02",
        "code": "ADN02",
        "endpoint": "http://adn02.com/ads",
        "score": 7.1
      },
      {
        "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
        "name": "Ad Network 01",
        "code": "ADN01",
        "endpoint": "http://adn01.com/ads",
        "score": 2.6
      },
      {
        "id": "56d21d8c-0fed-4be3-882f-13db20c15149",
        "name": "Ad Network 03",
        "code": "ADN03",
        "endpoint": "http://adn03.com/ads",
        "score": 6.4
      }
    ]
  }
]
```

**`/api/app/<app_id>`**

Returns one single application

```json
{
    "id": "855f8ef3-85f8-4bee-aff8-ae8a9bc24100",
    "name": "Application 01",
    "code": "APP01",
    "adNetworks": [
      {
        "id": "c507127e-6254-47ac-80ce-779b05b679f8",
        "name": "Ad Network 02",
        "code": "ADN02",
        "endpoint": "http://adn02.com/ads",
        "score": 7.1
      },
      {
        "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
        "name": "Ad Network 01",
        "code": "ADN01",
        "endpoint": "http://adn01.com/ads",
        "score": 2.6
      },
      {
        "id": "56d21d8c-0fed-4be3-882f-13db20c15149",
        "name": "Ad Network 03",
        "code": "ADN03",
        "endpoint": "http://adn03.com/ads",
        "score": 6.4
      }
    ]
  }
```

**`/api/app/<app_id>/mediate`**

Returns an ordered list by score.


```json
[
  {
    "id": "c507127e-6254-47ac-80ce-779b05b679f8",
    "name": "Ad Network 02",
    "code": "ADN02",
    "endpoint": "http://adn02.com/ads",
    "score": 7.1
  },
  {
    "id": "56d21d8c-0fed-4be3-882f-13db20c15149",
    "name": "Ad Network 03",
    "code": "ADN03",
    "endpoint": "http://adn03.com/ads",
    "score": 6.4
  },
  {
    "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
    "name": "Ad Network 01",
    "code": "ADN01",
    "endpoint": "http://adn01.com/ads",
    "score": 2.6
  }
]
```


+ **POST**

`/api/app`

Adds one application

```json
{
  "name": "Application 01",
  "code": "AP01"
}
```

`/api/app/<app_id>/networks`

```json
{
    "ad_networks" : ["e80ff03a-254d-4a26-b126-cca2a2edbea0", "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e"]
}
```

+ **PUT**

`/api/app/<app_id>`

Updates the information of the application with the supplied ID

```json
{
  "name": "Application 01",
  "code": "AP01"
}
```

`/api/app/<app_id>/networks`

Updates the scores of the supplies list of networks from the application with the supplied ID

```json
{
    "ad_networks": [
        {
            "id": "c507127e-6254-47ac-80ce-779b05b679f8",
            "score": 3.5
        }
    ]
}
```

+ **DELETE**

`/api/app/<app_id>`

```json
{}
```

`/api/app/<app_id>/networks`

```json
{
    "ad_networks" : ["e80ff03a-254d-4a26-b126-cca2a2edbea0", "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e"]
}
```

## Network Endpoint
+ **GET**

`/api/network`

```json
[
  {
    "id": "c507127e-6254-47ac-80ce-779b05b679f8",
    "name": "Ad Network 02",
    "code": "ADN02",
    "endpoint": "http://adn02.com/ads"
  },
  {
    "id": "b25e0be2-5d5a-4f33-82c9-ba72404ddf3e",
    "name": "Ad Network 01",
    "code": "ADN01",
    "endpoint": "http://adn01.com/ads"
  },
  {
    "id": "56d21d8c-0fed-4be3-882f-13db20c15149",
    "name": "Ad Network 03",
    "code": "ADN03",
    "endpoint": "http://adn03.com/ads"
  }
]
```

`/api/network/<network_id>`

```json
{
  "id": "c507127e-6254-47ac-80ce-779b05b679f8",
  "name": "Ad Network",
  "code": "ADN02",
  "endpoint": "http://adn02.com/ads"
}
```

+ **POST**

`/api/network`

```json
{
  "name": "Ad Network",
  "code": "ADN02",
  "endpoint": "http://adn02.com/ads"
}
```

+ **PUT**

`/api/network/<network_id>`

```json
{
  "name": "Ad Network",
  "code": "ADN02",
  "endpoint": "http://adn02.com/ads"
}
```

+ **DELETE**

`/api/network`

```json
{
  "name": "Ad Network",
  "code": "ADN02",
  "endpoint": "http://adn02.com/ads"
}
```
