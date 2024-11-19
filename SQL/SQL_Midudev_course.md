# Que es SQL?

- SQL: `Structured Query Language`
- Es un lenguaje de consultas estructuradas 
- Diseñado para administrar y consultar bases de datos
- SQL es un estandar desde 1987 (`tiene una especificación`)

# Motores de bases de datos

- **mySQL**
- **postgreSQL**
- **SQLite**

Dentro de cada motor, podemos tener `bases de datos`

Cada base de datos, contiene `tablas`

# Tipos de bases de datos

## Relacionales o SQL

- Existen relaciones que evitan la duplicidad de los datos , por eso existen `relaciones` entre las tablas generalmente con **IDs**

- Cada tabla o entidad tiene `atributos`

### **Contras**
- Hacer `muchas consultas` para recuperar la info que es necesaria

### **Pros**
- `Ocupan menos lugar` porque no repiten los datos
- `Coherencia` en la información almacenada

## No relacionales o No SQL

- Colecciones de documentos que se pueden relacionar pero es más costoso

### **Contras**
- Normalizar los datos es problemático
  - Que el cambio realizado llegue a todas las referencias
- Updates en todos los documentos
- Integridad de los datos no está garantizada

### **Pros**
- Consultas `más rápidas` y especialmente las que son grandes


# Herramientas y programas

### Programas

- URL: https://dev.mysql.com/downloads/
- MySQL Community Downloads --> **MySQL Workbench** (macOS)
- MySQL Community --> **MySQL Community Installer de 430MB** (Windows)

### Herramientas para bases de dastos

- **DBngin** (recomendando macOS)
  - URL: https://dbngin.com/
  - Detecta bases, se puede iniciar MySQL, postGre, Redis
- **SQLBolt**
  - Para practicar bases de datos y sintaxis con ejercicios interactivos
  - URL: https://sqlbolt.com/

