<?php
if (isset($_POST['signup'])) {
    if (isset($_POST['Username']) && isset($_POST['Password']) &&
        isset($_POST['Gender']) && isset($_POST['Age']) &&
        isset($_POST['Email']) && isset($_POST['Mobile no'])) {
        
        $username = $_POST['Username'];
        $password = $_POST['Password'];
        $gender = $_POST['Gender'];
	$age = $_POST['Age'];
        $email = $_POST['Email'];
        $phoneCode = $_POST['Mobile no'];
        $host = "localhost";
        $dbUsername = "root";
        $dbPassword = "";
        $dbName = "test";
        $conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);
        if ($conn->connect_error) {
            die('Could not connect to the database.');
        }
        else {
            $Select = "SELECT email FROM register WHERE email = ? LIMIT 1";
            $Insert = "INSERT INTO register(Username, Password, Gender, Age, Email, Mobile no) values(?, ?, ?, ?, ?, ?)";
            $stmt = $conn->prepare($Select);
            $stmt->bind_param("s", $email);
            $stmt->execute();
            $stmt->bind_result($resultEmail);
            $stmt->store_result();
            $stmt->fetch();
            $rnum = $stmt->num_rows;
            if ($rnum == 0) {
                $stmt->close();
                $stmt = $conn->prepare($Insert);
                $stmt->bind_param("ssssii",$Username, $Password, $Gender, $Age, $Email, $Mobile no);
                if ($stmt->execute()) {
                    echo "New record inserted sucessfully.";
                }
                else {
                    echo $stmt->error;
                }
            }
            else {
                echo "Someone already registers using this email.";
            }
            $stmt->close();
            $conn->close();
        }
    }
    else {
        echo "All field are required.";
        die();
    }
}
else {
    echo "Signup button is not set";
}
?>