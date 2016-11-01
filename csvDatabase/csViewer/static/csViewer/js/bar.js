function beautify(Wheredata, AllData) {
	// make crossfilter references and dimensions
	var ndx = crossfilter(Wheredata);
	
	var ps0 = ndx.dimension(function(d){ return d.cosElementName;});
	var ps2 = ndx.dimension(function(d){ return d.cosElementName;});
	var ps4 = ndx.dimension(function(d){ return d.cosElementName;});
	
	var ps0Grp = ps0.group().reduceSum(function(d){return d.ps0;});
	var ps2Grp = ps2.group().reduceSum(function(d){return d.ps2;});
	var ps4Grp = ps4.group().reduceSum(function(d){return d.ps4;});
	
	var margin = {top:50, right:50, bottom:50, left:50}, 
		width = 700 - margin.left - margin.right, 
		height = 300 -margin.top - margin.bottom;
	
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
		.domain(Wheredata.map(function (d){
			return d.cosElementName;
		}));

	var sec =	dc.barChart('#sec')
				.width(width)
				.height(height)
				.dimension(ps0)
				.group(ps0Grp)
				.x(ordinalScale)
				.y(y)
				.xUnits(dc.units.ordinal)
				.brushOn(true)
				.elasticY(true)
				.elasticX(true)
				.yAxisLabel('', 50)
				.on('pretransition', function(chart){ 
					chart.selectAll('g.x text')
					.attr('transform', 'translate(-10) rotate(300)')
					.attr('style', 'text-anchor:end');
				});
	
	var thir =	dc.barChart('#thir')
					.width(width)
					.height(height)
					.dimension(ps4)
					.group(ps4Grp)
					.x(ordinalScale)
					.y(y)
					.xUnits(dc.units.ordinal)
					.brushOn(true)
					.elasticY(true)
					.elasticX(true)
					.yAxisLabel('', 50)
					.on('pretransition', function(chart){ 
						chart.selectAll('g.x text')
						.attr('transform', 'translate(-10) rotate(300)')
						.attr('style', 'text-anchor:end');
					});

	var fou =	dc.barChart('#fou')
					.width(width)
					.height(height)
					.dimension(ps2)
					.group(ps2Grp)
					.x(ordinalScale)
					.y(y)
					.xUnits(dc.units.ordinal)
					.brushOn(true)
					.elasticY(true)
					.elasticX(true)
					.yAxisLabel('', 50)
					.on('pretransition', function(chart){ 
						chart.selectAll('g.x text')
						.attr('transform', 'translate(-10) rotate(300)')
						.attr('style', 'text-anchor:end');
					});

	dc.renderAll();
};



	// sec.on('pretransition', function(chart){
	// 	chart.selectAll('g.x text')
	// 	.attr('transform', 'translate(-10) rotate(300)')
	// 	.attr('style', 'text-anchor:end');
	// });
		// chart.selectAll('g.x')
		// .append('text')
		// .attr('class', 'x-axis-label')
		// .attr('text-anchor', 'middle')
		// .attr('x', (width-150)/2)
		// .attr('y', (height+50)/2)
		// .text('X axis');
// });
	
	// 	chart.selectAll('g.y')
	// 	.append('text')
	// 	.attr('class', 'y-axis-label')
	// 	.attr('text-anchor', 'middle')
	// 	.attr('y', (height-50)/2)
	// 	.attr('x', -100)
	// 	.text('Y axis');

	// });