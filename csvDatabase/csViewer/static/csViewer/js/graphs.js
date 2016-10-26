function beautify(data) {
	// make crossfilter references and dimensions
	var ndx = crossfilter(data);
	// console.log(data);
	var cosElementNumber = ndx.dimension(function(d){ return d.cosElementNumber; });
	// console.log(cosElementNumber);
	var cosElementName = ndx.dimension(function(d){ return d.cosElementName;});
	// console.log(cosElementName.top(10));
	var ps0 = ndx.dimension(function(d) {return d.ps0;});
	// console.log(ps0.top(10));
	var ps2 = ndx.dimension(function(d) {return d.ps2;});
	// console.log(ps2.top(10));
	var ps4 = ndx.dimension(function(d) {return d.ps4;});
	// console.log(ps4.top(10));
	var actual = ndx.dimension(function(d) {return d.actual;});
	// console.log(actual.top(10));
	var commitment = ndx.dimension(function(d){ return d.commitment;});
	// console.log(commitment.top(10));
	var poc = ndx.dimension(function(d){ return d.poc;});
	// console.log(poc.top(10));
	
	// make groups by which data can be represented
	var groupByps0 = cosElementName.group().reduceSum(function(d){ return d.ps0;});
	// make another 

	// make group for ps1vsps4
	var groupbyps2 = cosElementName.group().reduceSum(function(d){ return d.ps2; });
	var groupByps4 = cosElementName.group().reduceSum(function(d){ return d.ps4; });

	var margin = {top:50, right:50, bottom:50, left:50}, 
		width = 1100 - margin.left - margin.right, 
		height = 600 -margin.top - margin.bottom
	
	var x = d3.scale.linear()
		.range([0, width]); 
	var y = d3.scale.linear()
		.range([height, 0]);
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient('bottom');
	var yAxis = d3.svg.axis()
		.scale(y)
		.orient('left');

	// for all x scales to be named
	var ordinalScale = d3.scale.ordinal()
		.domain(data.map(function (d){
			return d.cosElementName;
		}));

	var sec =	dc.barChart('#sec')
				.width(width)
				.height(height)
				.dimension(ordinalScale)
				.group(groupByps4)
				.x(ordinalScale)
				.y(y)
				.xUnits(dc.units.ordinal)
				.brushOn(true)
				.elasticY(true)
				.elasticX(true);

	sec.on('pretransition', function(chart){
		chart.selectAll('g.x text')
		.attr('transform', 'translate(-10) rotate(300)')
		.attr('style', 'text-anchor:end');
	});

	dc.renderAll();

};