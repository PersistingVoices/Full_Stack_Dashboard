function makeGraphs(data) { 
	
	//create a crossfilter instance
	//named after n-dimentions
	console.log(data)
	var ndx = crossfilter(data);
	// console.log(ndx)
	var dim = ndx.dimension(function(d){ return(d['PS1']);});
	var grp = dim.group();

	dc.barChart("#PM-Chart")
		.dimension(dim)
		.width(1000)
		// .height(200)
		.group(grp)
		.x(d3.scale.ordinal().domain(data.map(function (d) {
			// body...
			return d.PM.slice(0,2);
		})))
		.y(d3.scale.linear().domain([0,5]))
		// .y(d3.scale.linear().domain(data.map(function(d){
		// 	// body...
		// 	console.log(Math.round(d.PS1)/100000);
		// 	return Math.round(d.PS1)/100000;
		// })))
		.xUnits(dc.units.ordinal)
		.brushOn(true)
		.centerBar(true)
		.xAxisPadding(500)
		.yAxisPadding(10);

	dc.renderAll();
};