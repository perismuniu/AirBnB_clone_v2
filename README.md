<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

TASKS

0. Fork me if you can!

In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

	“Who did this code?”
	“How it works?”
	“Where are unittests?”
	“Where is this?”
	“Why did they do that like this?”
	“I don’t understand anything.”
	“… I will refactor everything…”

But the worst thing you could possibly do is to redo everything. Please don’t do that! Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!

For this project you will fork this codebase:

	update the repository name to AirBnB_clone_v2
	update the README.md with your information but don’t delete the initial authors

If you are the owner of this repository, please create a new repository named AirBnB_clone_v2 with the same content of AirBnB_clone

1. Bug free!

Do you remember the unittest module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.

guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 
All your unittests must pass without any errors at anytime in this project, with each storage engine!. Same for PEP8!

guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$

Some tests won’t be relevant for some type of storage, please skip them by using the skipIf feature of the Unittest module - 26.3.6. Skipping tests and expected failures. Of course, the number of tests must be higher than the current number of tests, so if you decide to skip a test, you should write a new test!

How to test with MySQL?
First, you create a specific database for it (next tasks). After, you have to remember what the purpose of an unittest?

“Assert a current state (objects/data/database), do an action, and validate this action changed (or not) the state of your objects/data/database”

For example, “you want to validate that the create State name="California" command in the console will add a new record in your table states in your database”, here steps for your unittest:

get the number of current records in the table states (my using a MySQLdb for example - but not SQLAlchemy (remember, you want to test if it works, so it’s better to isolate from the system))
execute the console command
get (again) the number of current records in the table states (same method, with MySQLdb)
if the difference is +1 => test passed

2. Console improvements

Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:

	Command syntax: create <Class name> <param 1> <param 2> <param 3>...
	Param syntax: <key name>=<value>
	Value syntax:
		String: "<value>" => starts with a double quote
			any double quote inside the value must be escaped with a backslash \
			all underscores _ must be replace by spaces . Example: You want to set the string My little house to the attribute name, your command line must be name="My_little_house"
		Float: <unit>.<decimal> => contains a dot .
		Integer: <number> => default case
	If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped

Don’t forget to add tests for this new feature!

Also, this new feature will be tested here only with FileStorage engine.

3. MySQL setup development

Write a script that prepares a MySQL server for the project:

	A database hbnb_dev_db
	A new user hbnb_dev (in localhost)
	The password of hbnb_dev should be set to hbnb_dev_pwd
	hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
	hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
	If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

4. MySQL setup test

Write a script that prepares a MySQL server for the project:

	A database hbnb_test_db
	A new user hbnb_test (in localhost)
	The password of hbnb_test should be set to hbnb_test_pwd
	hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
	hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
	If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail

5. Delete object

Update FileStorage: (models/engine/file_storage.py)

	Add a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside - if obj is equal to None, the method should not do anything
	Update the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. Example below with State - it’s an optional filtering

6. DBStorage - States and Cities

SQLAlchemy will be your best friend!

It’s time to change your storage engine and use SQLAlchemy


In the following steps, you will make multiple changes:

	the biggest one is the transition between FileStorage and DBStorage: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the abstraction: Make your code running without knowing how it’s stored.
	add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)

Please follow all these steps:

Update BaseModel: (models/base_model.py)

	Create Base = declarative_base() before the class definition of BaseModel
	Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.
	Add or replace in the class BaseModel:
		class attribute id
			represents a column containing a unique string (60 characters)
			can’t be null
			primary key
		class attribute created_at
			represents a column containing a datetime
			can’t be null
			default value is the current datetime (use datetime.utcnow())
		class attribute updated_at
			represents a column containing a datetime
			can’t be null
			default value is the current datetime (use datetime.utcnow())
	Move the models.storage.new(self) from def __init__(self, *args, **kwargs): to def save(self): and call it just before models.storage.save()
	In def __init__(self, *args, **kwargs):, manage kwargs to create instance attribute from this dictionary. Ex: kwargs={ 'name': "California" } => self.name = "California" if it’s not already the case
	Update the to_dict() method of the class BaseModel:
		remove the key _sa_instance_state from the dictionary returned by this method only if this key exists
	Add a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete

Update City: (models/city.py)

	City inherits from BaseModel and Base (respect the order)
	Add or replace in the class City:
		class attribute __tablename__ -
			represents the table name, cities
		class attribute name
			represents a column containing a string (128 characters)
			can’t be null
		class attribute state_id
			represents a column containing a string (60 characters)
			can’t be null
			is a foreign key to states.id

