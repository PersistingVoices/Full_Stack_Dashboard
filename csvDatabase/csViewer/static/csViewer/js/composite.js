function beautify(Wheredata, AllData){

	var ndx = crossfilter(Wheredata);
	
	var ps0 = ndx.dimension(function(d){ return d.cosElementName;});
	var ps2 = ndx.dimension(function(d){ return d.cosElementName;});
	var ps4 = ndx.dimension(function(d){ return d.cosElementName;});
	
	var ps0Grp = ps0.group().reduceSum(function(d){return d.ps0;});
	var ps2Grp = ps0.group().reduceSum(function(d){return d.ps2;});
	var ps4Grp = ps0.group().reduceSum(function(d){return d.ps4;});
	
	var linechart1 = dc.compositeChart('#sec');

	var margin = {top:50, right:50, bottom:50, left:50}, 
		width = 700 - margin.left - margin.right, 
		height = 600 -margin.top - margin.bottom;

	var ordinalScale = d3.scale.ordinal()
		.domain(Wheredata.map(function (d){
			return d.cosElementName;
		}));

	linechart1.width(width)
		.height(height)
		.margins(margin)
		.dimension(ps0)
	.group(ps0Grp)
		.valueAccessor(function(d){
			return d.ps0;
		})
		.title('something')
		.x(ordinalScale)
		.xUnits(dc.units.ordinal)
			.compose([
				dc.lineChart(linechart1).group(ps0Grp, "ps0grp").colors("#F00"), 
				dc.lineChart(linechart1).group(ps4Grp, "ps4grp"), 
		])
		.on('pretransition', function(chart){ 
			chart.selectAll('g.x text')
			.attr('transform', 'translate(-10) rotate(300)')
			.attr('style', 'text-anchor:end');
		});

	dc.renderAll();
};