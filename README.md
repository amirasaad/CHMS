<p align="center">
  <a href="" rel="noopener">
</p>

<h3 align="center">Car Rental</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-CC-by-ND)](/LICENSE)

</div>

---

<p align="center">
	Car Hire Management System
    <br>
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](/TODO.md)

## 🧐 About <a name = "about"></a>

Manage booking system for car hiring process.

The following diagram describes the database entities relationship:
![ERD Diagram](/car_rental_erd.drawio.png)
And SQL statements to implement this diagram can be found at [db_init](/docker/mysql/docker-entrypoint-initdb.d/db_init.sql) script.


## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

[docker](https://www.docker.com)


### Installing

To get a development env running. you will need to run the following commands:


```shell
docker compose build
docker compose up -d
```


## 🔧 Running the tests <a name = "tests"></a>

To run the test suite, run the following commands:

```shell
cd customers_service
# For Unit tests
make test-unit
# For Integration tests
make test-integration
# For e2e tests
make test-e2e
```

Before running e2e make sure the server is up.

## ⛏️ Built Using <a name = "built_using"></a>

- [MySQL] - Database
- [FLask] - Server Framework
- [Python] - Server Environment
