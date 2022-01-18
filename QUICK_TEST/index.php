<?php
if(isset($_POST['name'])){
    $server = "localhost";
    $username = "root";
    $password = "";


    $con = mysqli_connect($server,$username,$password);

    if(!$con){
        die ("Connection to this database failed".mysqli_connect_error());
    }

    $name = $_POST['name'];
    $em = $_POST['email'];
    // echo "Success Connecting to the DB";
    $sql = "INSERT INTO `24sep`.`phptes` (`ename`, `email`) VALUES ('$name', '$em');";
    // echo $sql;
    if($con->query($sql) ==true){
        echo "Sucessfully";
    }
    else{
        echo "ERROR: $sql <br> $con->error";
    }
    $con->close();
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
    <style>
        .container{
            border: 2px solid red;
            padding: 150px;
            margin :150px;
            font-size: x-large;
            
        }
    </style>
</head>
<body>
    <div class="container">
        <form action="" method="post">
            <label for="name">Name : </label><br><input type="text" value="" name="name" placeholder="Name"><br>
            <label for="name">Email :</label><br><input type="text" value="" name="email" placeholder="Email">
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>

