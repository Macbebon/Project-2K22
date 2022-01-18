<?php
$serverName="localhost";
$dbusername="root";
$dbpassword="";
$dbname="bank_db";
$cid = mysqli_connect($serverName,$dbusername,$dbpassword) or die('the website is down for maintainance');
mysqli_select_db($cid,$dbname) or die(mysql_error());
?>