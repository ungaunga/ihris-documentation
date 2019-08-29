Importing Data
==============

This article describes the import tools developed for Botswana. The same can be adopted for other projects and be edited as necessary depending on the structure of the data you have.
The import tools for Botswana can be accessed in launchpad from  `here. <http://bazaar.launchpad.net/~ihris+botswana/ihris-botswana/4.1/files/head:/tools/>`_ 
Here there are many files, however we have one important file the  `import_base.php <http://bazaar.launchpad.net/~ihris+botswana/ihris-botswana/4.1/files/head:/tools/import_base.php>`_  which forms the basis for all the other tools. We will refer to this file in this article as simply the *Import Base* .

The Base Class
^^^^^^^^^^^^^^
The Import Base defines the classes which are then implemented by all the other tools.

Import Base
~~~~~~~~~~~
This file can be organized into different sections. The first section being lines 39-74. This is the part where we set the system wide variables like database credentials, where we find the other tools like I2CE and Command Line Interfacing tools (line 74). If you check closely, this first part resembles the site **index.php**  file.

DataFile Class
--------------
The DataFile class is the second part of import base. The DataFile class (lines 85-114) defines the abstract methods for the real classes to implement. It defines methods like getDataRow(), hasDataRow(), getHeaders() to fetch one data row at a time, to check if the file we are reading has data rows in it and to get the headers from the file respectively. We are assuming the file we are going to work with has its data organized into rows. The constructor initializes the file that we will be working on and we have a method to fetch the file name and to close the file after we have finished reading it.

CSVDataFile Class
-----------------
This is the first implementation of the DataFile class defined in the second part of the import base.

It implements the DataFile class depending on the features of the CSV File. Its constructor calls the parent constructor to initialize the file we are going to import data from, reads the size of this file and makes sure the file is open for reading otherwise it fails. (lines 123-125).

The hasDataRow() methods checks to see if there is some data in the file we just opened in the constructor. ( `ftell() method <php.net/manual/en/function.ftell.php>`_ ). Should there be no data, we return false otherwise we return true that the file has data in it.

Then we go and read the headers from this file. We assume the headers to be in the first row of the file [php.net/manual/en/function.fseek.php fseek() method) and that the separators could be one of a tab, comma or semicolon. (lines 147 and 148)

Then we read the header fields into a variable $headers line 149. Lines 150-153 we check if the $headers array has no data in it, or there are only two headers and if the user (one running the script) replies no the the displayed headers for confirmation, then we remain at the first line of the file and skip.

We assign the separator found in the file to the class feature ''''in_file_sep'''' and stop checking for more. Lines 157 - 159 we are making sure we have the separator used in the CSV file and then we remove any white spaces before and after each of the headers we have found. ( `trim() method <php.net/manual/en/function.trim.php>`_ ).

Then finally the function returns the headers we have found from the file.

The getDataRow() (lines 167-169) returns an array of data read from the file based on the separator we found above. ( `fgetcsv() function <php.net/manual/en/function.fgetcsv.php>`_ ). After we have done everything we close the file we opened.


ExcelDataFile Class
-------------------
We also assume if the data file we are reading is not a CSV then it could be an Excel spreadsheet. This is accomplished using the PHPExcel library which must be installed before this is done lines 187-189.

What this does in the constructor is initialization of the file we are going to work on like creating the reader resource, setting the file to readonly as we process, loading the file and the active sheet from the worksheet, and setting the row iterator in this worksheet.

The other methods perform the same function like in the CSVDataFile class above, except we have added a helper method _readRow, which reads the data from a row into an array and later this is used by the getHeaders() and getDataRow() methods. [This is due to the limited versatility of the PHPExcel library to process stuff more easily). More about PHPExcel library can be read from  `here <phpexcel.codeplex.com/>`_ .


Processor Class
~~~~~~~~~~~~~~~
This is the main class which does all the processing of the importing. Whenever you define a class to import some data, make sure you implement this class.

The convert() function (lines 263-267) is utility function to convert file file sizes into bytes, megabytes, gigabytes etc. depending on the size value we have.

The constructor of the class reads the file and determines whether it is a CSV or an Excel spreadsheet and initializes them accordingly lines 287-294 of the import base. Then it initializes the database user and the Form Factory instance, the bad file and test mode and creates the import logger. The import logger is a database table which keeps track of where the last import ended in case we didn't finish. The logger is somewhat for a specific file so that if we started processing a file and something happened in between before we finish we can proceed from where we ended.

The getCurrentRow() fetches one row at a time from the file and returns it for processing, the hasDataRow() makes sure we have rows in the file we are reading and returns true on success.

The run() method handles all the import processes giving the user choices whether to run the script in test or production mode giving options to skip some of the rows. It also checks to see if there are more than ten consecutive empty rows and asks the user whether to proceed or stop processing. It also checks to see, if the script is run in test mode (meaning no data is saved in the database) it echoes back **Success on Test**  meaning if we were running it in production mode this data from this row would be imported successfully into the database.

The getStats() is one of the utility method to collect statistics for the import process. At the end of the import process, the script gives statistics for the success and failed imports.

The processRow() processes each row encountered in the file and returns true on success and false on failure. If a row is processed (lines 393-395) we return a success (true) and proceed. Lines 399-404 we check if processing of the row has been successful we mark that as being processed and set that in the import logger (markProcessed()) and return true, otherwise we return false: failure.

The setTestMode() is a helper function to help set the mode of the script whether to run in test or production mode.

