-- CREATE
TABLE
IF
NOT
EXISTS
public.categories
-- (
    --     id integer NOT NULL DEFAULT nextval('categories_id_seq'::regclass),
--     name
character
varying(20)
COLLATE
pg_catalog.
"default"
NOT
NULL,
--     CONSTRAINT
categories_pkey
PRIMARY
KEY(id)
- - )

-- CREATE
TABLE
IF
NOT
EXISTS
public.employees
-- (
    --     id integer NOT NULL DEFAULT nextval('employees_id_seq'::regclass),
--     first_name
character
varying(30)
COLLATE
pg_catalog.
"default"
NOT
NULL,
--     last_name
character
varying(30)
COLLATE
pg_catalog.
"default"
NOT
NULL,
--     CONSTRAINT
employees_pkey
PRIMARY
KEY(id)
- - )

-- CREATE
TABLE
IF
NOT
EXISTS
public.products
-- (
    --     id integer NOT NULL DEFAULT nextval('products_id_seq'::regclass),
--     name
character
varying(15)
COLLATE
pg_catalog.
"default"
NOT
NULL,
--     category_id
integer,
--     CONSTRAINT
products_pkey
PRIMARY
KEY(id),
--     CONSTRAINT
fk_products_categories
FOREIGN
KEY(category_id)
- -         REFERENCES
public.categories(id)
MATCH
SIMPLE
- -         ON
UPDATE
NO
ACTION
- -         ON
DELETE
NO
ACTION
- - )

-- INSERT
INTO
employees(first_name, last_name)
-- VALUES('Emil', 'Enchev'),
--    ('Maria', 'Peshova')

-- INSERT
INTO
employees(first_name, last_name)
-- VALUES('Emil', 'Ivanov'),
--    ('Maria', 'Stefanova')

-- INSERT
INTO
categories(name)
-- VALUES('beer'),
--       ('milk'),
--       ('snacks')

-- INSERT
INTO
products(name, category_id)
-- VALUES('good beer', 1),
--       ('good milk', 2),
--       ('good snak', 3),
--       ('bad beer', 1),
--       ('bad milk', 2),
--       ('bad snak', 3)

-- SELECT *
-- FROM
employees

-- SELECT
id, last_name
-- FROM
employees

-- SELECT
id, CONCAT_WS(' ', last_name, first_name)
-- FROM
employees

-- SELECT
id, CONCAT_WS(' ', last_name, first_name)
-- FROM
employees
-- LIMIT
1

-- SELECT
id, CONCAT_WS(' ', last_name, first_name)
-- FROM
employees

-- SELECT
id, CONCAT_WS(' ', last_name, first_name)
AS
name
-- FROM
employees
-- LIMIT
1
-- WHERE
first_name
LIKE
'M%'

-- SELECT
id, CONCAT_WS(' ', last_name, first_name)
AS
name
-- FROM
employees
-- WHERE
CONCAT_WS(' ', last_name, first_name)
LIKE
'%h%'

-- SELECT
id, CONCAT_WS(' ', last_name, first_name)
AS
name
-- FROM
employees
-- WHERE
first_name = 'Emil'

-- ALTER
TABLE
employees
-- ADD
COLUMN
salary
DECIMAL

-- ALTER
TABLE
employees
-- DROP
COLUMN
salary

SELECT *
FROM
products
RIGHT
JOIN
categories
ON
products.category_id = categories.id
-- WHERE
categories.name = 'beer'
WHERE
categories.name
IN('beer', 'milk')
ORDER
BY
categories.name, products.name
DESC