Update State: (models/state.py)

	State inherits from BaseModel and Base (respect the order)
	Add or replace in the class State:
		class attribute __tablename__
			represents the table name, states
		class attribute name
			represents a column containing a string (128 characters)
			can’t be null
		for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
		for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City

New engine DBStorage: (models/engine/db_storage.py)

	Private class attributes:
		__engine: set to None
		__session: set to None
	Public instance methods:
		__init__(self):
			create the engine (self.__engine)
			the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
				dialect: mysql
				driver: mysqldb
			all of the following values must be retrieved via environment variables:
				MySQL user: HBNB_MYSQL_USER
				MySQL password: HBNB_MYSQL_PWD
				MySQL host: HBNB_MYSQL_HOST (here = localhost)
				MySQL database: HBNB_MYSQL_DB
			don’t forget the option pool_pre_ping=True when you call create_engine
			drop all tables if the environment variable HBNB_ENV is equal to test
		all(self, cls=None):
			query on the current database session (self.__session) all objects depending of the class name (argument cls)
			if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
			this method must return a dictionary: (like FileStorage)
				key = <class-name>.<object-id>
				value = object
		new(self, obj): add the object to the current database session (self.__session)
		save(self): commit all changes of the current database session (self.__session)
		delete(self, obj=None): delete from the current database session obj if not None
		reload(self):
			create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
			create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe

Update __init__.py: (models/__init__.py)

	Add a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
		If equal to db:
			Import DBStorage class in this file
			Create an instance of DBStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
		Else:
			Import FileStorage class in this file
			Create an instance of FileStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)

	This “switch” will allow you to change storage type directly by using an environment variable (example below)

State creation:

guillaume@ubuntu:~/AirBnB_v2$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
guillaume@ubuntu:~/AirBnB_v2$ 

City creation:

guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 

guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
guillaume@ubuntu:~/AirBnB_v2$ 

7. DBStorage - User

Update User: (models/user.py)

	User inherits from BaseModel and Base (respect the order)
	Add or replace in the class User:
		class attribute __tablename__
			represents the table name, users
		class attribute email
			represents a column containing a string (128 characters)
			can’t be null
		class attribute password
			represents a column containing a string (128 characters)
			can’t be null
		class attribute first_name
			represents a column containing a string (128 characters)
			can be null
		class attribute last_name
			represents a column containing a string (128 characters)
			can be null

8. DBStorage - Place

Update Place: (models/place.py)

	Place inherits from BaseModel and Base (respect the order)
	Add or replace in the class Place:
		class attribute __tablename__
			represents the table name, places
		class attribute city_id
			represents a column containing a string (60 characters)
			can’t be null
			is a foreign key to cities.id
		class attribute user_id
			represents a column containing a string (60 characters)
			can’t be null
			is a foreign key to users.id
		class attribute name
			represents a column containing a string (128 characters)
			can’t be null
		class attribute description
			represents a column containing a string (1024 characters)
			can be null
		class attribute number_rooms
			represents a column containing an integer
			can’t be null
			default value: 0
		class attribute number_bathrooms
			represents a column containing an integer
			can’t be null
			default value: 0
		class attribute max_guest
			represents a column containing an integer
			can’t be null
			default value: 0
		class attribute price_by_night
			represents a column containing an integer
			can’t be null
			default value: 0
		class attribute latitude
			represents a column containing a float
			can be null
		class attribute longitude
			represents a column containing a float
			can be null

Update User: (models/user.py)

	Add or replace in the class User:
		class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user

Update City: (models/city.py)

	Add or replace in the class City:
		class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities

9. DBStorage - Review

Update Review: (models/review.py)

	Review inherits from BaseModel and Base (respect the order)
	Add or replace in the class Review:
		class attribute __tablename__
			represents the table name, reviews
		class attribute text
			represents a column containing a string (1024 characters)
			can’t be null
		class attribute place_id
			represents a column containing a string (60 characters)
			can’t be null
			is a foreign key to places.id
		class attribute user_id
			represents a column containing a string (60 characters)
			can’t be null
		is a foreign key to users.id

Update User: (models/user.py)

	Add or replace in the class User:
		class attribute reviews must represent a relationship with the class Review. If the User object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his User should be named user

