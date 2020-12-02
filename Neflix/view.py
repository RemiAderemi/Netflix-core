#!C:\Python\python.exe
print("Content-type: text/html\n\n")

import model

def head():
    html="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="netflix.css">
    <title>Netflix</title>
	<link rel="icon" type="image/png" sizes="96x96" href="images/favicon.png">
	<meta name=”viewport” content=”width=device-width, initial-scale=1”>
</head>
<body>
    """
    return html

def home():
    html="""
    <div id="background-image">

		<div id="black-cover">

			<div id="before-login">
				<img id="logo" src="./images/netflix-logo.png">
				<a href="login.py" id="sign-in-link">Sign In</a>
			</div>
			<div id="center">
				<h1>Unlimited movies, TV<br>shows and more.</h1>

				<div id="description">
					Watch anywhere. Cancel anytime.
				</div>

				<div id="input-area">
					<input type="text" placeholder="Email address">
					<button type="button">TRY IT NOW</button>
				</div>
			</div>

		</div>

	</div>
    """
    return html

def login():
    html="""
    <div id="black">

			<div id="before-login">
				<img id="logo" src="./images/netflix-logo.png">
				<a href="sign_up.py" id="sign-in-link">Sign Up</a>
			</div>

			<form id="netform.py" action="netform.py" Method="POST" enctype="multipart/form-data">
				<h1>Sign In</h1>
				<input type="text" name="in_email" placeholder="Email address">
				<input type="password" name="in_password" placeholder="Password">
				<input type="submit" value="Sign In">
			</form>

	</div>
    """
    return html



def sign_up():
    html="""

    <div id="black">

			<div id="before-login">
				<img id="logo" src="./images/netflix-logo.png">
				<a href="login.html" id="sign-in-link">Sign In</a>
			</div>

			<form id="netform.py" action="netform.py" type="post" method="POST">
				<h1>Sign Up</h1>
				<input type="text" name="up_name" placeholder="Full Name">
				<input type="text" name="up_email" placeholder="Email address">
				<input type="password" name="up_password" placeholder="Password">
				<input type="password" name="password_confirm" placeholder="Confirm Password">
				<input type="submit" value="Sign Up">
			</form>

	</div>
    """
    return html

def movie_list():
    html="""
    <div id="header-after-login">
		<img id="menu" class="js-menu" src="./images/menu.svg">
		<nav>
			<img id="menu" class="js-menu" src="./images/menu.svg">
			<ul>
				<li><a href="movie-list.html">HOME</a></li>
			</ul>
		</nav>

		<img id="logo" src="./images/netflix-logo.png">
	</div>

	<div id="movies">

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
			</div>
		</div>

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
			</div>
		</div>

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
			</div>
		</div>

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
			</div>
		</div>

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
			</div>
		</div>

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
			</div>
		</div>

		<h2 class="movie-category">Drama</h2>
		<div class="movie-slider">
			<div class="movie-slider-inside">
				<a href="movie-detail.html"><img src="images/movies/1.png"></a>
				<a href="movie-detail.html"><img src="images/movies/2.png"></a>
				<a href="movie-detail.html"><img src="images/movies/3.png"></a>
				<a href="movie-detail.html"><img src="images/movies/4.png"></a>
				<a href="movie-detail.html"><img src="images/movies/5.png"></a>
			</div>
		</div>
	</div>

</div>
    """
    return html

def movie_detail():
    html="""
    <div id="header-after-login">
		<img id="menu" class="js-menu" src="./images/menu.svg">
		<nav>
			<img id="menu" class="js-menu" src="./images/menu.svg">
			<ul>
				<li><a href="movie-list.html">HOME</a></li>
			</ul>
		</nav>
		<img id="logo" src="./images/netflix-logo.png">
	</div>

	<div id="movie">
		<img src="images/movies/2.png">
		<h1 id="movie-title">VIKINGS</h1>
		<a href="https://youtube.com" id="movie-play" target="_blank">PLAY</a>
		<div id="movie-description">
			A motley crew of apocalypse servivors living at an abandoned truck stop never suspects that the pregnant woman among them is carrying the Messiah.
		</div>
	</div>
    """
    return html

def footer():
    html="""
    <script src="jquery.js"></script>
    <script type="text/javascript" src="netflix.js"></script>
</body>
</html>
    """
    return html