function beautify2(data){

	var ndx = crossfilter(data);
	var cosElementName = ndx.dimension(function(d){if(d.cosType == 'Execution Cost'){return d.cosElementName;}});
	var cosElementNamePs0 = ndx.dimension(function(d){if(d.cosType == 'Execution Cost'){return d.cosElementName;}});

	var cosElementNameChart = dc.barChart("#sec");
	var cosElementNameGroup = cosElementName.group().reduce(return d.ps2);
	var cosElementNamePs0Group = cosElementName.group().reduce(return d.ps0);

	var margin = {top:50, right:50, bottom:50, left:50}, 
		width = 700 - margin.left - margin.right, 
		height = 300 -margin.top - margin.bottom
	
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

	var ordinalScale = d3.scale.ordinal()
		.domain(data.map(function (d){
			if (d.cosType == 'Execution Cost'){
				return d.cosElementName;
			}
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
				.elasticX(true)
				.yAxisLabel('', 50);

	sec.on('pretransition', function(chart){
		chart.selectAll('g.x text')
		.attr('transform', 'translate(-10) rotate(300)')
		.attr('style', 'text-anchor:end');

		chart.selectAll('g.x')
		.append('text')
		.attr('class', 'x-axis-label')
		.attr('text-anchor', 'middle')
		.attr('x', (width-150)/2)
		.attr('y', (height+50)/2)
		.text('X axis');

		chart.selectAll('g.y')
		.append('text')
		.attr('class', 'y-axis-label')
		.attr('text-anchor', 'middle')
		.attr('y', (height-50)/2)
		.attr('x', -100)
		.text('Y axis');

	});

	dc.renderAll();

};