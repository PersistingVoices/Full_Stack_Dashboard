function beautify(Wheredata, AllData, waterfallData) {
	// make crossfilter references and dimensions
	var ndx = crossfilter(AllData);
	var ndy = crossfilter(waterfallData);

	var ps0 = ndx.dimension(function(d){ return d.cosElementName; });
	var ps1 = ndx.dimension(function(d){ return d.cosElementName; });
	var ps2 = ndx.dimension(function(d){ return d.cosElementName; });
	var ps3 = ndx.dimension(function(d){ return d.cosElementName; });
	var ps4 = ndx.dimension(function(d){ return d.cosElementName; });
	
	var ps0Grp = ps0.group().reduceSum(function(d){ return d.ps0; });
	var ps1Grp = ps1.group().reduceSum(function(d){ return d.ps1; });
	var ps2Grp = ps2.group().reduceSum(function(d){ return d.ps2; });
	var ps3Grp = ps3.group().reduceSum(function(d){ return d.ps3; });
	var ps4Grp = ps4.group().reduceSum(function(d){ return d.ps4; });
	
	var start = ndy.dimension(function(d){ return d.cosElementName;})
	var pDiff = ndy.dimension(function(d){ return d.cosElementName; });
	var nDiff = ndy.dimension(function(d){ return d.cosElementName; });
	var base = ndy.dimension(function(d){ return d.cosElementName; });
	var fin = ndy.dimension(function(d){ return d.cosElementName; });
	// fin as well later
	var startGrp = start.group().reduceSum(function(d) { return d.start; });
	var pDiffGrp = pDiff.group().reduceSum(function(d){ return d.pDiff; });
	var nDiffGrp = nDiff.group().reduceSum(function(d){ return d.nDiff; }); 
	var baseGrp = base.group().reduceSum(function(d){ return d.base; });
	var finGrp = fin.group().reduceSum(function(d){ return	d.fin; });

	var margin = {top:5, right:5, bottom:5, left:5}, 
		width = document.getElementById("ti").offsetWidth - 50; 
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

	var fou =	dc.barChart('#fou')
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

	var fiv =	dc.barChart('#fiv')
					.width(width)
					.height(height)
					.dimension(ps1)
					.group(ps1Grp)
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

	var six =	dc.barChart('#six')
					.width(width)
					.height(height)
					.dimension(ps3)
					.group(ps3Grp)
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
	width = document.getElementById("ti").offsetWidth * 1.225;
	// console.log(width)6
	var waterfall = dc.barChart('#wtr')
						.width(width)
						.height(height)
						.dimension(base)
						.group(baseGrp)
						.stack(startGrp)
						.stack(finGrp)
						.stack(pDiffGrp)
						.stack(nDiffGrp)
						.x(ordinalScale)
						.y(y)
						.xUnits(dc.units.ordinal)
						.brushOn(true)
						.elasticX(true)
						.elasticY(true)
						.yAxisLabel('', 50)
						.on('pretransition', function(chart){ 
							chart.selectAll('g.x text')
								.attr('transform', 'translate(-10) rotate(300)')
								.attr('style', 'text-anchor:end');
					});

	dc.renderAll();
};