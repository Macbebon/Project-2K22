
    <body>
        <div class="wrapper">
            
        <div class="header">
            <img src="header.jpg" height="100%" width="100%"/>
            </div>
            <div class="navbar">
                
            <ul>
            <li><a href="index.php">Home</a></li>
			<?php
			if(!isset($_SESSION['customer_login']) && !isset($_SESSION['admin_login']) && !isset($_SESSION['staff_login'])) 
			{
			?>
            <li><a href="features.php">Features</a></li>
			
			<li><a href="staff_login.php">Staff Login </a></li>
            <li><a href="adminlogin.php">Admin Login </a></li>
			
				<li id="last"><a href="loan.php">Loan</a></li>
            <li id="last"><a href="contact.php">Contact Us</a></li>
			<li id="last"><a href="about.php">About Us</a></li>
			
			<?php
			}
			?>
			
			
			
			
			
			
			
			
			
            </ul>
            </div>