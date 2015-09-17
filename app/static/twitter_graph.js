width=500;
height=500;
draggable=true;
start=0;
end=99999;
retweet='retweet';
reply='reply';
message='message';
size=7;

d3.json("static/twitter_model.json", function(json) {
  links = json.links;
  
links = links.filter(function(x) { return (x.time >= start && x.time <= end); });

links = links.filter(function(x) { return (x.type == retweet || x.type == reply || x.type == message); });

//sort links by source, then target
links.sort(function(a,b) {
	if (a.source > b.source) {return 1;}
	else if (a.source < b.source) {return -1;}
	else {
		if (a.target > b.target) {return 1;}
		if (a.target < b.target) {return -1;}
		else {return 0;}
	}
});

//any links with duplicate source and target get an incremented 'linknum'
for (var i=0; i<links.length; i++) {
	if (i != 0 &&
		links[i].source == links[i-1].source &&
		links[i].target == links[i-1].target) {
			links[i].linknum = links[i-1].linknum + 1;
		}
	else {links[i].linknum = 1;};
};

var nodes = {};

// Give a lookuptable for nodes and then in the lines below add username: lookup[link.source] or possibly append onto the node array later.

// Compute the distinct nodes from the links.
links.forEach(function(link) {
  link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
  link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
});

var x = d3.scale.linear()
	.domain([0, width])
	.range([0, width]);

var y = d3.scale.linear()
	.domain([0, height])
	.range([height, 0]);

var force = d3.layout.force()
	.nodes(d3.values(nodes))
	.links(links)
	.size([width, height])
	.linkDistance(1.5*Math.pow(size,2))
	.charge(-1.5*Math.pow(size,2))
	.on("tick", tick)
	.on('end', function() { force.stop(); })
	.start();

var svg = d3.selectAll("svg")
	.attr("id","network")
	.append("g");

// Per-type markers, as they don't inherit styles.
svg.append("svg:defs").selectAll("marker")
	.data(["retweet", "message", "reply","none"])
  .enter().append("svg:marker")
	.attr("id", String)
	.attr("viewBox", "0 -5 10 10")
	.attr("refX", 15)
	.attr("refY", -1.5)
	.attr("markerWidth", size)
	.attr("markerHeight", size)
	.attr("orient", "auto")
  .append("svg:path")
	.attr("d", "M0,-5L10,0L0,5");

var path = svg.append("svg:g").selectAll("path")
	.data(force.links())
  .enter().append("svg:path")
	.attr("class", function(d) { return "link " + d.type; })
	.attr("marker-end", function(d) { return "url(#" + d.type + ")"; });

var circle = svg.append("svg:g").selectAll("circle")
	.data(force.nodes())
  .enter().append("svg:circle")
	.attr("r", size)
	.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });


if (draggable){circle.call(force.drag);}; //This allows the circles to be dragged after the simulation has stopped.
	
circle.append("title")
	.text(function(d) { return "Node " + d.name; });

// Use elliptical arc path segments to doubly-encode directionality.
function tick() {

  path.attr("d", function(d) {
	var dx = d.target.x - d.source.x,
		dy = d.target.y - d.source.y,
		dr = 75/d.linknum;  //linknum is defined above
	return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
  });

  circle.attr("transform", function(d) {
	return "translate(" + d.x + "," + d.y + ")";
  });

};
});
