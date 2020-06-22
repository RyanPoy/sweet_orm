ORM
===

Introduction
------------
The ORM provides a simple ActiveRecord implementation for operate database.

Basic usage
-----------

1. Create you table

.. code-block:: SQL

  -- create table

  create table users (
    id int auto_increment primary key ,
    name varchar(32) not null default '',
    age int not null default 20
  );

2. Define the model for table

.. code-block:: python

  class User(Model):
    pass

3. Basic operate 

.. code-block:: python

  User.create(name='jim', age=24)
  User.find(1)
  User.all()
  User.first()
  User.last()
  # ...


Create
------

Create a single model
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  User.create(name='jim', age=25)

Create multiple models
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
  
  User.create_all(
    dict(name='jim', age=25),
    dict(name='jon', age=35),
    dict(name='lily', age=20),
  )

Update
------

Update a single model
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  u = User.find(1)                  # find the user which id = 1
  u.update(name="lily", age=20)     # update user


Update multiple models
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  # update all users set name = 'lily' and age = 20
  User.update_all(name='lily', age=20) 


Save
----

If the model has been persisted, 
calling the ``save`` method is equivalent to calling the ``update`` method. 
Otherwise it is equivalent to calling the create method.

.. code-block:: python

  u = User(name='jim', age=25)
  u.save() # will be create a model

  u = User.find(1)
  u.name = 'jon'
  u.age = 30
  u.save() # will be update the model


Delete
------

Delete a single model
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  u = User.find(1) # find the user which id = 1
  u.delete()       # delete the user

  User.where(name=10).delete() # delete the user which name = 10

Delete multiple models
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  User.delete_all()         # delete all users
  User.delete_all(age=20)   # delete all users which age = 20

Retrieving Modles
-----------------

.. code-block:: python

  User.first()
  User.last()
  User.all()
  User.where(name='jon').first()
  User.where(age__lt=30).all()


Aggregates
----------

.. code-block:: python

  User.count()
  User.max('age')
  User.min('age')
  User.avg('age')
  User.sum('age')

Transaction
-----------

Atomic
^^^^^^

.. code-block:: python

  from sweet_orm.orm import atomic

  @atomic
  def delete():
    User.first().delete()

Manual
^^^^^^

.. code-block:: python

  from sweet_orm.orm import atomic

  with User.transaction() as t:
    User.first().delete()
    t.commit()

  with User.transaction() as t:
    User.delete_all()
    t.rollback()

