function makeGraphs(data) { 
	
	//create a crossfilter instance
	//named after n-dimentions

	var width = 1000, height = 500;
	
	var ndx = crossfilter(data);
	var dim = ndx.dimension(function(d){ return d.PS1;});
	var grp = dim.group();

	var ordinalScale = d3.scale.ordinal()
		.domain(data.map(function (d) {
			// body...
			return d.PM;
		}))
		.rangePoints([0,width],1);

	// var yAxis2 = d3.scale.linear()
	// 					.domain(data.map(function(d){
	// 						// console.log(d.PS1);
	// 						// console.log(Math.round(d.PS1)/1000000);
	// 						return Math.round(d.PS1)/1000000;
	// 					}));

	var yAxis = d3.scale.linear()
						.domain([0,3]);

	var fir = dc.barChart("#PM")
				.width(width)
				.height(height)
				.dimension(dim)
				.group(grp)
				.x(ordinalScale)
				.y(yAxis)
				.gap(1)
				.xUnits(dc.units.ordinal)
				.brushOn(true)
				.centerBar(true)
				.renderHorizontalGridLines(true)
	
	fir.renderlet(function(chart){
		chart.selectAll("g.x text")
		.attr('transform', 'translate(-10,-100) rotate(270)');
	});

	dc.renderAll();

};