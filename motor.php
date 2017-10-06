

<?php
// Marcha para delante
if ($_POST[FORWARD]){ // condicional si se pulsa la acion
 $a- exec ("sudo python /var/www/html/motor/motor_F.py");
 echo $a;
 
}
// Marcha para detras
if ($_POST[BACKWARD]){
 $a- exec ("sudo python /var/www/html/motor/motor_B.py");
 echo $a;

}


?>

<form action="motor.php" method="POST">
Forward&nbsp<input type="submit" value="F" name="FORWARD">
<br></br>
Backwad&nbsp<input type="submit" value ="B" name ="BACKWARD">
</form>