Update Place: (models/place.py)

	for DBStorage: class attribute reviews must represent a relationship with the class Review. If the Place object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his Place should be named place
	for FileStorage: getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review

10. DBStorage - Amenity... and BOOM!

Update Amenity: (models/amenity.py)

	Amenity inherits from BaseModel and Base (respect the order)
	Add or replace in the class Amenity:
		class attribute __tablename__
			represents the table name, amenities
		class attribute name
			represents a column containing a string (128 characters)
			can’t be null
		class attribute place_amenities must represent a relationship Many-To-Many between the class Place and Amenity. Please see below more detail: place_amenity in the Place update

Update Place: (models/place.py)

	Add an instance of SQLAlchemy Table called place_amenity for creating the relationship Many-To-Many between Place and Amenity:
		table name place_amenity
		metadata = Base.metadata
		2 columns:
			place_id, a string of 60 characters foreign key of places.id, primary key in the table and never null
			amenity_id, a string of 60 characters foreign key of amenities.id, primary key in the table and never null
	Update Place class:
		for DBStorage: class attribute amenities must represent a relationship with the class Amenity but also as secondary to place_amenity with option viewonly=False (place_amenity has been define previously)
		for FileStorage:
			Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
			Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.

What’s a Many-to-Many relationship?

In our system, we don’t want to duplicate amenities (for example, having 10000 time the amenity Wifi), so they will be unique. But, at least 2 places can have the same amenity (like Wifi for example). We are in the case of:

	an amenity can be linked to multiple places
	a place can have multiple amenities

= Many-To-Many

To make this link working, we will create a third table called place_amenity that will create these links.

And you are good, you have a new engine!

0x03. AirBnB clone - Deploy static

TASKS

0. Prepare your web servers
mandatory
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

        Install Nginx if it not already installed
        Create the folder /data/ if it doesn’t already exist
        Create the folder /data/web_static/ if it doesn’t already exist
        Create the folder /data/web_static/releases/ if it doesn’t already exist
        Create the folder /data/web_static/shared/ if it doesn’t already exist
        Create the folder /data/web_static/releases/test/ if it doesn’t already exist
        Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
        Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
        Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
        Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
                Use alias inside your Nginx configuration
                Tip

Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

In optional, you will redo this task but by using Puppet

1. Compress before sending
mandatory
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

        Prototype: def do_pack():
        All files in the folder web_static must be added to the final archive
        All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
        The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
        The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None

2. Deploy archive!
mandatory
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:

        Prototype: def do_deploy(archive_path):
        Returns False if the file at the path archive_path doesn’t exist
        The script should take the following steps:
                Upload the archive to the /tmp/ directory of the web server
                Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
                Delete the archive from the web server
                Delete the symbolic link /data/web_static/current from the web server
                Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
        All remote commands must be executed on your both web servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
        Returns True if all operations have been done correctly, otherwise returns False
        You must use this script to deploy it on your servers: xx-web-01 and xx-web-02

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =...)

Disclaimer: commands execute by Fabric displayed below are linked to the way we implemented the archive function do_pack - like the mv command - depending of your implementation of it, you may don’t need it.

3. Full deployment
mandatory
Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:

        Prototype: def deploy():
        The script should take the following steps:
                Call the do_pack() function and store the path of the created archive
                Return False if no archive has been created
                Call the do_deploy(archive_path) function, using the new path of the new archive
                Return the return value of do_deploy
        All remote commands must be executed on both of web your servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
        You must use this script to deploy it on your servers: xx-web-01 and xx-web-02

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

4. Keep it clean!
#advanced
Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean:

        Prototype: def do_clean(number=0):
        number is the number of the archives, including the most recent, to keep.
                If number is 0 or 1, keep only the most recent version of your archive.
                if number is 2, keep the most recent, and second most recent versions of your archive.
etc.
        Your script should:
                Delete all unnecessary archives (all archives minus the number to keep) in the versions folder
                        Delete all unnecessary archives (all archives minus the number to keep) in the /data/web_static/releases folder of both of your web servers
        All remote commands must be executed on both of your web servers (using the env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

5. Puppet for setup
#advanced
Redo the task #0 but by using Puppet:

ubuntu@89-web-01:~/$ puppet apply 101-setup_web_static.pp
....
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 root root   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 root root 4096 Mar 7 22:29 releases
drwxr-xr-x 2 root root 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ 
