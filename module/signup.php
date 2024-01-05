//<?php
//
///* 
// * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
// * Click nbfs://nbhost/SystemFileSystem/Templates/Scripting/EmptyPHP.php to edit this template
// */
//// put your code here
//                $servername = "localhost";
//                $username = "root";
//                $password = "root";
////               mysqli_query($conn,"Create database php1");
//                $database='php1';
//                $conn1 = mysqli_connect($servername, $username, $password,$database);
//                if (!$conn1) {
//                  die("Connection failed: " . mysqli_connect_error());
//                }
//                echo '<br>Connected successfully<br>';
//                
////                if (mysqli_query($conn1, "create table form(user varchar(30),password varchar(30))")) {
////                    echo ("table created sucessfully<br>");
////                }
//                
//                $user = $_POST['username'];
//                $pass = $_POST['password'];
//                if (mysqli_query($conn1, "insert into form values('$user','$pass')")) {
//                    echo("added sucessfully");
//                }