# Primeros pasos con SQL (Ejercicios de SQLBolt)

  - **IMPORTANTE**
    - **NO** es CASE SENSITIVE
  - **RECOMENDABLE**
    - Comandos en `MAYÚSCULAS`
    - Nombre de columnas o tablas en `minúsculas`

    ## **SQLBolt Lessons** 
    ## Lesson 1 : SELECT Queries

    Utilizando la siguiente tabla como ejemplo:

    | id  | Title           | Director       | Year | Length (minutes) |
    |-----|-----------------|----------------|------|-------------------|
    | 1   | Toy Story       | John Lasseter  | 1995 | 81                |
    | 2   | A Bug's Life    | John Lasseter  | 1998 | 95                |
    | 3   | Toy Story 2     | John Lasseter  | 1999 | 93                |
    | 4   | Monsters, Inc.  | Pete Docter    | 2001 | 92                |
    | 5   | Finding Nemo    | Andrew Stanton | 2003 | 107               |
    | 6   | The Incredibles | Brad Bird      | 2004 | 116               |
    | 7   | Cars            | John Lasseter  | 2006 | 117               |
    | 8   | Ratatouille     | Brad Bird      | 2007 | 115               |
    | 9   | WALL-E          | Andrew Stanton | 2008 | 104               |
    | 10  | Up              | Pete Docter    | 2009 | 101               |

    ### Queries

        SELECT * FROM movies

    Trae `todas` las columnas de la tabla `movies`

        SELECT director FROM movies
    Trae la columna `director` de la tabla `movies`

        SELECT director, titles FROM movies
    Trae las columnas `director` y `titles` de la tabla `movies`

    ------------------------

    ## Lesson 2: Queries con CONSTRAINTS

    Permiten filtrar los resultados de consultas con el operador `WHERE`

        SELECT column, another_column, … 
        FROM mytable WHERE condition
        AND/OR another_condition
        AND/OR …;

    ### Operadores para **data numérica**:


    | Operator              | Condition                                 | SQL Example                        |
    |-----------------------|--------------------------------------------|------------------------------------|
    | =, !=, <, <=, >, >=   | Standard numerical operators               | `col_name != 4`                   |
    | BETWEEN … AND …       | Number is within range of two values (inclusive) | `col_name BETWEEN 1.5 AND 10.5`    |
    | NOT BETWEEN … AND …   | Number is not within range of two values (inclusive) | `col_name NOT BETWEEN 1 AND 10`    |
    | IN (…)                | Number exists in a list                    | `col_name IN (2, 4, 6)`            |
    | NOT IN (…)            | Number does not exist in a list            | `col_name NOT IN (1, 3, 5)`        |


    ### Utilizando la tabla anterior como ejemplo:

        SELECT * FROM movies WHERE id = 6;
    Trae todo de la tabla `movies` que tenga el ID = 6 

        SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
    Trae todo de la tabla `movies` que tenga el `year` entre el 2000 y el 2010 

        SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
    Trae todo de la tabla `movies` que **NO** tenga el `year` entre el 2000 y el 2010 

        SELECT * FROM movies WHERE id BETWEEN 1 AND 5;
        
    Trae todo de la tabla `movies` que tenga el `id` entre el 1 y el 5, es decir los 5 primeros ya que el ID es `autoincremental`.
     

    ------------------------
  
    ## Lesson 3: Queries con CONSTRAINTS parte 2

    ### Operadores para **data de texto**:

    | Operator    | Condition                                            | Example                                   |
    |-------------|-------------------------------------------------------|-------------------------------------------|
    | =           | Case sensitive exact string comparison (notice the single equals) | `col_name = "abc"`                        |
    | != or <>    | Case sensitive exact string inequality comparison     | `col_name != "abcd"`                      |
    | LIKE        | Case insensitive exact string comparison              | `col_name LIKE "ABC"`                     |
    | NOT LIKE    | Case insensitive exact string inequality comparison   | `col_name NOT LIKE "ABCD"`                |
    | %           | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | `col_name LIKE "%AT%"` (matches "AT", "ATTIC", "CAT" or even "BATS") |
    | _           | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE) | `col_name LIKE "AN_"` (matches "AND", but not "AN") |
    | IN (…)      | String exists in a list                               | `col_name IN ("A", "B", "C")`             |
    | NOT IN (…)  | String does not exist in a list                       | `col_name NOT IN ("D", "E", "F")`         |

 
    ### A raiz de la siguiente tabla:


    | id   | Title                 | Director         | Year | Length (minutes) |
    |------|-----------------------|------------------|------|-------------------|
    | 1    | Toy Story             | John Lasseter    | 1995 | 81                |
    | 2    | A Bug's Life          | John Lasseter    | 1998 | 95                |
    | 3    | Toy Story 2           | John Lasseter    | 1999 | 93                |
    | 4    | Monsters, Inc.        | Pete Docter      | 2001 | 92                |
    | 5    | Finding Nemo          | Andrew Stanton   | 2003 | 107               |
    | 6    | The Incredibles       | Brad Bird        | 2004 | 116               |
    | 7    | Cars                  | John Lasseter    | 2006 | 117               |
    | 8    | Ratatouille           | Brad Bird        | 2007 | 115               |
    | 9    | WALL-E                | Andrew Stanton   | 2008 | 104               |
    | 10   | Up                    | Pete Docter      | 2009 | 101               |
    | 11   | Toy Story 3           | Lee Unkrich      | 2010 | 103               |
    | 12   | Cars 2                | John Lasseter    | 2011 | 120               |
    | 13   | Brave                 | Brenda Chapman   | 2012 | 102               |
    | 14   | Monsters University   | Dan Scanlon      | 2013 | 110               |
    | 87   | WALL-G                | Brenda Chapman   | 2042 | 97                |

    ### Queries

        SELECT title FROM movies WHERE title LIKE "Toy Story%";
    
  - Trae las filas de la columna `title` que contengan el texto `"Toy Story"`.
  - El `%` indica que luego hay mas caracteres.

    
        SELECT title FROM movies WHERE director LIKE "John Lasseter"
    
  - Trae las filas de la columna `title` en donde `director` sea `"John Lasseter"`.
  - El `LIKE` permite buscar por coincidencia exacta del texto **(NO ES CASE SENSITIVE)**.

        SELECT title FROM movies WHERE director NOT LIKE "John Lasseter"
    
  - Trae las filas de la columna `title` en donde `director` **NO** sea `"John Lasseter"`.
  - El `LIKE` permite buscar por coincidencia exacta del texto **(NO ES CASE SENSITIVE)**.

        SELECT title FROM movies WHERE title LIKE "WALL-%"
    
  - Trae las filas de la columna `title` en donde contenga "WALL-"
  - El `%` indica que luego hay mas caracteres.

    ## Lesson 4: Filtrar y ordenar resultados de consultas

    ### Operador **`DISTINCT`** para **resultados únicos y no duplicados**:

        SELECT DISTINCT column, another_column, …
        FROM mytable
        WHERE condition(s);

     ### Operador **`ORDER BY`** para **ordenar resultados en ascedente o descendente**:

        SELECT column, another_column, …
        FROM mytable
        WHERE condition(s)
        ORDER BY column ASC/DESC;

  
     ### Operadores **`LIMIT`** y **`OFFSET`** para **limitar  y saltear resultados**:

        SELECT column, another_column, …
        FROM mytable
        WHERE condition(s)
        ORDER BY column ASC/DESC
        LIMIT num_limit OFFSET num_offset;

       ### A raiz de la siguiente tabla:

      | id   | Title                 | Director         | Year | Length (minutes) |
      |------|-----------------------|------------------|------|-------------------|
      | 1    | Monsters, Inc.        | Pete Docter      | 2001 | 92                |
      | 2    | Up                    | Pete Docter      | 2009 | 101               |
      | 3    | The Incredibles       | Brad Bird        | 2004 | 116               |
      | 4    | Toy Story 3           | Lee Unkrich      | 2010 | 103               |
      | 5    | A Bug's Life          | John Lasseter    | 1998 | 95                |
      | 6    | Toy Story 2           | John Lasseter    | 1999 | 93                |
      | 7    | Brave                 | Brenda Chapman   | 2012 | 102               |
      | 8    | Monsters University   | Dan Scanlon      | 2013 | 110               |
      | 9    | WALL-E                | Andrew Stanton   | 2008 | 104               |
      | 10   | Toy Story             | John Lasseter    | 1995 | 81                |
      | 11   | Cars                  | John Lasseter    | 2006 | 117               |
      | 12   | Finding Nemo          | Andrew Stanton   | 2003 | 107               |
      | 13   | Ratatouille           | Brad Bird        | 2007 | 115               |
      | 14   | Cars 2                | John Lasseter    | 2011 | 120               |


      ### Queries

        SELECT DISTINCT director FROM movies ORDER BY director ASC;
  - Trae las filas de la columna `director` ordenadas alfabéticamente y sin repetirse.
  - Por defector, ORDER BY es ASC (ascedente). Puede o no ponerse el ASC.

         SELECT * FROM movies ORDER BY year DESC LIMIT 4
  - Trae todas las filas ordenadas por la columna `year` en orden descendente (por mas recientes)
  - `LIMIT` permite traer una cantidad fija, en este caso 4

        SELECT * FROM movies ORDER BY title ASC LIMIT 5
  - Trae todas las filas ordenadas por la columna `title` en orden ascedente (alfabéticamente)
  - `LIMIT` permite traer una cantidad fija, en este caso 5

        SELECT * FROM movies ORDER BY title ASC LIMIT 5 OFFSET 5
  - Trae todas las filas ordenadas por la columna `title` en orden ascedente (alfabéticamente)
  - `LIMIT` permite traer una cantidad fija, en este caso 5
  - `OFFSET` permite traer las **PROXIMAS** filas, en este caso salteando las 5 primeras