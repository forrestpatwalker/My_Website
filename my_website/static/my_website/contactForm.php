<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require '/home/dh_8ib2x2/PHPMailer/src/Exception.php';
require '/home/dh_8ib2x2/PHPMailer/src/PHPMailer.php';
require '/home/dh_8ib2x2/PHPMailer/src/SMTP.php';


$name = $_POST['name'];
$message = $_POST['message'];
$emailFrom = $_POST['email'];
$formContent = "$message Email: $emailFrom";

$mail = new PHPMailer(true);                              // Passing `true` enables exceptions
try {
    //Server settings
    $mail->SMTPDebug = 0;                                 // Enable verbose debug output (Change to 2 to print a detailed report to the screen)
    $mail->isSMTP();                                      // Set mailer to use SMTP
    $mail->Host = 'smtp.dreamhost.com';                   // Specify main and backup SMTP servers
    $mail->SMTPAuth = true;                               // Enable SMTP authentication
    $mail->Username = 'This is a secret';       // SMTP username
    $mail->Password = 'This is a secret';         // SMTP password
    $mail->SMTPSecure = 'ssl';                            // Enable SSL encryption, TLS also accepted with port 465
    $mail->Port = 465;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('Secret', 'Secret');          //This is the email your form sends From
    $mail->addAddress('Secret', 'Secret'); // Add a recipient address


    //Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = "$name sent you a message.";
    $mail->Body    = $message;

    $mail->send();
    echo 'Message has been sent.';
} catch (Exception $e) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
?>