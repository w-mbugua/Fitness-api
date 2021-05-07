## Fitness API
An API built to help individuals, fitness instructors or gyms, to easily create and manage workout details.

## Technologies
* Python3
* Flask

## Behaviour
The API is built on three models: user, exercises and workout routines
#### 1. User Authentication
| Task | View| Response |
| :---         |     :---:      |          ---: |
| Registration - `POST`   | `/users/register`    | message    |
| Login - `POST`     | `/users/login`    | message     |
| Users - `GET`   | `/users`      |  *sample response    |
| User - `GET`   | `/users/<int:id>`      |  *sample response    |
| User - `DELETE`   | `/users/<int:id>`      |  message   |

```buildoutcfg

```
#### 2. Workout Exercises
| Task | View| Response |
| :---         |     :---:      |          ---: |
| Create exercise - `POST`   | `/exercises`    | message    |
|All exercise entries - `GET`     | `/exercises`    | *sample response     |
| A single exercise - `GET`   | `/exercises/<int:id>`      |  *sample response    |
| Delete - `DELETE`   | `/exercises/<int:id>`      |  message    |
```buildoutcfg

```
#### 3. Workout Routines
| Task | View| Response |
| :---         |     :---:      |          ---: |
| Create routine - `POST`   | `/workout-routines`    | message    |
|All routines - `GET`     | `/workout-routines`    | *sample response     |
| A single routine - `GET`   | `/workout-routines/<int:id>`      |  *sample response    |
| Update - `PUT`   | `/workout-routines/<int:id>`      |  message    |
| Delete - `DELETE`   | `/workout-routines/<int:id>`      |  message    |

## Authors
1. Alvin Awuor
2. Alex Wanyoike
3. Louise Manyara
4. Shamso Abdi
5. Joy Mbugua

## License
MIT License - 2021
