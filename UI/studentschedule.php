<!DOCTYPE html>
<html>
<head>
	<title>Student Schedule</title>
</head>
<body>
    <?php 
        $name = false;
        if(isset($_POST['studentName'])){
            $name = $_POST['studentName'];
        }
        ?>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="main.css">
    <meta name="viewport" content="width=device-width" />

    <script> var name = '<?php echo $name; ?>';</script>
    <script type="text/javascript" src="stud.js"></script>


    
</body>
</html>