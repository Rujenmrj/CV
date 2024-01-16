<?php
$name=$_POST['full_name'];
$mail=$_POST['email'];
if(mail($mail,"pre generated mail","Hello $name,
This is an auto generated mail 
I have received your message. I will get back to you as soon as possible"))
{
    echo "mail sent";
}
else{
    echo " unable to send mail";
}
?>