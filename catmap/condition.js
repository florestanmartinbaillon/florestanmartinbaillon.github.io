Decimal.precision = 500
phi = Decimal(1).plus(Decimal(5).sqrt()).div(Decimal(2))

un = Decimal(1)

// k = Decimal(123)
// N = Decimal(100)
// eps = Decimal(0.1)

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
	// let k = document.getElementById("k").value;
	let Nmin = document.getElementById("Nmin").value;
	let Nmax = document.getElementById("Nmax").value;
	let eps = document.getElementById("eps").value;
	let prec = document.getElementById("prec").value;


	Decimal.precision = Number(prec)

	// k = Decimal(k)
	// N = Decimal(N)
	Nmin = Number(Nmin)
	Nmax = Number(Nmax)
	eps = Decimal(eps)
	
	// cond = condition(k, N, eps)

	document.getElementById("result").innerHTML = '';

	for (let n=Nmin; n <= Nmax; n++){
		console.log(n)
		k = 1
		while (!condition(Decimal(k), Decimal(n), eps)) {
			k = k + 1
		}
		document.getElementById("result").innerHTML +=
			// `Condition: ${cond} <br/>`;
			`Pour N=${n}, eps=${eps}, premier k=${k} <br />`;
	}
}