The save() method saves the data into the database and echoes back the row number and the form where the data is being saved and the memory used so far. If the script is run in test mode then nothing gets saved into the database lines 429-431 otherwise it saves the data with the user who saved that data and asks whether to continue or stop.

The getHeaderMap() method does some mapping of the headers from the file we are importing data from and the internal headers that you will have defined for reference. 'Check its use  `here <http://bazaar.launchpad.net/~ihris+botswana/ihris-botswana/4.1/view/head:/tools/import_infinium.php#L69>`_ . The indices of the array are the internal references to the headers found in the file to be imported. And the mapHeaders() this now maps the internal references to the column headers in the file.

The initBadFile() method (lines 520-528) initializes a file where we keep record of the import process. Every row we fail to process gets saved in this file together with the reasons for failure by adding a column at the end of the import file we are working on.

The addBadRecord() method adds all the failures into the file which holds all the unsuccessful imports.

The createLogger() method creates the database table into which we keep track of all the rows that have been processed so that next time we run the same script on the same file we proceed from where we last ended.

The alreadProcessed() method confirms that the row we are now working on has been processed or not.

The markProcessed() method marks each row as processed into the logger table.

The getDate() function is a utility function to get the current data and format it, so that we can use it in the name of the bad records that we will create later for storing unsuccessful imports.


Extending the Processor Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is the Processor which is to be extended when importing data from any CSV or Excel File you have. The order of the fields doesn't matter.

 *We are going to use the import_file_numbers.php script for this discussion to present the main logic.* 

You will need to define the getExpectedHeaders() function to say what Actual Fields you have in the Excel/CSV file and what their maps/indices are that will be used in the script.

For this case for example


.. code-block::

    protected function getExpectedHeaders() {
            return  array(
                'surname'=>'SURNAME',
                'name'=>'NAME',
                'mpf'=>'MPF',
                );
        }
    


Will Only Pick the Headers: SURNAME, NAME and MPF from the Excel/CSV datafile regardless of the number of fields there are in the file. i.e. there could be 13 headers, but we are only interested in the three. So here, SURNAME, NAME and MPF is how they are referred to in the Excel/CSV File and now internally in the script they will be referred to as **surname, name and mpf**  respectively.

The constructor makes sure the file we are loading is readily available before we start processing. And any other initializations you want to make. Here we are making sure (ensureMPFID()) we have the Man Power File Number is available in the Identification Types before we can start processing. So this sets adds the man power File Number as one of the Identification types as described here

You will also need to define the _processRow() function which ideally goes through each row and does the processing of the rows one after another...


Details of the Functions
~~~~~~~~~~~~~~~~~~~~~~~~


* ensureMPFID()
This starts from line 60 of this file where we define the id for the man power file number Identification Type. And Line 61 we set the Identification Type. 

Line 64 fetches from the database all the id present for the different identification types from the id_type form (table) then in line 65 we are checking to see if the id we defined in line 60 above is in the found values from the database. Lines 68-70 we are asking for confirmation that we didn't find the Identification Type should we create it? Then Lines 71-74 we are trying to load/initialize/set the id_type form so that we can save the new Identification Type to it. We issue an error if that fails and we stop.

Otherwise, line 75, we set the value for the name field in the id_type form which we initilized above to be Manpower File Number and line 76 we are giving it the id and we save on line 77. (Remember the id and the id_type names were set in lines 60 and 61 respectively.



* _processRow()
Here we start by making sure that we have all the data we need in order to proceed. We will check that neither of the name, surname and mpf are missing from the CSV/Excel file. If one of these is missing, then we mark this as one of the bad records line 82 and we skip, move to the next.

Lines 85-132 we are creating a WHERE clause which will try to compare when we are adding this Man Power File Number. Names in the database due to some reasons would be interchanged between surname and firstname, that's why we have the four cases.

Line 133 we are fetching all the ids for the data that just matched the WHERE clause.

Lines 134-136 check if nothing was found, then that person data (name combination) is not currently in the database and likewise lines 137-140 we check if we found more than one id for the name combination. For each case, we add this to the bad records file (line 135 and 138) and continue processing.

Line 142 we reset the array with personids we found so that the index is at zero  and line 143 we only take the current value where we are at, we then lines 144-151 create a WHERE clause to fetch only the manpowerfilenumber id.

Line 152 we are searching in the person_id form for any man power file number id_num for the persons we have found *person|.$personid* 

Next we are only checking if this person we have found has one or more than one Man Power File Numbers already set where we record that in the bad records file and continue processing.

When we are done, we then load/initialize the person_id form and echo an error and quit in case we couldn't achieve that, otherwise Lines 171-174 we set the id number (id_num) we have from the CSV/Excel file and we set the id_type value from that in the id_type form and set the parent for this value to be the person we just found.


Running the scripts
~~~~~~~~~~~~~~~~~~~
When running the scripts the invocation is


.. code-block::

    php /path/to/tools/script path/to/data_file_we_are_importing_data_from
    


e.g. if we have the script in /var/lib/iHRIS/sites/manage/tools/import_file_numbers.php and the data file in /home/sovello/Desktop/manpowerfilenumbers.csv then we would do


.. code-block::

    php /var/lib/iHRIS/sites/manage/tools/import_file_numbers.php /home/sovello/Desktop/manpowerfilenumbers.csv
    



Disclaimer
~~~~~~~~~~
The file paths in this article are based on code at  `revision 20 in Launchpad <http://bazaar.launchpad.net/~ihris+botswana/ihris-botswana/4.1/files/20>`_ .

[[Category:Botswana]]
