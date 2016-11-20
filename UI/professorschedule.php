<!DOCTYPE html>
<html>
<head>
	<title>Student Schedule</title>
</head>
<body>
<?php
    $class = false;
    if(isset($_POST['className'])){
        $class = $_POST['className'];
    }?>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<link rel="stylesheet" type="text/css" href="main.css">
	<meta name="viewport" content="width=device-width" />

	<script> var className = '<?php echo $class; ?>';</script>
	<script type="text/javascript" src="prof.js"></script>



</body>
</html>