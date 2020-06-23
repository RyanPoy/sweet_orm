Recordset
=========

Introduction
------------
the basic database operate tools. 

Selects
-------

Retrieving
^^^^^^^^^^^
.. code-block:: python

  db.records('users').all()
  # SELECT * FROM `users`

  db.records('users').first()
  # SELECT * FROM `users` limit 1

  db.records('users').last()
  # SELECT * FROM `users`
  # then get last record

.. admonition:: Note

  .last() will query all records from database, then get last one 


Aggregates
^^^^^^^^^^
provide **count**、**max**、**min**、**avg**、**sum** aggregate methods

.. code-block:: python

  db.records('users').count()
  # SELECT COUNT(*) FROM `users`

  db.records('users').max('age')
  # SELECT MAX(`age`) FROM `users`

  db.records('users').min('age')
  # SELECT MIN(`age`) FROM `users`

  db.records('users').avg('age')
  # SELECT AVG(`age`) FROM `users`

  db.records('users').sum('age')
  # SELECT SUM(`age`) FROM `users`

Custom query fields
^^^^^^^^^^^^^^^^^^^
``*`` is the defult value if you don't set any query field.
Also, you can customize the query field.

.. code-block:: python

  db.records('users').select('age').all()
  # SELECT `age` FROM `users`
  
  db.records('users').select('age', 'name').all()
  # SELECT `age`, `name` FROM `users`

  db.records('users').select('age').select('name').all()
  # SELECT `age`, `name` FROM `users`

Raw expressions
^^^^^^^^^^^^^^^

Sometimes you may need to use a raw expression in a query. You can call raw() method

.. code-block:: python

  rs = db.raw('select * from users')
  for r in rs:
    print(r)

.. admonition:: Note
  
  Raw statements will be injected into the query as strings, 
  so you should be extremely careful to not create SQL injection vulnerabilities.

Joins
------

Inner join
^^^^^^^^^^^^
inner join is default join

.. code-block:: python

  db.records('users').join('posts', users__id="posts.user_id").all()
  # SELECT * FROM `users` INNER JOIN `posts` ON `users`.`id` = `posts`.`user_id`


Left join
^^^^^^^^^^^^
If you would like to perform a "left join" instead of an "inner join", use the leftJoin method. 

.. code-block:: python

  db.records('users').left_join('posts', on="users.id = posts.user_id").all()
  # SELECT * FROM `users` LEFT JOIN `posts` ON `users`.`id` = `posts`.`user_id`

Right join
^^^^^^^^^^^

.. code-block:: python

  db.records('users').right_join('posts', on="users.id = posts.user_id").all()
  # SELECT * FROM `users` RIGHT JOIN `posts` ON `users`.`id` = `posts`.`user_id`

Cross join
^^^^^^^^^^

.. code-block:: python
  
  db.records('users').cross_join('posts', on="users.id = posts.user_id").all()
  # SELECT * FROM `users` CROSS JOIN `posts` ON `users`.`id` = `posts`.`user_id`

Advanced usage
^^^^^^^^^^^^^^^

.. code-block:: python

  def complex(join):
    join.on('user.id=contacts.user_id') \
        .and_(user__id=10) \
        .or_(user__name='abc')
  db.records('users').join('contacts', complex).all()

  # SELECT * FROM `users` INNER JOIN `contacts` ON `user`.`id`=`contacts`.`user_id` AND `user`.`id` = 10 OR `user`.`name` = 'abc'


Unions
------

.. code-block:: python

  db.records('users').where(first_name=None).union(
    db.records('users').where(last_name=None)
  ).all()
  # SELECT * FROM `users` WHERE first_name IS NULL UNION SELECT * FROM `users` WHERE last_name IS NULL 


Where Clauses
-------------

Is null
^^^^^^^

.. code-block:: python

  db.records('users').where(name=None).all()
  # SELECT * FROM `users` WHERE `id` IS NULL 

Is not null
^^^^^^^^^^^

.. code-block:: python
  
  db.records('users').where(name__not=None).all()
  # SELECT * FROM `users` WHERE `id` IS NOT NULL 

Like
^^^^
.. code-block:: python

  db.records('users').where(name__like='%Jim%').all()
  # SELECT * FROM `users` WHERE `id` LIKE '%Jim%'

Not like
^^^^^^^^

.. code-block:: python

  db.records('users').where(name__not_like='%Jim%').all()
  # SELECT * FROM `users` WHERE `id` NOT LIKE '%Jim%'

Equal
^^^^^

.. code-block:: python

  db.records('users').where(age=10).all()
  # SELECT * FROM `users` WHERE `age` = 10

Not equal
^^^^^^^^^

.. code-block:: python

  db.records('users').where(age__not=10).all()
  # SELECT * FROM `users` WHERE `age` <> 10

Less than
^^^^^^^^^

.. code-block:: python

  db.records('users').where(id__lt=10).all()
  # SELECT * FROM `users` WHERE `id` < 10

Less than or equal
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
  
  db.records('users').where(id__lte=10).all()
  # SELECT * FROM `users` WHERE `id` <= 10

Great than
^^^^^^^^^^^
.. code-block:: python

  db.records('users').where(id__gt=10).all()
  # SELECT * FROM `users` WHERE `id` > 10

