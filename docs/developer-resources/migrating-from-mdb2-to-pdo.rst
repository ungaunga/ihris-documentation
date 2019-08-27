Migrating from MDB2 to PDO
================================================


Server Changes
^^^^^^^^^^^^^^
For Ubuntu 14.04, you must replace the default PHP MySQL driver:


.. code-block:: bash

    sudo apt install php5-mysqlnd
    



PHP Code Changes
^^^^^^^^^^^^^^^^

Update Database Reference
~~~~~~~~~~~~~~~~~~~~~~~~~
In the below examples, <code>$db</code> will refer to the database object that was returned from <code>MDB2::singleton()</code> or <code>I2CE::PDO()</code> or it may refer to those strings exactly.  You may see <code>$db->prepare(...)</code> or <code>MDB2::singleton()->prepare(...)</code>.

Change: 

.. code-block:: php

    MDB2::singleton()
  to: 

.. code-block:: php

    I2CE::PDO()



Update Error Checks (for all database queries)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Change pearError blocks to try catch:


.. code-block:: php

    $result = $db->query($qry);
    if ( I2CE::pearError( $result, "MESSAGE" ) ) {
        return false;
    }
    

becomes:


.. code-block:: php

    try {
        $result = $db->query($qry);
        // Do something with $result
    
        // Free result
        unset( $result );  // in most cases
        $result = null;    // in big loops or very frequent functions
    } catch( PDOException $e ) {
        I2CE::pdoError( $e, "MESSAGE" );
        return false;
    }
    



Prepared Statements
~~~~~~~~~~~~~~~~~~~
Remove extra arguments for field types from the call to prepare().  

Prepared statements also act as the result.  Note that in many cases the prepare statement will be in a different place than the execute and fetch calls.


.. code-block:: php

    $stmt = $db->prepare( $qry, $field_types, MDB2_PREPARE_RESULT );
    if ( I2CE::pearError( $stmt, "MESSAGE" ) ) {
        // handle failure or exit
    }
    
    ...
    
    $result = $stmt->execute();
    if ( I2CE::pearError( $result, "MESSAGE" ) ) {
        // handle failure
    } else {
        while ( $data = $result->fetchRow() ) {
            // Do something
        }
    }
    

becomes:


.. code-block:: php

    try {
        $stmt = $db->prepare( $qry );
    catch ( PDOException $e ) {
        I2CE::pdoError( $e, "MESSAGE" );
        // handle failure or exit
    }
    
    ...
    
    try {
        $stmt->execute();
        while( $data = $stmt->fetch() ) {
            // Do something
        }
        $stmt->closeCursor();
    } catch ( PDOException $e ) {
        I2CE::pdoError( $e, "MESSAGE" );
        // handle failure
    }
    



execParam method
~~~~~~~~~~~~~~~~
Change:


.. code-block:: php

    $db->execParam( $qry, $params, $types );
    

to:


.. code-block:: php

    try {
        I2CE_PDO::execParam( $qry, $params );
    } catch ( PDOException $e ) {
        I2CE::pdoError( $e, "MESSAGE" );
    }
    



getRow method
~~~~~~~~~~~~~
Change:


.. code-block:: php

    $row = $db->getRow( $qry, $types, $params, $param_types );
    if ( I2CE::pearError( $row, "ERROR " ) ) {
        return false;
    }
    

To:


.. code-block:: php

    try {
        $row = I2CE_PDO::getRow( $qry, $params );
    } catch( PDOException $e ) {
        I2CE::pdoError( $e, "ERROR" );
        return false;
    }
    



getBeforeID/getAfterID (sequence) methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change:


.. code-block:: php

    $new_id = $this->db->getBeforeID( $table, $col, true, true );
    $this->db->exec( $stmt );
    $new_id = $this->db->getAfterID( $new_id, $table, $col );
    

To:


.. code-block:: php

    $this->db->exec( $stmt );
    $new_id = $this->db->lastInsertId();
    



queryCol method
~~~~~~~~~~~~~~~
Change: 


.. code-block:: php

    $var = $db->queryCol( $qry, # )
    

to: 


.. code-block:: php

    $result = $pdo->query( $qry );
    $var = $result->fetchAll( PDO::FETCH_COLUMN, # );
    



queryAll method
~~~~~~~~~~~~~~~
Change: 


.. code-block:: php

    $var = $db->queryAll( $qry )
    

to: 
<source lang="php">
$result = $pdo->query( $qry );
$var = $result->fetchAll();
</source>


getOne method
~~~~~~~~~~~~~
Change: 
<source lang="php">
$res = $db->getOne( $qry );
</source>
to: 
<source lang="php">
$result = $pdo->query( $qry );
$res = $result->fetchColumn();
</source>


mysql_real_escape_string function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If there is no other option to replace mysql_real_escape_string then do the following.  **Note that $db->quote() will return a string in quotes that is also escaped.**
Change: 
<source lang="php">
"'" . mysql_real_escape_string($var) . "'"
</source>
to: 
<source lang="php">
$db->quote( $var )
</source>
If you don't need it to return quotes, then change: 
<source lang="php">
mysql_real_escape_string()
</source>
to:
<source lang="php">
I2CE_PDO::escape_string()
</source>


Method and Field changes
~~~~~~~~~~~~~~~~~~~~~~~~
{| class="wikitable"
! Change 
! To
|-
| <code>numRows()</code>
| <code>rowCount()</code>
|-
| <code>fetchRow()</code>
| <code>fetch()</code>
|-
| <code>in_transaction</code>
| <code>inTransaction()</code>
|-
| <code>$db->database_name</code>
| <code>I2CE_PDO::details('dbname')</code>
|-
| <code>$db->dsn['username']</code>
| <code>I2CE_PDO::details('user')</code>
|-
| <code>$db->dsn['password']</code>
| <code>I2CE_PDO::details('pass')</code>
|-
| <code>$db->getOption('result_buffering')</code>
| <code>$db->getAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY)</code>
|}

[[Category:Developer Resources]]
