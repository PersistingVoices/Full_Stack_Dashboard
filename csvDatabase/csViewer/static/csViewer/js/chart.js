function makeGraphs(data) { 
	
	//create a crossfilter instance
	//named after n-dimentions

	var width = 1000, height = 500;
	
	var ndx = crossfilter(data);
	var PS1Dim = ndx.dimension(function(d){ return d.PS1; });
	var PMDim = ndx.dimension(function(d){ return d.PM; });

	// value d.PS1 needs to be divided by 2 as group() apparantly finds 2 instanaces of that value in the source data array. 
	// reduceSum finds the number of instances, and sums them all up, so its quite inconvient to use this func, use another function.
	var PMgrp = PMDim.group().reduceSum(function(d){ return d.PS1/2; });
	// console.log(PMgrp.all());
	var ordinalScale = d3.scale.ordinal()
		.domain(data.map(function (d) {
			// body...
			return d.PM;
		}))
		.rangePoints([0,width],1)
		.rangeBands([0, height]);

	var yAxis = d3.scale.linear()
						.domain([0,200000000]);

	var fir = dc.barChart("#PM")
				.width(width)
				.height(height)
				.dimension(PMDim)
				.group(PMgrp)
				.x(ordinalScale)
				.y(yAxis)
				.gap(1)
				.xUnits(dc.units.ordinal)
				.brushOn(true)
				.centerBar(true)
				.renderHorizontalGridLines(true)
				.xAxisPadding('length:50');
	
	fir.renderlet(function(chart){
		console.log(chart);
		chart.selectAll("g.x text")
		.attr('transform', ' translate(-10) rotate(270)')
		.attr('style', 'text-anchor:start');
		var barsData = [];
		// transferrs all bars characteristics to a handler 'bars'
		var bars = chart.selectAll('.bar').each(function (d){
			barsData.push(d);
		});

		// Remove old values if found
		d3.select(bars[0][0].parentNode).select('#inline-labels').remove;
		// Create new group for labels
		var gLabels = d3.select(bars[0][0].parentNode).append('g')
														.attr('id', 'inline-labels');
		for (var i= bars[0].length - 1; i>=0; i--){ 
			var b = bars[0][i];
			if (+b.getAttribute('height') < 18) continue;

			// gLabels.append('text')
			// 	.text(barsData[i].y)
			// 	.attr('x', +b.getAttribute('x') - (b.getAttribute('width')/2))
			// 	.attr('y', +b.getAttribute('y') -10)
			// 	.attr('fill', 'blue');
		}

	});

	dc.renderAll();

};

