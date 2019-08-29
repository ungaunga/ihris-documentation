Migrating from MDB2 to PDO
==========================

==Server Changes==
For Ubuntu 14.04, you must replace the default PHP MySQL driver:
<source lang="bash">
sudo apt install php5-mysqlnd
</source>

==PHP Code Changes==
===Update Database Reference===
In the below examples, <code>$db</code> will refer to the database object that was returned from <code>MDB2::singleton()</code> or <code>I2CE::PDO()</code> or it may refer to those strings exactly.  You may see <code>$db->prepare(...)</code> or <code>MDB2::singleton()->prepare(...)</code>.

Change: <source lang="php">MDB2::singleton()</source>  to: <source lang="php">I2CE::PDO()</source>

===Update Error Checks (for all database queries)===
Change pearError blocks to try catch:
<source lang="php">
$result = $db->query($qry);
if ( I2CE::pearError( $result, "MESSAGE" ) ) {
    return false;
}
</source>
becomes:
<source lang="php">
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
</source>

===Prepared Statements===
Remove extra arguments for field types from the call to prepare().  

Prepared statements also act as the result.  Note that in many cases the prepare statement will be in a different place than the execute and fetch calls.
<source lang="php">
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
</source>
becomes:
<source lang="php">
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
</source>

===execParam method===
Change:
<source lang="php">
$db->execParam( $qry, $params, $types );
</source>
to:
<source lang="php">
try {
    I2CE_PDO::execParam( $qry, $params );
} catch ( PDOException $e ) {
    I2CE::pdoError( $e, "MESSAGE" );
}
</source>

===getRow method===
Change:
<source lang="php">
$row = $db->getRow( $qry, $types, $params, $param_types );
if ( I2CE::pearError( $row, "ERROR " ) ) {
    return false;
}
</source>
To:
<source lang="php">
try {
    $row = I2CE_PDO::getRow( $qry, $params );
} catch( PDOException $e ) {
    I2CE::pdoError( $e, "ERROR" );
    return false;
}
</source>

===getBeforeID/getAfterID (sequence) methods===

Change:
<source lang="php">
$new_id = $this->db->getBeforeID( $table, $col, true, true );
$this->db->exec( $stmt );
$new_id = $this->db->getAfterID( $new_id, $table, $col );
</source>
To:
<source lang="php">
$this->db->exec( $stmt );
$new_id = $this->db->lastInsertId();
</source>

===queryCol method===
Change: 
<source lang="php">
$var = $db->queryCol( $qry, # )
</source>
to: 
<source lang="php">
$result = $pdo->query( $qry );
$var = $result->fetchAll( PDO::FETCH_COLUMN, # );
</source>

===queryAll method===
Change: 
<source lang="php">
$var = $db->queryAll( $qry )
</source>
to: 
<source lang="php">
$result = $pdo->query( $qry );
$var = $result->fetchAll();
</source>

===getOne method===
Change: 
<source lang="php">
$res = $db->getOne( $qry );
</source>
to: 
<source lang="php">
$result = $pdo->query( $qry );
$res = $result->fetchColumn();
</source>

===mysql_real_escape_string function===
If there is no other option to replace mysql_real_escape_string then do the following.  '''Note that $db->quote() will return a string in quotes that is also escaped.'''
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

===Method and Field changes===
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