Great than or equal
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  db.records('users').where(id__gte=10).all()
  # SELECT * FROM `users` WHERE `id` >= 10

Between and
^^^^^^^^^^^^^^^

.. code-block:: python

  db.records('users').where(id__bt=[1, 5]).all()
  # SELECT * FROM `users` WHERE `id` BETWEEN 1 AND 5

Not between and
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  db.records('users').where(id__not_bt=[1, 5]).all()
  # SELECT * FROM `users` WHERE `id` NOT BETWEEN 1 AND 5

IN
^^^

.. code-block:: python

  db.records('users').where(id=[1, 5]).all()
  # SELECT * FROM `users` WHERE `id` IN (1, 5)


Not in
^^^^^^^^^

.. code-block:: python
  
  db.records('users').where(id__not=[1, 5]).all()
  # SELECT * FROM `users` WHERE `id` NOT IN (1, 5)

Parameter grouping
^^^^^^^^^^^^^^^^^^

.. code-block:: python

  db.records('users').where(id__not=[1, 5]).where(
	  WhereClause().and_(name='jim').or_(name='lucy')
  ).all()
  # SELECT * FROM `users` WHERE `id` NOT IN (1, 5) AND ( `name` = 'jim' OR `name` = 'lucy' )

Where Exists
^^^^^^^^^^^^

.. code-block:: python
  
  users = db.records('users').where_exists(
    db.records('mobiles').where(name='iphone'),
    db.records('mobiles').where(name='aphone')
  ).all()
  # SELECT * FROM `users` WHERE EXISTS (SELECT * FROM `mobiles` WHERE `name` = 'iphone') AND EXISTS (SELECT * FROM `mobiles` WHERE `name` = 'aphone')

Order By
--------

.. code-block:: python

  db.records('users').order_by('id')
  # SELECT * FROM `users` ORDER BY `id`

  db.records('users').order_by('id', False)
  # SELECT * FROM `users` ORDER BY `id`

  db.records('users').order_by('id', True)
  # SELECT * FROM `users` ORDER BY `id` DESC

Group By / Having
-----------------

.. code-block:: python

  db.records('users').group_by('school_id').having(school_id__bt=[1, 100]).all()
  # SELECT * FROM `users` GROUP BY `school_id` HAVING `school_id` BETWEEN 1 AND 100


Page
----

Limit / Offset
^^^^^^^^^^^^^^

.. code-block:: python

  db.records('users').limit(10).offset(5).all()
  # SELECT * FROM `users` LIMIT 10 OFFSET 5

Paginator
^^^^^^^^^

.. code-block:: python
  
  db.records('users').page(3, 15).all()
  # SELECT * FROM `users` LIMIT 15 OFFSET 30


Inserts
-------

Single insert and get id
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
  
  db.records('users').insert_getid(id=3, name='jim', age=23)
  # INSERT INTO `users` (`id`, `name`, `age`) VALUES (3, 'jim', 23)


Single insert and get how many records insert successful
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  db.records('users').insert(id=3, name='jim', age=23)
  # INSERT INTO `users` (`id`, `name`, `age`) VALUES (3, 'jim', 23)


Multiple insert and get how many records insert successful
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
  
  db.records('users').insert([
    dict(id=3, name='jim', age=23),
    dict(id=5, name='lily', age=32),
  ])
  # INSERT INTO `users` (`id`, `name`, `age`) VALUES (3, 'jim', 23), (5, 'lily', 32)


Updates
-------

Updating Columns
^^^^^^^^^^^^^^^^

.. code-block:: python
  
  db.records('users').where(id__gt=10).update(age=30, gender='m')
  # UPDATE `users` SET `age` = 30, `gender` = 'm' WHERE id > 10

Increment and Decrement
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
  
  db.records('users').increment(age=10, score=20)
  # UPDATE `users` SET `age` = `age` + 10, `score` = `score` + 20

  db.records('users').decrement(age=10, score=20)
  # UPDATE `users` SET `age` = `age` - 10, `score` = `score` - 20


Deletes
-------

Delete
^^^^^^

.. code-block:: python
  
  db.records('users').delete()
  
  # DELETE `users`


Truncate
^^^^^^^^

.. code-block:: python

  db.records('users').truncate()
  # TRUNCATE `users`

Locking
-------

read lock
^^^^^^^^^

.. code-block:: python

  db.records('users') \
    .select('users.id', 'cars.name') \
    .left_join('cars', 'users.id=cars.user_id') \
    .where(car_id=10) \
    .read_lock()
  # SELECT `users`.`id`, `cars`.`name` FROM `users` LEFT JOIN `cars` ON `users`.`id` = `cars`.`user_id` WHERE `car_id` = 10 LOCK IN SHARE MODE'

write lock
^^^^^^^^^^

.. code-block:: python

  db.records('users') \
    .select('user.id') \
    .select('cars.name') \
    .left_join('cars', 'users.id=cars.user_id') \
    .where(car_id=10) \
    .write_lock()
  # SELECT `users`.`id`, `cars`.`name` FROM `users` LEFT JOIN `cars` ON `users`.`id` = `cars`.`user_id` WHERE `car_id` = 10 FOR UPDATE

Transaction
-----------

.. code-block:: python

  with db.transction():
    db.records('users').insert([
      dict(id=3, name='jim', age=23),
      dict(id=5, name='lily', age=32),
    ])
