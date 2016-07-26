var etatL = 0
var etatR = 0

function OngletLeft()
{	
	if (etatL == 0 )
	{
		if (etatR == 1)
		{
		document.getElementById('right').style.visibility = "hidden";
		etatR = 0;
		document.getElementById('left').style.visibility = "visible";
		etatL = 1;
		}
		else 
		{
			document.getElementById('left').style.visibility = "visible";
			etatL = 1;
		}
	}
	else 
	{
		document.getElementById('left').style.visibility = "hidden";
		etatL = 0;
	}
}

function OngletRight()
{	
	if (etatR == 0)
	{
		if (etatL == 1)
		{
			document.getElementById('left').style.visibility = "hidden";
			etatL = 0;
			document.getElementById('right').style.visibility = "visible";
			etatR = 1;
		}
		else 
		{
			document.getElementById('right').style.visibility = "visible";
			etatR = 1;
		}
	}
	else 
	{
		document.getElementById('right').style.visibility = "hidden";
		etatR = 0;
	}
}

