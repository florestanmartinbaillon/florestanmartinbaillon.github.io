Decimal.precision = 100
phi = Decimal(1).plus(Decimal(5).sqrt()).div(Decimal(2))

un = Decimal(1)

k = Decimal(123)
N = Decimal(100)
eps = Decimal(0.1)

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
	console.log(prod.toString())
	return (cond1 && cond2)
}

function getValues() {
	// Get values from input boxes
	let k = document.getElementById("k").value;
	let N = document.getElementById("N").value;
	let eps = document.getElementById("eps").value;
	// let prec = document.getElementById("prec").value;

	k = Decimal(k)
	N = Decimal(N)
	eps = Decimal(eps)
	
	cond = condition(k, N, eps)

	document.getElementById("result").innerHTML =
		`Condition: ${cond}`;
}
