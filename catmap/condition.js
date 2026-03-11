Decimal.precision = 500
phi = Decimal(1).plus(Decimal(5).sqrt()).div(Decimal(2))

un = Decimal(1)

function norm(x) {
	n = x.floor()
	f = x.minus(n)
	if (f.lessThan(Decimal(0.5))) {
		return f
	}
	else {
		return un.minus(f)
	}
}

function condition(k, N, eps) {
	prod = k.mul(phi)
	sqN = N.sqrt()
	cond1 = norm(prod).lessThan(eps.div(sqN))
	cond2 = norm(prod.mul(N)).lessThan(eps.div(k))

	return (cond1 && cond2)
}

function getValues() {
	// Get values from input boxes
	let Nmin = document.getElementById("Nmin").value;
	let Nmax = document.getElementById("Nmax").value;
	let eps = document.getElementById("eps").value;
	let prec = document.getElementById("prec").value;


	Decimal.precision = Number(prec)

	Nmin = Number(Nmin)
	Nmax = Number(Nmax)
	eps = Decimal(eps)
	
	document.getElementById("result").innerHTML = '';

	for (let n=Nmin; n <= Nmax; n++){
		console.log(n)
		k = 2*n
		while (!condition(Decimal(k), Decimal(n), eps)) {
			k = k + 1
		}
		document.getElementById("result").innerHTML +=
			`Pour N=${n}, eps=${eps}, premier k=${k} <br />`;
	}
}
