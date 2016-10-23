function makegraphs(error, dashJson, secJson) {
  
    var PMlist = dashJson;
    var secVar = secJson;
    PMlist.forEach(function(d){
        d["PM"] = d[0];
        
    });
    
//    create a crossfilter instance
    var ndx = crossfilter(PMlist);
    
//    define data dimensions
    var nameDim = ndx.dimension(function(d) {return})
};